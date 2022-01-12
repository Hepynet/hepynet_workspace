import atlas_mpl_style as ampl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ampl.use_atlas_style(usetex=False)

# Meta info
df_lm_path = "/net/s3_datae/yangz/zprime/data_frames/21-0120-sys/low_mass/tree_NOMINAL/zprime_low_m_quadtype_2_unblind.feather"
df_hm_path = "/net/s3_datae/yangz/zprime/data_frames/21-0120-sys/high_mass/tree_NOMINAL/zprime_high_m_quadtype_2_unblind.feather"

bkg_sm = ["bkg_ggZZ", "bkg_qcd", "bkg_fakes_diboson"]
bkg_other = ["bkg_fakes_data"]

my_figsize = (8.333, 8.333)

# Load inputs
df_lm = pd.read_feather(df_lm_path)
df_hm = pd.read_feather(df_hm_path)

mz1_bkg_sm = df_hm.loc[df_hm["sample_name"].isin(bkg_sm), "mz1"].values
mz2_bkg_sm = df_hm.loc[df_hm["sample_name"].isin(bkg_sm), "mz2"].values
mzz_bkg_sm = df_hm.loc[df_hm["sample_name"].isin(bkg_sm), "mzz"].values
wt_bkg_sm = df_hm.loc[df_hm["sample_name"].isin(bkg_sm), "weight"].values

mz1_bkg_other = df_hm.loc[df_hm["sample_name"].isin(bkg_other), "mz1"].values
mz2_bkg_other = df_hm.loc[df_hm["sample_name"].isin(bkg_other), "mz2"].values
mzz_bkg_other = df_hm.loc[df_hm["sample_name"].isin(bkg_other), "mzz"].values
wt_bkg_other = df_hm.loc[df_hm["sample_name"].isin(bkg_other), "weight"].values

mz1_sig_15 = df_lm.loc[df_lm["sample_name"] == "sig_Zp015", "mz1"].values
mz2_sig_15 = df_lm.loc[df_lm["sample_name"] == "sig_Zp015", "mz2"].values
mzz_sig_15 = df_lm.loc[df_lm["sample_name"] == "sig_Zp015", "mzz"].values
wt_sig_15 = df_lm.loc[df_lm["sample_name"] == "sig_Zp015", "weight"].values

mz1_sig_35 = df_lm.loc[df_lm["sample_name"] == "sig_Zp035", "mz1"].values
mz2_sig_35 = df_lm.loc[df_lm["sample_name"] == "sig_Zp035", "mz2"].values
mzz_sig_35 = df_lm.loc[df_lm["sample_name"] == "sig_Zp035", "mzz"].values
wt_sig_35 = df_lm.loc[df_lm["sample_name"] == "sig_Zp035", "weight"].values

mz1_sig_51 = df_hm.loc[df_hm["sample_name"] == "sig_Zp051", "mz1"].values
mz2_sig_51 = df_hm.loc[df_hm["sample_name"] == "sig_Zp051", "mz2"].values
mzz_sig_51 = df_hm.loc[df_hm["sample_name"] == "sig_Zp051", "mzz"].values
wt_sig_51 = df_hm.loc[df_hm["sample_name"] == "sig_Zp051", "weight"].values

mz1_sig_69 = df_hm.loc[df_hm["sample_name"] == "sig_Zp069", "mz1"].values
mz2_sig_69 = df_hm.loc[df_hm["sample_name"] == "sig_Zp069", "mz2"].values
mzz_sig_69 = df_hm.loc[df_hm["sample_name"] == "sig_Zp069", "mzz"].values
wt_sig_69 = df_hm.loc[df_hm["sample_name"] == "sig_Zp069", "weight"].values

