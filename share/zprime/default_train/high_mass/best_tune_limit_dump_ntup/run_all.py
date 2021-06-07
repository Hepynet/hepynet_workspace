import os

mass_points_high = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]

command_template = "hepynet ./share/zprime/default_train/high_mass/best_tune_limit_dump_ntup/apply_best_m{p_mass:02d}_fixed_m_truth_ntup.yaml"

for mass in mass_points_high:
    os.system(command_template.format(p_mass=mass))
