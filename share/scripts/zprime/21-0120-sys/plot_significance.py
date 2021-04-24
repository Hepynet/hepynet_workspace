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
    3.414,
    6.242,
    6.741,
    6.932,
    7.439,
    7.568,
    8.003,
    8.207,
    11.414,
    14.544,
    18.445,
    24.697,
    37.445,
    29.501,
    35.316,
    35.019,
    40.278,
    45.247,
    50.456,
    55.987,
    59.871,
    63.654,
    70.029,
    105.979,
    136.965,
]

fig, ax = plt.subplots()
ax.scatter(x_mass, significances, s=200)
ax.set_xlabel("mass [GeV]]")
ax.set_ylabel("significance improvement [%]")
ampl.plot.draw_atlas_label(0.05, 0.95, ax=ax, status="wip", energy="13 TeV", lumi=139)
fig.suptitle("significance improvement")
fig.savefig("significance_improve.png")
