# Using 21-0120-sys inputs with updated process added (fakes, ttv, etc. )


from calendar import c
import pathlib
import sys

import pandas as pd
import psutil
import uproot

MB = 1024 * 1024
GB = MB * 1024

# setups
ntup_dir = pathlib.Path(f"/data/zprime/ntuples/21-0120-sys")
df_dir = pathlib.Path(f"/data/zprime/data_frames/22-0120-sys")
df_dir.mkdir(parents=True, exist_ok=True)

variations = [
    "tree_NOMINAL",
    "tree_FT_EFF_B_systematics__1down",
    "tree_FT_EFF_B_systematics__1up",
    "tree_FT_EFF_C_systematics__1down",
    "tree_FT_EFF_C_systematics__1up",
    "tree_FT_EFF_Light_systematics__1down",
    "tree_FT_EFF_Light_systematics__1up",
    "tree_FT_EFF_extrapolation__1down",
    "tree_FT_EFF_extrapolation__1up",
    "tree_FT_EFF_extrapolation_from_charm__1down",
    "tree_FT_EFF_extrapolation_from_charm__1up",
    "tree_MUON_EFF_ISO_STAT__1down",
    "tree_MUON_EFF_ISO_STAT__1up",
    "tree_MUON_EFF_ISO_SYS__1down",
    "tree_MUON_EFF_ISO_SYS__1up",
    "tree_MUON_EFF_RECO_STAT__1down",
    "tree_MUON_EFF_RECO_STAT__1up",
    "tree_MUON_EFF_RECO_STAT_LOWPT__1down",
    "tree_MUON_EFF_RECO_STAT_LOWPT__1up",
    "tree_MUON_EFF_RECO_SYS__1down",
    "tree_MUON_EFF_RECO_SYS__1up",
    "tree_MUON_EFF_RECO_SYS_LOWPT__1down",
    "tree_MUON_EFF_RECO_SYS_LOWPT__1up",
    "tree_MUON_EFF_TTVA_STAT__1down",
    "tree_MUON_EFF_TTVA_STAT__1up",
    "tree_MUON_EFF_TTVA_SYS__1down",
    "tree_MUON_EFF_TTVA_SYS__1up",
    "tree_MUON_ID__1down",
    "tree_MUON_ID__1up",
    "tree_MUON_MS__1down",
    "tree_MUON_MS__1up",
    "tree_MUON_SAGITTA_RESBIAS__1down",
    "tree_MUON_SAGITTA_RESBIAS__1up",
    "tree_MUON_SAGITTA_RHO__1down",
    "tree_MUON_SAGITTA_RHO__1up",
    "tree_MUON_SCALE__1down",
    "tree_MUON_SCALE__1up",
    "tree_PRW_DATASF__1down",
    "tree_PRW_DATASF__1up",
]

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

feature_list_data = [f for f in feature_list]
feature_list_data[-1] = "weight"

feature_list_fakes_data = [f for f in feature_list]
feature_list_fakes_data[-1] = "weightR"

feature_list_final = [f.lower() for f in feature_list]
feature_list_final[-1] = "weight"

bkg_sys_wt_list = [
    "weight_QCD_SCALE_UP_MZ1",
    "weight_QCD_SCALE_DOWN_MZ1",
    "weight_QCD_SCALE_UP_MZ2",
    "weight_QCD_SCALE_DOWN_MZ2",
    "weight_PDF_UP_MZ1",
    "weight_PDF_UP_MZ2",
    "weight_ALPHA_S_UP_MZ1",
    "weight_ALPHA_S_UP_MZ2",
]
bkg_sys_wt_list_final = [f.lower() for f in bkg_sys_wt_list]

data_names = {
    "data_all": "data",
}

bkg_names = {
    "bkg_ttbar": "tree_ttbar",
    "bkg_zll": "tree_zll",
    "bkg_ttv": "tree_ttv",
    "bkg_vvv": "tree_vvv",
    "bkg_qcd": "tree_364250_QCD",
    "bkg_ggZZ": "tree_ggZZ",
    "bkg_fakes_data": "fakes_new/tree_data_new",
    "bkg_fakes_diboson": "fakes_new/tree_diboson",
}

bkg_names_p4_sys = {
    "bkg_qcd": "tree_364250_QCD",
    "bkg_ggZZ": "tree_ggZZ",
}

sig_names_low = {
    "sig_Zp005": "502547_2muZp005",
    "sig_Zp007": "502548_2muZp007",
    "sig_Zp009": "502549_2muZp009",
    "sig_Zp011": "502550_2muZp011",
    "sig_Zp013": "502551_2muZp013",
    "sig_Zp015": "502552_2muZp015",
    "sig_Zp017": "502553_2muZp017",
    "sig_Zp019": "502554_2muZp019",
    "sig_Zp023": "502555_2muZp023",
    "sig_Zp027": "502556_2muZp027",
    "sig_Zp031": "502557_2muZp031",
    "sig_Zp035": "502558_2muZp035",
    "sig_Zp039": "502559_2muZp039",
}

