import matplotlib.pyplot as plt
import atlas_mpl_style as ampl

ampl.use_atlas_style(usetex=False)

x_mass = [
    5,
    7,
    9,
    11,
    13,
    15,
    17,
    19,
    23,
    27,
    31,
    35,
    39,
    42,
    45,
    48,
    51,
    54,
    57,
    60,
    63,
    66,
    69,
    72,
    75,
]
sig_eff = [
    98.0,
    98.2,
    98.3,
    98.2,
    98.0,
    98.0,
    98.2,
    98.0,
    97.8,
    97.6,
    97.0,
    96.8,
    95.2,
    88.0,
    88.6,
    88.9,
    79.2,
    78.7,
    73.1,
    68.0,
    62.5,
    52.5,
    46.3,
    51.2,
    67.9,
]
bkg_eff = [
    92.7,
    86.2,
    85.7,
    84.7,
    84.2,
    83.8,
    82.6,
    82.2,
    77.3,
    73.0,
    66.8,
    60.7,
    52.6,
    49.5,
    46.0,
    46.0,
    32.3,
    30.2,
    23.4,
    18.6,
    15.0,
    9.89,
    6.02,
    4.26,
    6.02,
]


fig, ax = plt.subplots()
ax.scatter(x_mass, sig_eff, s=200, label="signal")
ax.scatter(x_mass, bkg_eff, s=200, label="background")
ax.set_xlabel("mass [GeV]]")
ax.set_ylabel("efficiency [%]")
ax.set_ylim(0, 140)
ax.legend(loc="upper right")
ampl.plot.draw_atlas_label(0.05, 0.95, ax=ax, status="wip", energy="13 TeV", lumi=139)
fig.suptitle("efficiency")
fig.savefig("sig_bkg_eff.png")
