%% Housekeeping

clear

%% Values

Simulation_Time = 300;
out=sim('PID_Tuning_models',Simulation_Time);
K_m = 0.025;
tau_m = 1/12; % Mins (Dead time)
T_m = 1/2; % Mins

%% Run and Import Data from Simulink

% ZN 1st Method

x1 = out.tout;
y1 = out.ZN1.signals.values;

y1_MV = out.ZNMV1.signals.values; % Manipulated Variable

% ZN 2nd Method

y2 = out.ZN2.signals.values;

y2_MV = out.ZNMV2.signals.values; % Manipulated Variable

% Matlab Automatic Tuner

y3 = out.Auto1.signals.values;

y3_MV = out.Auto1MV.signals.values; % Manipulated Variable

% Manual Tuning

%{
CC_Kc = (1.35/K_m)*((T_m/tau_m)+0.185);
CC_Ki = CC_Kc*(2.5*tau_m)*((T_m+0.185*tau_m)/(T_m+0.611*tau_m));
CC_Kd = CC_Kc*(0.37*tau_m)*(T_m/(T_m+0.185*tau_m));
%}

y4 = out.CC.signals.values;
y4_MV = out.CCMV.signals.values;

%% Plots

tiledlayout(2,1)

%nexttile([1 2])
nexttile
plot(x1,y1)
hold on 
plot(x1,y2)
hold on 
plot(x1,y3)
hold on 
plot(x1,y4)
xlabel('Time (Seconds)')
ylabel('Flow Rate (L/min)')
title({'Comparison of PID Tuning Methods'})
grid on
legend('Ziegler-Nichols Open Loop','Ziegler-Nichols Closed Loop', 'MATLAB Automatic Tuner')
xlim([0,200])

nexttile
plot(x1,y1_MV)
hold on 
plot(x1,y2_MV)
hold on 
plot(x1,y3_MV)
hold on 
plot(x1,y4_MV)
xlabel('Time (Seconds)')
ylabel('Pump Speed (Rpm)')
title({'Manipulated Variable - Pump Speed'})
grid on
legend('Ziegler-Nichols Open Loop','Ziegler-Nichols Closed Loop', 'MATLAB Automatic Tuner')
xlim([0,200])

%{
nexttile
plot(x2,y2)
xlim([0,20])
ylim([1,4])
xlabel('Time (Seconds)')
ylabel('Flow Rate (L/min)')
title({'Steady State response of dynamic model w/ pump', 'oscillations for a pump speed of 100 rpm)'})
grid on
%}