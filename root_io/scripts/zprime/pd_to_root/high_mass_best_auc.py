import array
import pathlib

import numpy as np
import pandas as pd
import ROOT

df_dir = pathlib.Path("/data/zprime/data_frames_fit/21-0120-sys-best-hyper/high_mass")
ntup_dir = pathlib.Path("/data/zprime/ntuples_fit/21-0120-sys-best-hyper/high_mass")
ntup_dir.mkdir(parents=True, exist_ok=True)

samples = [
    "bkg_qcd",
    "bkg_ggZZ",
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
branch_list = ["mz1", "mz2", "dnn_out_sig", "weight"]
ntup_name = "nominal"

for sample in samples:
    print(f"Generating fit ntuples for: {sample}")
    # read dataframe
    df_path = df_dir / f"{sample}.feather"
    df:pd.DataFrame = pd.read_feather(df_path)
    # prepare ntuple file
    ntup_path = ntup_dir / f"{sample}.root"
    root_file = ROOT.TFile(ntup_path.as_posix(), "RECREATE")
    root_file.cd()
    ntup = ROOT.TNtuple(ntup_name, ntup_name, ":".join(branch_list))
    # dump
    fit_array = df[branch_list].to_numpy()
    for row in fit_array:
        fill_values = list(row)
        ntup.Fill(array.array("f", fill_values))
    root_file.cd()
    ntup.Write()
    root_file.Close()
