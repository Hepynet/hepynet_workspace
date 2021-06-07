import array
import pathlib

import numpy as np
import pandas as pd
import ROOT

df_dir = pathlib.Path(
    "/data/zprime/data_frames_fit/21-0120-sys-best-limit/high_mass_fixed_m_truth"
)
ntup_dir = pathlib.Path(
    "/data/zprime/ntuples_fit/21-0120-sys-best-limit/high_mass_fixed_m_truth"
)
ntup_dir.mkdir(parents=True, exist_ok=True)

bkg_samples = ["bkg_qcd", "bkg_ggZZ"]

branch_list = ["mz1", "mz2", "dnn_out_sig", "weight"]
ntup_name = "nominal"

for mass in [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]:
    sig_sample = f"sig_Zp{mass:03d}"
    df_dir_m = df_dir / f"m_{mass:02d}"
    ntup_dir_m = ntup_dir / f"m_{mass:02d}"
    ntup_dir_m.mkdir(parents=True, exist_ok=True)
    print(f"Generating fit ntuples for mass: {mass}")
    for sample in bkg_samples + [sig_sample]:
        # sig
        df_path = df_dir_m / f"{sample}.feather"
        df: pd.DataFrame = pd.read_feather(df_path)
        # prepare ntuple file
        ntup_path = ntup_dir_m / f"{sample}.root"
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
