clc;
clear all;
close all; % Close previous figures

%% defining data
X = [1.35, 1.35, 1.35, 1.36, 1.36, 1.36, 1.37, 1.37, 1.37];  % O1-C13 bond lengths
Y = [1.34, 1.36, 1.38, 1.34, 1.36, 1.38, 1.34, 1.36, 1.38]; % O2-C8 bond lengths
Z = [-382.2247697, -382.2247706, -382.1557086, -382.2247697, -382.2247706, -382.1557086, -382.2247697, -382.2247706, -382.1557086];


% Convert Ha to eV
Z = (Z - min(Z)) * 27.2114;

%% Step 2: Create Grid and Interpolate Data
[Xq, Yq] = meshgrid(linspace(min(X), max(X), 50), linspace(min(Y), max(Y), 50));
Zq = griddata(X, Y, Z, Xq, Yq, 'cubic'); % Interpolated PES

%% Step 3: Plot 3D Surface
figure;
surf(Xq, Yq, Zq);

% Step 4: Customize Appearance
colormap(flipud(pink(128)));  % Pink-purple gradient colormap
shading interp; % Smooth shading
colorbar; % Show color scale
xlabel('Bond Length 1 (O1-C13)'); ylabel('Bond Length 2 (O2-C8)'); zlabel('Potential Energy (eV)');
title('Potential Energy Surface (PES)');
view(150, 30); % Adjust view angle

% Step 5: Save Figure
saveas(gcf, '/Users/monicautashiro-aichouri/Desktop/PES_plot.png');