# Plot functions
def make_plot(
    bkg_sm,
    wt_bkg_sm,
    bkg_other,
    wt_bkg_other,
    sig_15,
    wt_sig_15,
    sig_35,
    wt_sig_35,
    sig_51,
    wt_sig_51,
    sig_69,
    wt_sig_69,
    my_bins,
    my_range,
    my_y_lim,
    x_label,
    save_name,
    sig_scale=5,
):
    # get bkg histograms
    bkg_sm_bins, hist_edges = np.histogram(
        bkg_sm, bins=my_bins, range=my_range, weights=wt_bkg_sm
    )
    bkg_sm_hist = ampl.plot.Background(
        "SM ZZ", bkg_sm_bins, color=(7 / 256, 162 / 256, 171 / 256)
    )
    bkg_other_bins, _ = np.histogram(
        bkg_other, bins=my_bins, range=my_range, weights=wt_bkg_other
    )
    bkg_other_hist = ampl.plot.Background(
        "other", bkg_other_bins, color=(244 / 256, 121 / 256, 66 / 256)
    )
    # get sig histograms
    sig_15_bins, _ = np.histogram(
        sig_15, bins=my_bins, range=my_range, weights=wt_sig_15 * sig_scale
    )
    sig_35_bins, _ = np.histogram(
        sig_35, bins=my_bins, range=my_range, weights=wt_sig_35 * sig_scale
    )
    sig_51_bins, _ = np.histogram(
        sig_51, bins=my_bins, range=my_range, weights=wt_sig_51 * sig_scale
    )
    sig_69_bins, _ = np.histogram(
        sig_69, bins=my_bins, range=my_range, weights=wt_sig_69 * sig_scale
    )
    # plot
    fig, ax = plt.subplots(figsize=my_figsize)
    ampl.plot.plot_backgrounds([bkg_other_hist, bkg_sm_hist], hist_edges, ax=ax)
    if sig_scale != 0:
        scale_suffix = f"x{sig_scale}"
    else:
        scale_suffix = ""
    ampl.plot.plot_signal(f"Z'(15 GeV) {scale_suffix}", hist_edges, sig_15_bins)
    ampl.plot.plot_signal(f"Z'(35 GeV) {scale_suffix}", hist_edges, sig_35_bins)
    ampl.plot.plot_signal(f"Z'(51 GeV) {scale_suffix}", hist_edges, sig_51_bins)
    ampl.plot.plot_signal(f"Z'(69 GeV) {scale_suffix}", hist_edges, sig_69_bins)
    ax.set_ylim(my_y_lim[0], my_y_lim[1])
    ax.set_xlabel(x_label)
    ax.set_ylabel("Events")
    ampl.plot.draw_atlas_label(
        0.05, 0.95, ax=ax, status="internal", energy="13 TeV", lumi=139
    )
    # reorder legends
    order = [2,3,4,5,0,1]
    handles, labels = ax.get_legend_handles_labels()
    handles = [handles[i] for i in order]
    labels = [labels[i] for i in order]
    ax.legend(handles, labels, loc="upper right")
    # save figures
    fig.savefig(f"{save_name}.png")
    fig.savefig(f"{save_name}.svg")
    fig.savefig(f"{save_name}.pdf")


# Plot mz1
make_plot(
    mz1_bkg_sm,
    wt_bkg_sm,
    mz1_bkg_other,
    wt_bkg_other,
    mz1_sig_15,
    wt_sig_15,
    mz1_sig_35,
    wt_sig_35,
    mz1_sig_51,
    wt_sig_51,
    mz1_sig_69,
    wt_sig_69,
    my_bins=40,
    my_range=(10, 110),
    my_y_lim=(0, 200),
    x_label="$m_{Z1} [GeV]$",
    save_name="mass_spectrum_mz1",
)

# Plot mz2
make_plot(
    mz2_bkg_sm,
    wt_bkg_sm,
    mz2_bkg_other,
    wt_bkg_other,
    mz2_sig_15,
    wt_sig_15,
    mz2_sig_35,
    wt_sig_35,
    mz2_sig_51,
    wt_sig_51,
    mz2_sig_69,
    wt_sig_69,
    my_bins=40,
    my_range=(10, 110),
    my_y_lim=(0, 200),
    x_label="$m_{Z2} [GeV]$",
    save_name="mass_spectrum_mz2",
)

# Plot mzz
make_plot(
    mzz_bkg_sm,
    wt_bkg_sm,
    mzz_bkg_other,
    wt_bkg_other,
    mzz_sig_15,
    wt_sig_15,
    mzz_sig_35,
    wt_sig_35,
    mzz_sig_51,
    wt_sig_51,
    mzz_sig_69,
    wt_sig_69,
    my_bins=40,
    my_range=(80, 180),
    my_y_lim=(0, 600),
    x_label="$m_{4\mu} [GeV]$",
    save_name="mass_spectrum_mzz",
    sig_scale=25
)