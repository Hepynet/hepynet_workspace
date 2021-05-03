import os

command_template = "hepynet -t ./share/zprime/high_mass/apply_no_63_on_{mass:02d}.yaml"

for mass in [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]:
    os.system(command_template.format(mass=mass))