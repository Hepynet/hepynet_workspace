import atlas_mpl_style as ampl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

ampl.use_atlas_style(usetex=False)

# data
cuts = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
mass_points_high = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]
mass_points_low = [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]

limits_low = np.array(
    [
        [4.0161E-03, 3.9980E-03, 4.0044E-03, 4.0665E-03, 4.2058E-03, 4.6242E-03, 6.7146E-03, np.nan, np.nan, np.nan],
        [3.6268E-03, 3.6540E-03, 3.5908E-03, 3.5796E-03, 3.6328E-03, 4.0269E-03, 5.3508E-03, np.nan, np.nan, np.nan],
        [3.2811E-03, 3.2537E-03, 3.2058E-03, 3.2155E-03, 3.2740E-03, 3.6509E-03, 4.7507E-03, 8.7328E-03, np.nan, np.nan],
        [3.1187E-03, 3.1014E-03, 3.0227E-03, 3.0412E-03, 3.1137E-03, 3.3859E-03, 4.3848E-03, 7.8247E-03, np.nan, np.nan],
        [3.0232E-03, 2.9612E-03, 2.9005E-03, 2.8870E-03, 2.9318E-03, 3.1376E-03, 3.8456E-03, 6.5229E-03, np.nan, np.nan],
        [3.1010E-03, 3.0444E-03, 2.9685E-03, 2.9502E-03, 2.9782E-03, 3.1362E-03, 3.7310E-03, 6.4340E-03, np.nan, np.nan],
        [3.5423E-03, 3.4409E-03, 3.3382E-03, 3.3315E-03, 3.3302E-03, 3.4259E-03, 3.9441E-03, 6.3613E-03, 1.8562E-02, np.nan],
        [3.4912E-03, 3.4099E-03, 3.3417E-03, 3.3322E-03, 3.3483E-03, 3.4512E-03, 3.8155E-03, 5.6233E-03, np.nan, np.nan],
        [4.9717E-03, 4.8089E-03, 4.6229E-03, 4.6224E-03, 4.6179E-03, 4.6750E-03, 4.7539E-03, 6.1263E-03, 2.0897E-02, np.nan],
        [5.9777E-03, 5.8403E-03, 5.5829E-03, 5.6055E-03, 5.6094E-03, 5.6657E-03, 5.7111E-03, 6.5214E-03, 1.7372E-02, np.nan],
        [7.1174E-03, 7.0200E-03, 6.4437E-03, 6.4189E-03, 6.4210E-03, 6.4310E-03, 6.5111E-03, 7.0247E-03, 1.6418E-02, np.nan],
        [1.0597E-02, 1.0674E-02, 9.9775E-03, 9.8479E-03, 9.9296E-03, 9.9195E-03, 9.8610E-03, 1.0238E-02, 1.7857E-02, np.nan],
        [1.5430E-02, 1.4307E-02, 1.3133E-02, 1.3010E-02, 1.3145E-02, 1.3144E-02, 1.3061E-02, 1.3512E-02, 1.9703E-02, np.nan],
    ]
)
limits_low = np.log10(limits_low)

limits_high = np.array(
    [
        [1.8968E-02, 1.8967E-02, 1.8714E-02, 1.8821E-02, 1.8936E-02, 1.8888E-02, 1.7564E-02, 1.5407E-02, 1.4918E-02, 2.2786E-0],
        [2.1120E-02, 2.0963E-02, 2.0385E-02, 1.9298E-02, 1.8463E-02, 1.7764E-02, 1.7457E-02, 1.7223E-02, 1.7248E-02, 2.4493E-0],
        [2.2611E-02, 2.2512E-02, 2.1426E-02, 2.0344E-02, 1.9564E-02, 1.8997E-02, 1.8690E-02, 1.8619E-02, 1.9050E-02, 3.0748E-0],
        [2.7593E-02, 2.7431E-02, 2.5394E-02, 2.3672E-02, 2.2532E-02, 2.1645E-02, 2.1416E-02, 2.0851E-02, 2.1228E-02, 3.3238E-0],
        [3.9519E-02, 3.9359E-02, 3.6100E-02, 3.3476E-02, 3.1575E-02, 3.0329E-02, 2.9448E-02, 2.9122E-02, 3.2423E-02, 7.1805E-0],
        [5.6950E-02, 5.6679E-02, 4.9849E-02, 4.6073E-02, 4.3690E-02, 4.2415E-02, 4.1808E-02, 4.1607E-02, 4.6927E-02, 1.1044E-0],
        [8.7557E-02, 8.6201E-02, 7.7378E-02, 7.0808E-02, 6.7126E-02, 6.5624E-02, 6.3259E-02, 6.3482E-02, 7.5835E-02, 2.0610E-0],
        [1.2703E-01, 1.2562E-01, 1.1628E-01, 1.0588E-01, 1.0163E-01, 9.9826E-02, 9.6375E-02, 9.8982E-02, 1.2468E-01, 3.2877E-0],
        [1.8841E-01, 1.8398E-01, 1.6579E-01, 1.4895E-01, 1.4270E-01, 1.3470E-01, 1.3157E-01, 1.3361E-01, 1.6688E-01, 3.7352E-0],
        [3.0090E-01, 2.9633E-01, 2.5119E-01, 2.2668E-01, 2.0252E-01, 1.8660E-01, 1.7638E-01, 1.7577E-01, 2.1078E-01, 4.1610E-0],
        [3.8313E-01, 3.8029E-01, 3.0426E-01, 2.6112E-01, 2.4186E-01, 2.2459E-01, 2.0996E-01, 2.0050E-01, 2.3923E-01, 3.9412E-0],
        [4.5193E-01, 4.3219E-01, 3.4931E-01, 3.0834E-01, 2.7555E-01, 2.5371E-01, 2.2936E-01, 2.2552E-01, 2.9615E-01, 5.9975E-0],
    ]
)
limits_high = np.log10(limits_high)

