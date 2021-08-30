%% Housekeeping

clear

%% Run Simulink Model & Calculate filter values

Simulation_Time = 300;
out=sim('PID_noise_filter',Simulation_Time);

scope='PID_noise_filter/Spectrum Analyzer'; % For some reason sometimes to import spectrum analysis data you have to run theses 3 commands manually in the command window. No clue why...
config = get_param (gcb, 'ScopeConfiguration'); % Really tempremental import. TODO find a better alternative.
specTable = getSpectrumData(config);        % I believe to get this to work it is required that the last block that you opened by the spectrum analyzer in the simulink file.



%{
sample_rate = 1/0.01; % Calculate the sample rate in Hz given the sampling time is 0.01 sec.
Pass_Band_freq = 10/(sample_rate/2);
fprintf('Pass band freq for Butterworth filter = %2.2f', Pass_Band_freq)
%}

%% Get Data

x1 = out.tout;
y1 = out.simout1.signals.values;

y2 = out.simout3.signals.values;

y3 = out.simout4.signals.values;

x2 = cell2mat(specTable.FrequencyVector);

ampy = cell2mat(specTable.Spectrum);
ampy1 = ampy(:,1);
ampy2 = ampy(:,2);

%% Plots

tiledlayout(2,1)

nexttile
plot(x1,y1)
hold on
plot(x1,y2)
hold on
plot(x1,y3)
xlim([0,200])
legend('No Filter with Noise', 'Filter and Noise',...
    'No Filter and No Noise')
xlabel('Time (Seconds)')
ylabel('Flow Rate (L/min)')
title({'Unfiltered vs Filtered Process Signal'})
grid on

nexttile
plot(x2,ampy1)
hold on
plot(x2,ampy2)
xlim([0,50])
legend('Unfiltered Signal','Filtered Signal')
xlabel('Frequency (Hz)')
ylabel('Amplitude (dBm)')
title({'Frequency Spectrum'})
grid on