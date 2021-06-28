import pathlib

import pandas as pd
import uproot

from lfv_const import *

# setups
ntup_dir = pathlib.Path(f"/data/lfv/ntuples/v8")
df_dir = pathlib.Path(f"/data/lfv/data_frames/v8")
df_dir.mkdir(parents=True, exist_ok=True)
tree_name = "lfvTree"

# convert to pandas DataFrame
def process_sample(
    feature_list,
    feature_names,
    sample_name,
    sample_path,
    is_sig,
    is_mc,
    m_truth_name,
    tree_name,
    cut,
):
    print(f"Processing: {sample_name}")
    sample_dfs = list()
    for chunk_pd in uproot.iterate(
        f"{sample_path}:{tree_name}",
        feature_list[:],
        cut=cut,
        library="pd",
        step_size="200 MB",
    ):
        # use lower case for features' names
        chunk_pd.columns = feature_names[:]
        # physic para for pNN
        if ("bkg" in sample_name) or ("data" in sample_name):
            chunk_pd = chunk_pd.assign(m_truth=chunk_pd[m_truth_name])
        elif "sig" in sample_name:
            chunk_pd = chunk_pd.assign(m_truth=m_truth_dict[sample_name])
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
    return sample_dfs


# prepare emu
print("## Processing channel: emu")
feature_list_in = feature_list_in_emu
feature_list_out = feature_list_out_emu
df_emu_list = list()
for bkg_name, bkg_file in bkg_dict.items():
    root_path = ntup_dir / "background" / f"{bkg_file}.root"
    df_emu_list += process_sample(
        feature_list=feature_list_in,
        feature_names=feature_list_out,
        sample_name=bkg_name,
        sample_path=root_path,
        is_sig=False,
        is_mc=True,
        m_truth_name="ll_m",
        tree_name=tree_name,
        cut="emuChannel == 1",
    )
for sig_name, sig_file in sig_dict_emu.items():
    root_path = ntup_dir / "signal" / f"{sig_file}.root"
    df_emu_list += process_sample(
        feature_list=feature_list_in,
        feature_names=feature_list_out,
        sample_name=sig_name,
        sample_path=root_path,
        is_sig=True,
        is_mc=True,
        m_truth_name="ll_m",
        tree_name=tree_name,
        cut="emuChannel == 1",
    )
df_emu: pd.DataFrame = pd.concat(df_emu_list, ignore_index=True)
del df_emu_list
save_path = df_dir / "lfv_emu.feather"
print(f"## Saving to {save_path}")
df_emu.to_feather(save_path)
del df_emu
