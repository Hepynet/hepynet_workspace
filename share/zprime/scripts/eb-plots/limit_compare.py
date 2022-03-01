import atlas_mpl_style as ampl
import matplotlib.pyplot as plt
import numpy as np

ampl.use_atlas_style(usetex=False)


mass_points = [
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
exp_limits_dnn_1d = [
    0.002298735,
    0.002810603,
    0.003145797,
    0.003436513,
    0.003672908,
    0.003797005,
    0.003928107,
    0.004125384,
    0.004364662,
    0.004714059,
    0.005447839,
    0.005955226,
    0.007465217,
    0.011538393,
    0.011797741,
    0.014825206,
    0.019784635,
    0.024071235,
    0.031274625,
    0.041689596,
    0.062439935,
    0.087324473,
    0.119059252,
    0.143145589,
    0.169936037,
]
obs_limits_dnn_1d = [
    0.001799254,
    0.002735184,
    0.00353255,
    0.003221289,
    0.003686119,
    0.003264037,
    0.002613003,
    0.004344898,
    0.004791725,
    0.005987512,
    0.005728937,
    0.007846471,
    0.014390391,
    0.014016949,
    0.014091288,
    0.015513684,
    0.014187328,
    0.022290515,
    0.031368878,
    0.055245094,
    0.05039919,
    0.065809842,
    0.099325001,
    0.129499358,
    0.165800586,
]

fig, ax = plt.subplots(figsize=(8.333, 8.333))

ax.plot(
    mass_points,
    exp_limits_dnn_1d,
    color="black",
    linestyle="dashed",
    label="ATLAS exp.",
)
ax.plot(
    mass_points,
    obs_limits_dnn_1d,
    color="purple",
    linestyle="-",
    label="ATLAS obs.",
)

x = [5, 200]
y = [0.0095, 0.35]
y_high = [0.35, 0.35]
ax.plot(x, y, color="red", label="Neutrino Trident")
ax.fill_between(x, y, y_high, facecolor="red", alpha=0.2)

x = [10, 1000]
y = [0.002, 0.2]
y_low = [0.002, 0.002]
ax.plot(x, y, color="green", label="$B_s$ mixing")
ax.fill_between(x, y, y_low, facecolor="green", alpha=0.2)

ax.text(
    0.5,
    0.5,
    "$b->s\mu^+\mu^-$ anomaly \n explanation allowed",
    verticalalignment="bottom",
    horizontalalignment="left",
    rotation=45,
    transform=ax.transAxes,
    color="royalblue",
    fontsize=22,
)

ax.set_xlim(5, 1000)
ax.set_xscale("log")
ax.set_xlabel(r"$m_{Z'}$ [GeV]")

ax.set_ylim(0.002, 0.35)
ax.set_yscale("log")
ax.set_ylabel(r"$g_{Z'}$")

ax.legend(loc="lower right", facecolor="white", edgecolor="black", framealpha=1.0)
ampl.plot.draw_atlas_label(
    0.05, 0.95, ax=ax, status="internal", energy="13 TeV", lumi=139
)

fig.savefig("limit_compare.png")
fig.savefig("limit_compare.svg")
fig.savefig("limit_compare.pdf")
