%turns out it has issues coverting data thats coming over UDP (unable to change back to integer[what we need for plots] in system it doesnt work with UDP data)
%Came up with another plan to do it by python though it has delays in live plotting after changing sampling to 92hz you can see that in Main page as Import_Socket )

clc;
clear;

u = udpport("datagram", "LocalPort", 9500);
disp("Listening on UDP port 9500...");

timestamps = [];
weights = [];
csvFile = "esp32_weight_log.csv";
fid = fopen(csvFile, 'w');
fprintf(fid, "Time,Weight\n");

figure;
h = plot(NaN, NaN, 'b.-');
xlabel('Time (s)');
ylabel('Force(N)');
title('Live Weight Plot');
grid on;

startTime = tic;

while true
    if u.NumDatagramsAvailable > 0
        data = read(u, 1, "string");  
        display(data);
        weight = str2double(data);

        t = toc(startTime);    
        
        % Append data
        timestamps(end+1) = t;
        weights(end+1) = weight;
        
        % Update plot
        set(h, 'XData', timestamps, 'YData', weights);
        drawnow limitrate

        % Write to CSV
        fprintf(fid, "%.3f,%.2f\n", t, weight);
    end
    pause(0.05); 
end

