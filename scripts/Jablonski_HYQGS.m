% Load data from Excel
filename = 'HYQCalculations.xlsx';
sheet = 'CPCMMO';
data = readtable(filename, 'Sheet', sheet);

% Select HOMO-3 (MO #25) to LUMO+3 (MO #32)
mo_range = 25:32; % MO numbers
subset = data(ismember(data.("NO"), mo_range), :);
mo_numbers = subset.("NO"); 

% Colors
pink = [255, 182, 195]/255;
blue = [0, 146, 155]/255;   

% Setup plot
figure;
hold on;

% Define HOMO/LUMO color
hl_color = [0/255, 146/255, 155/255];

% Evenly space on x-axis
x_center = 1;   
half_width = 0.4; 
y = subset.E_Eh_;

% Draw energy levels
for i = 1:length(y)
    MO = mo_numbers(i);
    yi = y(i);

    % Assign color
    if MO <= 28
        color = pink;
    else
        color = blue;
    end

    % Set x-position
    if MO <= 30
        % stack vertically at x = 1
        xi = x_center;
        x_coords = [xi - half_width, xi + half_width];
    elseif MO == 31
        % left-aligned
        xi = x_center - half_width/1.5;
        x_coords = [xi - half_width/2, xi + half_width/2];
    elseif MO == 32
        % right-aligned
        xi = x_center + half_width/1.5;
        x_coords = [xi - half_width/2, xi + half_width/2];
    end

    % Draw horizontal line
    plot(x_coords, [yi, yi], 'Color', color, 'LineWidth', 2);

    % Label each MO
    text(mean(x_coords), yi + 0.01, sprintf('MO %d', MO), ...
        'HorizontalAlignment', 'center', 'FontSize', 10);
end


% Aesthetics
ylim([min(y)-0.05, max(y)+0.05]);
xlim([x_center - 1, x_center + 1]);
set(gca, 'XTick', []);
ylabel('Energy (Eh)');
box on;
title('');
xticklabels([]);
hold off;

output_file = 'MO_Jablonski_Diagram.png';
exportgraphics(gcf, output_file, 'Resolution', 300);