sig_names_high = {
    "sig_Zp042": "502560_2muZp042",
    "sig_Zp045": "502561_2muZp045",
    "sig_Zp048": "502562_2muZp048",
    "sig_Zp051": "502563_2muZp051",
    "sig_Zp054": "502564_2muZp054",
    "sig_Zp057": "502565_2muZp057",
    "sig_Zp060": "502566_2muZp060",
    "sig_Zp063": "502567_2muZp063",
    "sig_Zp066": "502568_2muZp066",
    "sig_Zp069": "502569_2muZp069",
    "sig_Zp072": "502570_2muZp072",
    "sig_Zp075": "502571_2muZp075",
}

sig_masses = {
    "sig_Zp005": 5,
    "sig_Zp007": 7,
    "sig_Zp009": 9,
    "sig_Zp011": 11,
    "sig_Zp013": 13,
    "sig_Zp015": 15,
    "sig_Zp017": 17,
    "sig_Zp019": 19,
    "sig_Zp023": 23,
    "sig_Zp027": 27,
    "sig_Zp031": 31,
    "sig_Zp035": 35,
    "sig_Zp039": 39,
    "sig_Zp042": 42,
    "sig_Zp045": 45,
    "sig_Zp048": 48,
    "sig_Zp051": 51,
    "sig_Zp054": 54,
    "sig_Zp057": 57,
    "sig_Zp060": 60,
    "sig_Zp063": 63,
    "sig_Zp066": 66,
    "sig_Zp069": 69,
    "sig_Zp072": 72,
    "sig_Zp075": 75,
}

# convert to pandas DataFrame
def process_sample(sample_name, sample_path, is_sig, is_mc, m_truth_name, variation):
    print(f"Processing: {sample_name} (variation: {variation})")

    apply_cut = f"quadtype == 2"
    if is_mc:
        if "bkg_fakes_data" in sample_name:
            features = feature_list_fakes_data[:]
            apply_cut = f"(quadtype == 2) & (numfake == 2)"
        else:
            features = feature_list[:]
    else:
        features = feature_list_data[:]
    column_names = feature_list_final[:]
    if variation == "tree_NOMINAL" and sample_name == "bkg_qcd":
        features += bkg_sys_wt_list
        column_names += bkg_sys_wt_list_final

    sample_dfs = list()
    for chunk_pd in uproot.iterate(
        f"{sample_path}:{variation}",
        features,
        cut=apply_cut,
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
        elif "sig" in sample_name:
            chunk_pd = chunk_pd.assign(m_truth=sig_masses[sample_name])
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
        # special fake_diboson
        if sample_name == "bkg_fakes_diboson":
            chunk_pd["weight"] *= 0.7
        if sample_name == "bkg_zll":
            chunk_pd["weight"] *= 0.9
        if sample_name == "bkg_ttbar":
            chunk_pd["weight"] *= 0.1
        # update df list
        sample_dfs.append(chunk_pd)

    sys.stdout.write("\033[K")
    return sample_dfs


low_dir = df_dir / "low_mass"
low_dir.mkdir(parents=True, exist_ok=True)
high_dir = df_dir / "high_mass"
high_dir.mkdir(parents=True, exist_ok=True)
for var in variations:
    if var == "tree_NOMINAL":
        cur_bkg_names = bkg_names
    else:
        cur_bkg_names = bkg_names_p4_sys
    # low mass region
    print("## Processing low mass region")
    low_df_list = list()
    ## data
    if var == "tree_NOMINAL":
        for data_name, data_file in data_names.items():
            root_path = ntup_dir / f"tree_{data_file}.root"
            low_df_list += process_sample(data_name, root_path, False, False, "mz2", var)
    ## bkg
    for bkg_name, bkg_file in cur_bkg_names.items():
        root_path = ntup_dir / f"{bkg_file}.root"
        low_df_list += process_sample(bkg_name, root_path, False, True, "mz2", var)
    ## sig
    for sig_name, sig_file in sig_names_low.items():
        root_path = ntup_dir / f"tree_{sig_file}.root"
        low_df_list += process_sample(sig_name, root_path, True, True, "mz2", var)
    ## dump
    low_df: pd.DataFrame = pd.concat(low_df_list, ignore_index=True)
    del low_df_list
    save_dir = low_dir / var
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = save_dir / "zprime_low_m_quadtype_2_unblind.feather"
    print(f"## Saving to {save_path}")
    low_df.to_feather(save_path)
    del low_df

    # high mass region
    print("## Processing high mass region")
    high_df_list = list()
    ## data
    if var == "tree_NOMINAL":
        for data_name, data_file in data_names.items():
            root_path = ntup_dir / f"tree_{data_file}.root"
            high_df_list += process_sample(data_name, root_path, False, False, "mz1", var)
    ## bkg
    for bkg_name, bkg_file in cur_bkg_names.items():
        root_path = ntup_dir / f"{bkg_file}.root"
        high_df_list += process_sample(bkg_name, root_path, False, True, "mz1", var)
    ## sig
    for sig_name, sig_file in sig_names_high.items():
        root_path = ntup_dir / f"tree_{sig_file}.root"
        high_df_list += process_sample(sig_name, root_path, True, True, "mz1", var)
    ## dump
    high_df: pd.DataFrame = pd.concat(high_df_list, ignore_index=True)
    del high_df_list
    save_dir = high_dir / var
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = save_dir / "zprime_high_m_quadtype_2_unblind.feather"
    print(f"## Saving to {save_path}")
    high_df.to_feather(save_path)
    del high_df
