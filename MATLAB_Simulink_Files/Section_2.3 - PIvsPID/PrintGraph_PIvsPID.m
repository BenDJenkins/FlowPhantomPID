%% Housekeeping

clear

%% Run Simulink Model

Simulation_Time = 300;
out=sim('PIDController_PIvsPID',Simulation_Time);

%% Import Data from Simulink

% Data for Plot 1
x1 = out.tout;
y1 = out.simout.signals.values;

% Data for Plot 2
x2 = out.tout;
y2 = out.simout1.signals.values;

% Data for Plot 3
x3 = out.tout;
y3 = out.simout2.signals.values;

% Data for Plot 4
x4 = out.tout;
y4 = out.simout3.signals.values;


%% Plots

tiledlayout(2,1)

nexttile
plot(x1,y1)
hold on
plot(x2,y2)
xlim()
legend('Without Noise','With Unfiltered Noise')
xlabel('Time (Seconds)')
ylabel('Flow Rate (L/min)')
title({'PI Controlled System'})
grid on

nexttile
plot(x3,y3)
hold on
plot(x4,y4)
xlim()
legend('Without Noise','With Unfiltered Noise')
xlabel('Time (Seconds)')
ylabel('Flow Rate (L/min)')
title({'PID Controlled System'})
grid on