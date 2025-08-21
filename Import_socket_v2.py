import os
print("Working directory is:", os.getcwd())

import socket, csv, time
import matplotlib.pyplot as plt
from collections import deque

UDP_IP = "0.0.0.0"
UDP_PORT = 9500
CSV_FILE = "thrust_log.csv"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.01)

csv_file = open(CSV_FILE, 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(["Time (s)", "Thrust (N)"])

plt.ion()
fig, ax = plt.subplots()
time_buf, thrust_buf = deque(maxlen=1000), deque(maxlen=1000)  #12s at 80 Hz
(scatter,) = ax.plot([], [], 'b.', label="Thrust")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Thrust (N)")
ax.set_title("Real-Time Thrust (~80 Hz)")
ax.legend()
ax.grid(True)

start = time.time()
plot_counter = 0

try:
    while True:
        try:
            data, _ = sock.recvfrom(1024)
            thrust = float(data.decode().strip())

            t = time.time() - start

            time_buf.append(t)
            thrust_buf.append(thrust)
            writer.writerow([t, thrust])

            # flush every 50 samples (~0.6s at 80 Hz) 
            plot_counter += 1
            if plot_counter % 50 == 0:
                csv_file.flush()

            if plot_counter % 10 == 0:
                scatter.set_data(time_buf, thrust_buf)
                ax.relim()
                ax.autoscale_view()
                plt.pause(0.001)

        except socket.timeout:
            continue
        except ValueError:
            continue

except KeyboardInterrupt:
    pass
finally:
    csv_file.flush()
    csv_file.close()
    sock.close()
    plt.ioff()
    plt.show()
