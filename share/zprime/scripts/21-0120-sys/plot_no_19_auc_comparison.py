import matplotlib.pyplot as plt
import atlas_mpl_style as ampl

ampl.use_atlas_style(usetex=False)

x_mass = [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]
auc_all_mass = [
    0.53098,
    0.5502,
    0.57123,
    0.5635,
    0.57242,
    0.59273,
    0.5832,
    0.5896,
    0.61989,
    0.64175,
    0.68773,
    0.70187,
    0.75969,
]
auc_no_19 = [
    0.53135,
    0.54993,
    0.57191,
    0.56511,
    0.57347,
    0.59325,
    0.58428,
    0.58856,
    0.61899,
    0.64327,
    0.68913,
    0.70378,
    0.76279,
]

fig, ax = plt.subplots()
ax.scatter(x_mass, auc_all_mass, facecolors="orange", s=200, label="all-mass-trained")
ax.scatter(
    x_mass, auc_no_19, marker="+", facecolors="black", s=200, label="no-19-trained"
)
ax.set_xlabel("mass [GeV]]")
ax.set_ylabel("Area Under Curve (AUC)")
ax.set_ylim(0.5, 1.2)
ax.legend(loc="upper right")
ampl.plot.draw_atlas_label(0.05, 0.95, ax=ax, status="wip", energy="13 TeV", lumi=139)
fig.suptitle("AUC Comparison")
fig.savefig("AUC_compare_low.png")
