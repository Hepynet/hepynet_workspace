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
    98.1,
    98.3,
    98.0,
    97.3,
    97.6,
    97.8,
    97.8,
    97.8,
    98.1,
    97.8,
    97.1,
    96.0,
    94.0,
    72.8,
    69.6,
    69.3,
    70.1,
    63.6,
    70.1,
    64.6,
    59.3,
    60.6,
    54.6,
    39.2,
    50.1,
]
bkg_eff = [
    90.0,
    85.7,
    84.2,
    82.8,
    82.6,
    82.8,
    82.1,
    81.8,
    77.6,
    72.9,
    67.2,
    59.2,
    46.7,
    31.6,
    26.5,
    26.4,
    25.0,
    19.4,
    21.8,
    17.2,
    13.8,
    13.8,
    10.3,
    3.63,
    4.53,
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
