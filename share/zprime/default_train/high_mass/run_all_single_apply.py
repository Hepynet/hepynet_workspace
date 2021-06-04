import os

mass_points_high = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]

command_template_1 = "hepynet ./share/zprime/default_train/high_mass/apply_best_m{p_mass:02d}.yaml"
command_template_2 = "hepynet ./share/zprime/default_train/high_mass/apply_best_m{p_mass:02d}_fixed_m_truth.yaml"
command_template_3 = "hepynet ./share/zprime/default_train/high_mass/apply_best_m{p_mass:02d}_fixed_m_truth_ntup.yaml"

for mass in mass_points_high:
    os.system(command_template_1.format(p_mass=mass))
    os.system(command_template_2.format(p_mass=mass))
    os.system(command_template_3.format(p_mass=mass))
