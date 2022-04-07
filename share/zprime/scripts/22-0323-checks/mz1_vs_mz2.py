import pandas as pd
import matplotlib.pyplot as plt

df_path = "/net/s3_datae/yangz/zprime/data_frames/22-0120-sys/high_mass/tree_NOMINAL/zprime_high_m_quadtype_2_unblind.feather"

df = pd.read_feather(df_path)
mz1 = df["mz1"]
mz2 = df["mz2"]
wt = df["weight"]

fig, ax = plt.subplots()
ax.hist2d(mz1, mz2, weights=wt)
fig.savefig("mz1_vs_mz2.png")