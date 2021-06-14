import os

mass_points_high = [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]

command_template_1 = "hepynet ./share/zprime/default_train/low_mass/check_single_mass/apply_best_limit_m{p_mass:02d}.yaml"

for mass in mass_points_high:
    os.system(command_template_1.format(p_mass=mass))
