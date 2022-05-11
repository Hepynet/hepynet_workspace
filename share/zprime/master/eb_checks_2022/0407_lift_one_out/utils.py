import numpy as np
import pathlib

low_mass_points = [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]
high_mass_points = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]

def get_mass_cut(mass):
    # sigma_range = 3.0 * (0.0401444 + 0.0122949 * mass + 0.000140695 * mass * mass)  # @ Bing Li
    # sigma_range = 3.0 * (0.193 - 0.002 * mass + 0.00035 * mass * mass)  # @ Shuzhou Zhang
    sigma = np.poly1d(
        [
            5.20753537e-08,
            3.34322964e-08,
            -2.17314377e-04,
            2.26208490e-02,
            -1.81540253e-02,
        ]
    )
    sigma_range = 3 * sigma(mass)  # @ Shuzhou Update 2022/01/24
    return (mass - sigma_range, mass + sigma_range)

def get_last_folder(input_dir:pathlib.Path, pattern):
    candidates = list(input_dir.glob(pattern))
    candidates.sort()
    if candidates:
        return candidates[-1]
    else:
        return ""