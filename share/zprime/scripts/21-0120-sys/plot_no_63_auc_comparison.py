import matplotlib.pyplot as plt
import atlas_mpl_style as ampl

ampl.use_atlas_style(usetex=False)

x_mass = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]
auc_all_mass = [
    0.77618,
    0.79201,
    0.80619,
    0.81205,
    0.82134,
    0.8214,
    0.83184,
    0.8361,
    0.8456,
    0.85483,
    0.87553,
    0.9066,
]
auc_no_63 = [
    0.77785,
    0.79372,
    0.80736,
    0.8133,
    0.82244,
    0.82194,
    0.83224,
    0.83624,
    0.84562,
    0.85522,
    0.87619,
    0.90729,
]

fig, ax = plt.subplots()
ax.scatter(x_mass, auc_all_mass, facecolors="orange", s=200, label="all-mass-trained")
ax.scatter(
    x_mass, auc_no_63, marker="+", facecolors="black", s=200, label="no-63-trained"
)
ax.set_xlabel("mass [GeV]]")
ax.set_ylabel("Area Under Curve (AUC)")
ax.set_ylim(0.5, 1.2)
ax.legend(loc="upper right")
ampl.plot.draw_atlas_label(0.05, 0.95, ax=ax, status="wip", energy="13 TeV", lumi=139)
fig.suptitle("AUC Comparison")
fig.savefig("AUC_compare_high.png")
