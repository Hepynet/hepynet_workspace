import numpy as np
import pandas as pd
import uproot
import matplotlib.pyplot as plt

#region = "low_mass"
region = "high_mass"

data_ntup_path = f"/net/s3_datae/yangz/zprime/ntuples_fit/22-0120-sys/{region}/tree_NOMINAL/data_all.root:ntup"
data_pd = uproot.concatenate(data_ntup_path, ["weight"], library="pd")
print("ntuples_fit - total weight:", np.sum(data_pd.to_numpy()))

pd_path = f"/net/s3_datae/yangz/zprime/data_frames_fit/22-0120-sys/{region}/tree_NOMINAL/data_all.feather"
data_pd = pd.read_feather(pd_path, ["weight"])
print("data_drames_fit - total weight:", np.sum(data_pd.to_numpy()))

# check dnn
fig, ax = plt.subplots()

pd_path = f"/net/s3_datae/yangz/zprime/data_frames_fit/22-0120-sys/{region}/tree_NOMINAL/data_all.feather"
data_pd = pd.read_feather(pd_path, ["dnn_out_sig", "weight"])
ax.hist(data_pd["dnn_out_sig"].to_numpy(), weights=data_pd["weight"].to_numpy(), label="ver22-df")

data_ntup_path = f"/net/s3_datae/yangz/zprime/ntuples_fit/22-0120-sys/{region}/tree_NOMINAL/data_all.root:ntup"
data_pd = uproot.concatenate(data_ntup_path, ["dnn_out_sig", "weight"], library="pd")
ax.hist(data_pd["dnn_out_sig"].to_numpy(), weights=data_pd["weight"].to_numpy(), label="ver22", histtype="step")

data_ntup_path = f"/net/s3_datae/yangz/zprime/ntuples_fit/21-0120-sys-best-limit/{region}/tree_NOMINAL/data_all.root:ntup"
data_pd = uproot.concatenate(data_ntup_path, ["dnn_out_sig", "weight"], library="pd")
ax.hist(data_pd["dnn_out_sig"].to_numpy(), weights=data_pd["weight"].to_numpy(), label="ver21", histtype="step")

ax.legend()
fig.savefig("compare.png")


