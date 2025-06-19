import socket
import csv
import time
import matplotlib.pyplot as plt
from collections import deque
import matplotlib.ticker as ticker

UDP_IP = "0.0.0.0"
UDP_PORT = 9500
CSV_FILE = "thrust_log2.csv"
MAX_POINTS = 200
Y_LIM = (-200, 200)
X_TICK_INTERVAL = 5
Y_TICK_INTERVAL = 50

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.01)  # Allow non-blocking read to avoid hanging

print(f"[INFO] Listening for UDP packets on {UDP_IP}:{UDP_PORT}")

csv_file = open(CSV_FILE, mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Time (s)", "Thrust (N)"])

plt.ion()
fig, ax = plt.subplots()
time_buffer = deque(maxlen=MAX_POINTS)
thrust_buffer = deque(maxlen=MAX_POINTS)
line, = ax.plot([], [], 'b.-', label="Thrust")

ax.set_title("Real-Time Thrust Measurement")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Thrust (N)")
ax.set_ylim(Y_LIM)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

ax.xaxis.set_major_locator(ticker.MultipleLocator(X_TICK_INTERVAL))
ax.yaxis.set_major_locator(ticker.MultipleLocator(Y_TICK_INTERVAL))
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.legend(loc="upper right")

start_time = time.time()
plot_counter = 0
PLOT_EVERY_N = 5  # Plot every 5th sample to prevent lag

try:
    while True:
        try:
            raw_data, addr = sock.recvfrom(1024)
            thrust_str = raw_data.decode().strip()
            thrust = float(thrust_str)

            # Optional debug
            # print(f"[DEBUG] Received thrust: {thrust}")

            t = time.time() - start_time
            time_buffer.append(t)
            thrust_buffer.append(thrust)

            csv_writer.writerow([t, thrust])
            csv_file.flush()

            plot_counter += 1
            if plot_counter % PLOT_EVERY_N == 0:
                line.set_data(time_buffer, thrust_buffer)
                ax.relim()
                ax.autoscale_view(scaley=False)
                plt.draw()
                plt.pause(0.001)

        except socket.timeout:
            continue
        except ValueError:
            print(f"[WARN] Invalid data received: {raw_data}")
            continue

except KeyboardInterrupt:
    print("\n[INFO] Data logging interrupted by user.")

finally:
    csv_file.close()
    sock.close()
    print("[INFO] Logging complete. Resources released.")