import atlas_mpl_style as ampl
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Setup
df_nominal_path = "/net/s3_datae/yangz/zprime/data_frames_fit/22-0120-sys/high_mass/tree_NOMINAL/bkg_qcd.feather"
df_powheg_path = "/net/s3_datae/yangz/zprime/data_frames_fit/22-0120-sys/high_mass/tree_NOMINAL/bkg_qcd_powheg.feather"
job_name = "compare_powheg"
ampl.use_atlas_style(usetex=False)
formats = ["png", "eps"]

# Get data
df_nominal = pd.read_feather(df_nominal_path)
dnn_0 = df_nominal["dnn_out_sig"]
wt_0 = df_nominal["weight"]
df_powheg = pd.read_feather(df_powheg_path)
dnn_1 = df_powheg["dnn_out_sig"]
wt_1 = df_powheg["weight"]

# Plot
#fig = plt.figure()
#gs = mpl.gridspec.GridSpec(4, 1, hspace=0.0, wspace=0.0)
#ax = fig.add_subplot(gs[0:3])
#ax.tick_params(labelbottom=False)
#ratio_ax = fig.add_subplot(gs[3], sharex=ax)
#ratio_ax.autoscale(axis="x", tight=True)
#plt.sca(ax)
fig, ax = plt.subplots()

## plot hist
bins_0, edges_0 = np.histogram(
    dnn_0, bins=20, range=(0, 0.55), weights=wt_0, density=True
)
sumw2, _ = np.histogram(dnn_0, bins=20, range=(0, 0.55), weights=np.power(wt_0, 2))
errs_0 = np.sqrt(sumw2)
ampl.plot.plot_signal("QCD nominal", edges_0, bins_0, ax=ax)

bins_1, edges_1 = np.histogram(
    dnn_1, bins=20, range=(0, 0.55), weights=wt_1, density=True
)
sumw2, _ = np.histogram(dnn_1, bins=20, range=(0, 0.55), weights=np.power(wt_1, 2))
errs_1 = np.sqrt(sumw2)
ampl.plot.plot_signal("QCD Powheg", edges_1, bins_1, ax=ax)
"""
ax.hist(
    dnn_0, bins=20, range=(0, 0.55), weights=wt_0, histtype="step", label="QCD nominal", density=True
)
ax.hist(
    dnn_1, bins=20, range=(0, 0.55), weights=wt_1, histtype="step", label="QCD Powheg", density=True
)
"""
## plot_ratio
#ampl.plot.plot_signal("ratio", edges_0, bins_1/bins_0, ax=ratio_ax)
#ratio_ax.step(edges_0[:-1], bins_1/bins_0 )
'''
ampl.plot.plot_ratio(
    edges_0,
    bins_1,
    errs_1,
    bins_0,
    errs_0,
    ratio_ax,
    plottype="raw",
    offscale_errs=True,
)
'''
## adjust figure
ax.set_yscale("log")
ax.legend()
#ratio_ax.set_ylim(0, 2)
#ratio_ax.set_xlabel("DNN_score")

for fm in formats:
    fig.savefig(f"{job_name}.{fm}")
