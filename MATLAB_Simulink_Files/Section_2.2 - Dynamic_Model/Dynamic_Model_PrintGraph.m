%% Housekeeping

clear

%% Run Simulink Model

Simulation_Time = 300;
out=sim('Dynamic_Model',Simulation_Time);

%% Import Data from Simulink

% Data for Plot 1
x1 = out.tout;
y1 = out.simout.signals.values;

% Data for Plot 2
%L = length(y1(40000:end,1)); 
x2 = out.tout;
y2 = out.simout2.signals.values;

% Data for Plot 3

x3 = out.tout;
y3 = out.simout1.signals.values;

%% Plots

tiledlayout(2,2)

nexttile([1 2])
plot(x3,y3)
xlim([0,200])
xlabel('Time (Seconds)')
ylabel('Flow Rate (L/min)')
title({'Uncontrolled dynamic response w/ pump oscillations', '(Pump speed step: 0 rpm to 100 rpm)'})
grid on

nexttile
plot(x1,y1)
ylim([0,3])
xlim([0,200])
xlabel('Time (Seconds)')
ylabel('Flow Rate (L/min)')
title({'Uncontrolled dynamic response w/o pump oscillations', '(Pump speed step: 0 rpm to 100 rpm)'})
grid on

nexttile
plot(x2,y2)
xlim([0,20])
ylim([1,4])
xlabel('Time (Seconds)')
ylabel('Flow Rate (L/min)')
title({'Steady State response of dynamic model w/ pump', 'oscillations for a pump speed of 100 rpm)'})
grid on