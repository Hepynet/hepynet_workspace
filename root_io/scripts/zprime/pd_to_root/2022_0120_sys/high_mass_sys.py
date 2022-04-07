import array
import pathlib

import numpy as np
import pandas as pd
import ROOT

df_dir = pathlib.Path("/data/zprime/data_frames_fit/22-0120-sys/high_mass")
ntup_dir = pathlib.Path("/data/zprime/ntuples_fit/22-0120-sys/high_mass")
ntup_dir.mkdir(parents=True, exist_ok=True)

samples = [
    # "data_all",
    "bkg_qcd",
    "bkg_ggZZ",
    "bkg_fakes_data",
    "bkg_fakes_diboson",
    "bkg_ttv",
    "bkg_vvv",
    "bkg_ttbar",
    "bkg_zll",
    "sig_Zp027",
    "sig_Zp031",
    "sig_Zp035",
    "sig_Zp039",
    "sig_Zp042",
    "sig_Zp045",
    "sig_Zp048",
    "sig_Zp051",
    "sig_Zp054",
    "sig_Zp057",
    "sig_Zp060",
    "sig_Zp063",
    "sig_Zp066",
    "sig_Zp069",
    "sig_Zp072",
    "sig_Zp075",
]
branch_list = ["mz1", "mz2", "mz1_mz2", "ptz1", "ptz2", "mzz", "dnn_out_sig", "weight"]
sys_wt_list = [
    "weight_qcd_scale_up_mz1",
    "weight_qcd_scale_down_mz1",
    "weight_qcd_scale_up_mz2",
    "weight_qcd_scale_down_mz2",
    "weight_pdf_up_mz1",
    "weight_pdf_up_mz2",
    "weight_alpha_s_up_mz1",
    "weight_alpha_s_up_mz2",
]
ntup_name = "ntup"

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

for var in variations:
    print(f"Variation: {var}")
    ntup_dir_var = ntup_dir / var
    ntup_dir_var.mkdir(parents=True, exist_ok=True)
    cur_samples = samples
    if var == "tree_NOMINAL":
        cur_samples.append("data_all")
    for sample in cur_samples:
        print(f"Generating fit ntuples for: {sample}")
        # read dataframe
        df_path = df_dir / var / f"{sample}.feather"
        df: pd.DataFrame = pd.read_feather(df_path)
        # prepare ntuple file
        ntup_path = ntup_dir_var / f"{sample}.root"
        root_file = ROOT.TFile(ntup_path.as_posix(), "RECREATE")
        root_file.cd()
        # dump
        dump_features = branch_list[:]
        if sample == "bkg_qcd" and var == "tree_NOMINAL":
            dump_features += sys_wt_list
        ntup = ROOT.TNtuple(ntup_name, ntup_name, ":".join(dump_features))
        fit_array = df[dump_features].to_numpy()
        for row in fit_array:
            fill_values = list(row)
            ntup.Fill(array.array("f", fill_values))
        root_file.cd()
        ntup.Write()
        root_file.Close()
