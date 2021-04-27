import matplotlib.pyplot as plt
import atlas_mpl_style as ampl

ampl.use_atlas_style(usetex=False)

x_mass = [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]
auc_all_mass = [
    0.568,
    0.543,
    0.572,
    0.585,
    0.566,
    0.588,
    0.580,
    0.557,
    0.611,
    0.596,
    0.668,
    0.693,
    0.725,
]
auc_no_19 = [
    0.568,
    0.544,
    0.572,
    0.585,
    0.570,
    0.588,
    0.579,
    0.557,
    0.612,
    0.599,
    0.670,
    0.694,
    0.729,
]


fig, ax = plt.subplots()
ax.scatter(x_mass, auc_all_mass, facecolors="orange", s=200, label="all-mass-trained")
ax.scatter(
    x_mass, auc_no_19, marker="+", facecolors="black", s=200, label="no-19-trained"
)
ax.set_xlabel("mass [GeV]]")
ax.set_ylabel("Area Under Curve (AUC)")
ax.set_ylim(0, 1.4)
ax.legend(loc="upper right")
ampl.plot.draw_atlas_label(0.05, 0.95, ax=ax, status="wip", energy="13 TeV", lumi=139)
fig.suptitle("AUC Comparison")
fig.savefig("AUC_compare_low.png")
