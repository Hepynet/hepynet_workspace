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

significances = [
    0.876,
    2.218,
    2.253,
    2.415,
    2.414,
    2.481,
    2.937,
    2.802,
    4.009,
    5.042,
    6.283,
    7.852,
    9.876,
    25.26,
    31.34,
    32.66,
    37.99,
    40.46,
    44.28,
    48.21,
    49.85,
    51.75,
    64.30,
    101.66,
    127.74,
]

fig, ax = plt.subplots()
ax.scatter(x_mass, significances, s=200)
ax.set_xlabel("mass [GeV]]")
ax.set_ylabel("significance improvement [%]")
ampl.plot.draw_atlas_label(0.05, 0.95, ax=ax, status="wip", energy="13 TeV", lumi=139)
fig.suptitle("significance improvement")
fig.savefig("significance_improve.png")
