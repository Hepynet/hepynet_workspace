import matplotlib.pyplot as plt
import atlas_mpl_style as ampl

ampl.use_atlas_style(usetex=False)

x_mass = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]
auc_all_mass = [
    0.764,
    0.792,
    0.812,
    0.802,
    0.811,
    0.823,
    0.831,
    0.829,
    0.840,
    0.851,
    0.853,
    0.889,
]
auc_no_63 = [
    0.766,
    0.794,
    0.813,
    0.804,
    0.812,
    0.824,
    0.831,
    0.828,
    0.839,
    0.851,
    0.854,
    0.891,
]


fig, ax = plt.subplots()
ax.scatter(x_mass, auc_all_mass, facecolors="orange", s=200, label="all-mass-trained")
ax.scatter(
    x_mass, auc_no_63, marker="+", facecolors="black", s=200, label="no-63-trained"
)
ax.set_xlabel("mass [GeV]]")
ax.set_ylabel("Area Under Curve (AUC)")
ax.set_ylim(0, 1.4)
ax.legend(loc="upper right")
ampl.plot.draw_atlas_label(0.05, 0.95, ax=ax, status="wip", energy="13 TeV", lumi=139)
fig.suptitle("AUC Comparison")
fig.savefig("AUC_compare_high.png")
