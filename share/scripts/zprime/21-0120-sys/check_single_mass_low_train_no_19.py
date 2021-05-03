import os

command_template = "hepynet -t ./share/zprime/low_mass/apply_no_19_on_{mass:02d}.yaml"

for mass in [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]:
    os.system(command_template.format(mass=mass))