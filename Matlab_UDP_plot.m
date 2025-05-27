clc;
clear;

u = udpport("datagram", "LocalPort", 6969);

figure;
h = animatedline;
ax = gca;
ax.YGrid = 'on';
xlabel('Time (s)');
ylabel('Weight (kg)');
title('Real-time Load Cell Data via UDP');

tStart = tic;

while true
    if u.NumDatagramsAvailable > 0
        data = readline(u);  % receive packet
        weight = str2double(data);
        t = toc(tStart);
        addpoints(h, t, weight);
        drawnow limitrate;
    end
end
