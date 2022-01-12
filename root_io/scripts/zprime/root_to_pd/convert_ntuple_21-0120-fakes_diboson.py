import pathlib
import sys

import pandas as pd
import psutil
import uproot


MB = 1024 * 1024
GB = MB * 1024

# setups
ntup_dir = pathlib.Path(f"/data/zprime/ntuples/21-0120-sys/fakes_new")
df_dir = pathlib.Path(f"/data/zprime/data_frames/21-0120-sys")
df_dir.mkdir(parents=True, exist_ok=True)

feature_list = [
    "PtL1",
    "PtL2",
    "PtL3",
    "PtL4",
    "EtaL1",
    "EtaL2",
    "EtaL3",
    "EtaL4",
    "MZ1",
    "MZ2",
    "PtZ1",
    "PtZ2",
    "MZZ",
    "PtZZ",
    "EtaZZ",
    "DeltaRl12",
    "DeltaRl34",
    "dEtal12",
    "dEtal34",
    "nJet",
    "EtaZ1",
    "EtaZ2",
    "run",
    "event",
    "quadtype",
    "weightr",
]
feature_list_final = [f.lower() for f in feature_list]
feature_list_final[-1] = "weight"

bkg_names = {
    "bkg_fakes_diboson": "diboson",
}

# convert to pandas DataFrame
def process_sample(sample_name, sample_path, is_sig, is_mc, m_truth_name, variation):
    print(f"Processing: {sample_name} (variation: {variation})")

    features = feature_list[:]
    column_names = feature_list_final[:]

    sample_dfs = list()
    for chunk_pd in uproot.iterate(
        f"{sample_path}:{variation}",
        features,
        cut=f"(quadtype == 2) & (numfake == 1)",
        library="pd",
        step_size="200 MB",
    ):
        mem_available = psutil.virtual_memory().available / GB
        mem_total = psutil.virtual_memory().total / GB
        print(
            f"RAM available {mem_available:.02f} / {mem_total:.02f} GB",
            end="\r",
            flush=True,
        )
        # use lower case for features' names
        chunk_pd.columns = column_names
        # physic para for pNN
        if ("bkg" in sample_name) or ("data" in sample_name):
            chunk_pd = chunk_pd.assign(m_truth=chunk_pd[m_truth_name])
        else:
            raise ValueError("this scripts only works for fake background")
        # additional_parameters
        mz1_mz2 = chunk_pd["mz1"].values - chunk_pd["mz2"].values
        chunk_pd["mz1_mz2"] = mz1_mz2
        # convert float64 to float32
        f64_cols = chunk_pd.select_dtypes(include="float64").columns
        chunk_pd[f64_cols] = chunk_pd[f64_cols].astype("float32")
        # add tags
        chunk_pd = chunk_pd.assign(sample_name=sample_name)
        chunk_pd = chunk_pd.assign(camp=None)
        chunk_pd = chunk_pd.assign(is_sig=is_sig)
        chunk_pd = chunk_pd.assign(is_mc=is_mc)
        # update df list
        sample_dfs.append(chunk_pd)
    sys.stdout.write("\033[K")
    return sample_dfs

low_dir = df_dir / "low_mass"
low_dir.mkdir(parents=True, exist_ok=True)
high_dir = df_dir / "high_mass"
high_dir.mkdir(parents=True, exist_ok=True)

var = "tree_NOMINAL"

# low mass region
print("## Processing low mass region")
low_df_list = list()
## bkg
for bkg_name, bkg_file in bkg_names.items():
    root_path = ntup_dir / f"tree_{bkg_file}.root"
    low_df_list += process_sample(bkg_name, root_path, False, True, "mz2", var)
## dump
low_df: pd.DataFrame = pd.concat(low_df_list, ignore_index=True)
del low_df_list
save_dir = low_dir / var
save_dir.mkdir(parents=True, exist_ok=True)
save_path = save_dir / "zprime_low_m_quadtype_2_fakes_diboson.feather"
print(f"## Saving to {save_path}")
low_df.to_feather(save_path)
del low_df

# high mass region
print("## Processing high mass region")
high_df_list = list()
## bkg
for bkg_name, bkg_file in bkg_names.items():
    root_path = ntup_dir / f"tree_{bkg_file}.root"
    high_df_list += process_sample(bkg_name, root_path, False, True, "mz1", var)
## dump
high_df: pd.DataFrame = pd.concat(high_df_list, ignore_index=True)
del high_df_list
save_dir = high_dir / var
save_dir.mkdir(parents=True, exist_ok=True)
save_path = save_dir / "zprime_high_m_quadtype_2_fakes_diboson.feather"
print(f"## Saving to {save_path}")
high_df.to_feather(save_path)
del high_df
