import pathlib

import matplotlib.pyplot as plt
import numpy as np
import yaml
from utils import *

# Settings
#region = "high_mass"
region = "low_mass"
input_dir = pathlib.Path(
    f"/home/yangz/analysis/hepynet_workspace/run/zprime/eb_checks_2022/{region}"
)
auc_name = "auc_test_original"

if region == "high_mass":
    mass_points = high_mass_points
else:
    mass_points = low_mass_points

# Get nominal AUC
auc_nom = {}
## Get train folder
train_dir = get_last_folder(input_dir, f"*train_all_mass*")
for mm in mass_points:
    apply_dir = get_last_folder(train_dir, f"apply/*apply_all_mass_on_m_{mm:02d}*")
    result_path = apply_dir / "epoch_final/metrics/roc_auc.yaml"
    with open(result_path, "r") as f:
        result = yaml.load(f, Loader=yaml.FullLoader)
        auc_nom[mm] = result["roc_auc"][auc_name]

# Get the results in each mass point
auc = {}
for m in mass_points:
    auc[m] = {}
    # Get train folder
    candidates = list(input_dir.glob(f"*train_no_m_{m:02d}_*"))
    candidates.sort()
    train_dir = candidates[-1]
    print("train_folder:", train_dir)
    # Get the results in each mass point
    for mm in mass_points:
        # Get apply folder
        candidates = list(train_dir.glob(f"apply/*apply_no_m_{m:02d}_on_m_{mm:02d}"))
        candidates.sort()
        apply_dir = candidates[-1]
        print("  > apply_folder:", apply_dir)
        # Get the result
        result_path = apply_dir / "epoch_final/metrics/roc_auc.yaml"
        with open(result_path, "r") as f:
            result = yaml.load(f, Loader=yaml.FullLoader)
            auc[m][mm] = result["roc_auc"][auc_name]

print("auc_nom:", auc_nom)
print("auc:", auc)

# Plot Heatmap
data = np.array(
    [
        [(1 - (auc[m][mm] / auc_nom[mm])) * 100 for mm in mass_points]
        for m in mass_points
    ]
)
print(list(data))
fig, ax = plt.subplots()
## Plot heatmap
im = ax.imshow(data, cmap="RdBu_r")
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("AUC difference (%)", rotation=-90, va="bottom")
## Set ticks
tick_labels = [str(x) for x in mass_points]
ax.set_xticks(np.arange(len(mass_points)))
ax.set_yticks(np.arange(len(mass_points)))
ax.set_xticklabels(tick_labels)
ax.set_yticklabels(tick_labels)
ax.tick_params(top=True, bottom=False, labeltop=False, labelbottom=True)
## Set labels
ax.set_title(f"{region} region")
ax.set_xlabel("Removed mass point [GeV]")
ax.set_ylabel("Applied mass point [GeV]")
## Save figure
fig.savefig(f"auc_diff_{region}_{auc_name}.png")
