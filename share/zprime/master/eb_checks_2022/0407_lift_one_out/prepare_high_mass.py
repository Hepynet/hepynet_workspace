import copy
import pathlib

from utils import *

# Set up the default parameters
high_mass_points = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]
def_cfg_train = {}
for m in high_mass_points:
    def_cfg_train[f"p_cmt_{m:02d}"] = ""

# Get template string
with open("high_mass_train_temp.txt", "r") as f:
    temp_train = f.read()
with open("high_mass_apply_temp.txt", "r") as f:
    temp_apply = f.read()

# Setup the config file
train_dir = pathlib.Path("train/high_mass")
train_dir.mkdir(parents=True, exist_ok=True)
apply_dir = pathlib.Path("apply/high_mass")
apply_dir.mkdir(parents=True, exist_ok=True)

# prepare default config
setup = copy.deepcopy(def_cfg_train)
setup["p_job_name"] = f"train_all_mass"
config = temp_train.format(**setup)
with open(train_dir / f"train_all_mass.yaml", "w") as f:
    f.write(config)
for mm in high_mass_points:
    cut_low, cut_high = get_mass_cut(mm)
    setup = {
        "p_job_name": f"apply_all_mass_on_m_{mm:02d}",
        "p_job_name_train": f"train_all_mass",
        "p_cut_low": cut_low,
        "p_cut_high": cut_high,
        "p_signal": f"sig_Zp0{mm:02d}",
    }
    config = temp_apply.format(**setup)
    with open(apply_dir / f"apply_all_mass_on_m_{mm:02d}.yaml", "w") as f:
        f.write(config)

# prepare config with one mass removed
for m in high_mass_points:
    # prepare train config
    setup = copy.deepcopy(def_cfg_train)
    setup[f"p_cmt_{m}"] = "#"
    setup["p_job_name"] = f"train_no_m_{m:02d}"
    config = temp_train.format(**setup)
    with open(train_dir / f"train_no_m_{m:02d}.yaml", "w") as f:
        f.write(config)
    # prepare apply config
    for mm in high_mass_points:
        cut_low, cut_high = get_mass_cut(mm)
        setup = {
            "p_job_name": f"apply_no_m_{m:02d}_on_m_{mm:02d}",
            "p_job_name_train": f"train_no_m_{m:02d}",
            "p_cut_low": cut_low,
            "p_cut_high": cut_high,
            "p_signal": f"sig_Zp0{mm:02d}",
        }
        config = temp_apply.format(**setup)
        with open(apply_dir / f"apply_no_m_{m:02d}_on_m_{mm:02d}.yaml", "w") as f:
            f.write(config)
    