# plot low mass
fig, ax = plt.subplots()
im = ax.imshow(limits_low, cmap="plasma")
# create colorbar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("couping limits [log]", rotation=-90, va="bottom")
# highlight selected cuts
ax.add_patch(Rectangle((0.5, -0.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 5
ax.add_patch(Rectangle((2.5, 0.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 7
ax.add_patch(Rectangle((1.5, 1.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 9
ax.add_patch(Rectangle((1.5, 2.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 11
ax.add_patch(Rectangle((2.5, 3.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 13
ax.add_patch(Rectangle((2.5, 4.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 15
ax.add_patch(Rectangle((3.5, 5.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 17
ax.add_patch(Rectangle((2.5, 6.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 19
ax.add_patch(Rectangle((3.5, 7.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 23
ax.add_patch(Rectangle((2.5, 8.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 27
ax.add_patch(Rectangle((2.5, 9.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 31
ax.add_patch(Rectangle((2.5, 10.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 35
ax.add_patch(Rectangle((2.5, 11.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 39

# adjustment
ax.set_xlabel("DNN cut")
ax.set_xticks(np.arange(len(cuts)))
ax.set_yticks(np.arange(len(mass_points_low)))
ax.set_ylabel("mass [GeV]")
ax.set_xticklabels(cuts)
ax.set_yticklabels(mass_points_low)
ax.set_title("limits - mass vs cuts")
fig.tight_layout()
ampl.plot.draw_atlas_label(0.05, 0.95, ax=ax, status="wip", energy="13 TeV", lumi=139, color="white")
# save
fig.savefig("limit_2d_cut_vs_mass_low.png")


# plot high mass
fig, ax = plt.subplots()
im = ax.imshow(limits_high, cmap="plasma")
# create colorbar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("couping limits [log]", rotation=-90, va="bottom")
# highlight selected cuts
ax.add_patch(Rectangle((7.5, -0.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 42
ax.add_patch(Rectangle((6.5, 0.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 45
ax.add_patch(Rectangle((6.5, 1.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 48
ax.add_patch(Rectangle((6.5, 2.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 51
ax.add_patch(Rectangle((6.5, 3.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 54
ax.add_patch(Rectangle((6.5, 4.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 57
ax.add_patch(Rectangle((5.5, 5.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 60
ax.add_patch(Rectangle((5.5, 6.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 63
ax.add_patch(Rectangle((5.5, 7.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 66
ax.add_patch(Rectangle((6.5, 8.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 69
ax.add_patch(Rectangle((6.5, 9.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 72
ax.add_patch(Rectangle((6.5, 10.5), 1, 1, fill=False, edgecolor="orange", lw=3))  # 75
# adjustment
ax.set_xlabel("DNN cut")
ax.set_xticks(np.arange(len(cuts)))
ax.set_yticks(np.arange(len(mass_points_high)))
ax.set_ylabel("mass [GeV]")
ax.set_xticklabels(cuts)
ax.set_yticklabels(mass_points_high)
ax.set_title("limits - mass vs cuts")
fig.tight_layout()
ampl.plot.draw_atlas_label(0.05, 0.95, ax=ax, status="wip", energy="13 TeV", lumi=139, color="white")
# save
fig.savefig("limit_2d_cut_vs_mass_high.png")
