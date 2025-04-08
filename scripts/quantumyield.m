%% Strickler–Berg Radiative Lifetime Calculation

% Loading fluorescence spectrum
% Replace 'fluorescence_spectrum.csv' with your file path
data = readmatrix('fluorescence_spectrum.csv'); 
lambda_nm = data(:,1);    % Wavelength in nm
intensity = data(:,2);    % Fluorescence intensity (a.u.)

% Constants
n = 1.5;  % Refractive index (solvent)
c = 2.9979e10;  % Speed of light in cm/s

% Convert wavelength to wavenumber (cm^-1)
nu_bar = 1e7 ./ lambda_nm;  % in cm^-1
I_nu = intensity;           % Keep same intensity

% Interpolate to uniform spacing in wavenumber space
nu_uniform = linspace(min(nu_bar), max(nu_bar), 1000);
I_interp = interp1(nu_bar, I_nu, nu_uniform, 'pchip');

% Compute integrals using trapezoidal rule
integral_num   = trapz(nu_uniform, I_interp);                         % ∫ I(ν) dν
integral_denom = trapz(nu_uniform, I_interp ./ (nu_uniform.^3));     % ∫ I(ν)/ν^3 dν

% Strickler–Berg formula
k_rad_SB = 2.88e-9 * n^2 * (integral_num / integral_denom);  % in s^-1
tau_rad_SB = 1 / k_rad_SB;                                   % in seconds

% Output
fprintf('--- Strickler–Berg Radiative Lifetime ---\n');
fprintf('k_rad (SB): %.2e s^-1\n', k_rad_SB);
fprintf('tau_rad:    %.2e s (%.2f ns)\n', tau_rad_SB, tau_rad_SB * 1e9);
