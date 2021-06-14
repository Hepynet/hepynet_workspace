import os

mass_points_high = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]

command_template_1 = "hepynet ./share/zprime/default_train/high_mass/check_single_mass/apply_best_limit_m{p_mass:02d}.yaml"

for mass in mass_points_high:
    os.system(command_template_1.format(p_mass=mass))
