import pathlib
import sys

import pandas as pd
import psutil
import uproot
import ROOT

MB = 1024 * 1024
GB = MB * 1024

# setups
test_ntup_path = "/eos/atlas/atlascerngroupdisk/phys-higgs/HSG1/MxAOD/h026/mc16a/Nominal/mc16a.MGH7_hh_bbyy_vbf_l0cvv1cv1.MxAODDetailedNoSkim.e7254_s3126_r9364_p4207_h026.root"
tree_name = "CollectionTree"

for block in uproot.iterate(
    f"{test_ntup_path}:{tree_name}",
    ["HGamEventInfoAuxDyn.m_yy"],
    library="pd",
    step_size=20,
):
    print(block)
    break

#in_file = ROOT.TFile.Open(test_ntup_path, "READ")
#tree = in_file.Get("CollectionTree")
#
#for entryNum in range (0 , tree . GetEntries ()):
#    m_yy = getattr(tree ,"HGamEventInfoAuxDyn.m_yy")
#    print("m_yy=", m_yy)
#    if entryNum == 10:
#        break
#