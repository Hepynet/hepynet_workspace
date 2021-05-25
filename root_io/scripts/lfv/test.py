import pathlib

import awkward as ak
import pandas as pd
import ROOT
import uproot
from xsec import xsec_dict

MB = 1024 * 1024
GB = MB * 1024

ELECTRON_MASS = 0.0005109989461  # GeV
MUON_MASS = 0.10565837545  # GeV
TAU_MASS = 1.77682  # GeV

test_file = pathlib.Path("/data/lfv/test/test.root")
df_dir = pathlib.Path(f"/data/lfv/data_frames/test")
df_dir.mkdir(parents=True, exist_ok=True)

is_data = False
dsid = 364180  # fake dsid, for test
lumi = 58.450  # fake lumi, for test


# variables which have one value per event
plain_input_list = [
    "emuSelection",
    "etauSelection",
    "mutauSelection",
]
# variables which have unfixed length of values per event
ak_input_list = [
    "mu_pt",
    "mu_eta",
    "el_pt",
    "tau_pt",
]

input_list = plain_input_list + ak_input_list

sum_weights_tree = uproot.open(f"{test_file}:sumWeights")
sum_weights = sum_weights_tree["totalEventsWeighted"].array(library="np")[0]

"""
for chunk_pd in uproot.iterate(f"{test_file}:nominal", library="np", step_size=10,):
    print(type(chunk_pd))
    for pd_key in chunk_pd.keys():
        if "HLT" in pd_key or "trig" in pd_key:
            print(pd_key)
    exit()
"""


def select_electron(event):
    select_id = -1
    n_electrons = len(event.el_pt)
    n_select = 0
    for i in range(n_electrons):
        if event.el_pt[i] < 65000:
            continue
        if abs(event.el_delta_z0_sintheta[i]) > 0.5:
            continue
        if abs(event.el_d0sig[i]) > 5.0:
            continue
        if event.el_isElMedium[i] != 1:
            continue
        if not (event.el_isElTight[i] and event.el_isolation_FixedCutTight[i]):
            continue
        select_id = i
        n_select += 1
    if n_select > 1:
        select_id = -1
    return select_id


def select_muon(event):
    select_id = -1
    n_muons = len(event.mu_pt)
    n_select = 0
    for i in range(n_muons):
        if event.mu_pt[i] < 65000:
            continue
        if abs(event.mu_delta_z0_sintheta[i]) > 0.5:
            continue
        if abs(event.mu_d0sig[i]) > 3.0:
            continue
        if not event.mu_isolation_FixedCutLoose[i]:
            continue
        select_id = i
        n_select += 1
    if n_select > 1:
        select_id = -1
    return select_id


def select_tau(event):
    select_id = -1
    n_taus = len(event.tau_pt)
    n_select = 0
    for i in range(n_taus):
        if event.tau_pt[i] < 65000:
            continue
        if abs(event.tau_charge[i]) != 1:
            continue
        if event.tau_nTracks[i] != 1 and event.tau_nTracks[i] != 3:
            continue
        if event.tau_isRNNMedium[i] != 1:
            continue
        select_id = i
        n_select += 1
    if n_select > 1:
        select_id = -1
    return select_id


for i, chunk_ak in enumerate(
    uproot.iterate(
        f"{test_file}:nominal", expressions=None, library="ak", step_size=30,
    )
):
    # for index, row in chunk_pd.iterrows():
    #    print(row)
    # exit()
    # is_emu_list = list()
    # print(type(chunk_ak["emuSlection"]))
    # print(chunk_ak)
    # for line in chunk_ak:
    #    print(
    #        "emu",
    #        line["emuSelection"],
    #        "etau",
    #        line.etauSelection,
    #        "mutau",
    #        line.mutauSelection,
    #    )
    #    is_emu_list.append()

    # get norm factor
    if is_data:
        norm_factor = 1
    else:
        if dsid in xsec_dict:
            xsec = xsec_dict[dsid]
        else:
            print(f"Unknown DSID: {dsid} to retrieve cross-section")
            exit()

    chunk_dict = {
        "is_emu": list(),
        "is_etau": list(),
        "is_mutau": list(),
        "lep0_pt": list(),
        "lep0_eta": list(),
        "lep0_phi": list(),
        "lep0_e": list(),
        "lep0_c": list(),
        "lep1_pt": list(),
        "lep1_eta": list(),
        "lep1_phi": list(),
        "lep1_e": list(),
        "lep1_c": list(),
        "met": list(),
        "met_phi": list(),
        "ll_m": list(),
        "ll_pt": list(),
        "ll_y": list(),
        "ll_dr": list(),
        "ll_dphi": list(),
    }
    for ev in chunk_ak:
        # cut trigger
        if not (
            ev.HLT_mu26_ivarmedium
            or ev.HLT_mu50
            or ev.HLT_e60_lhmedium_nod0
            or ev.HLT_e140_lhloose_nod0
            or ev.HLT_e26_lhtight_nod0_ivarloose
            # or ev.HLT_e120_lhloose
            # or ev.HLT_mu20_iloose_L1MU15
            # or ev.HLT_e24_lhmedium_L1EM20VH
            # or ev.HLT_e60_lhmedium
        ):
            print("#### NOT pass cut")
            exit()
        if not (
            ak.any(ev.el_trigMatch_HLT_e60_lhmedium_nod0)
            # or ak.any(ev.el_trigMatch_HLT_e60_lhmedium)
            # or ak.any(ev.el_trigMatch_HLT_e24_lhmedium_L1EM20VH)
            # or ak.any(ev.el_trigMatch_HLT_e120_lhloose)
            or ak.any(ev.el_trigMatch_HLT_e26_lhtight_nod0_ivarloose)
            or ak.any(ev.el_trigMatch_HLT_e140_lhloose_nod0)
            or ak.any(ev.mu_trigMatch_HLT_mu50)
            # or ak.any(ev.mu_trigMatch_HLT_mu20_iloose_L1MU15)
            or ak.any(ev.mu_trigMatch_HLT_mu26_ivarmedium)
        ):
            print("#### NOT pass cut")
            exit()

        #

        is_emu = ev.emuSelection
        is_etau = ev.etauSelection
        is_mutau = ev.mutauSelection

        # get objects
        electron_id = select_electron(ev)
        muon_id = select_muon(ev)
        tau_id = select_tau(ev)

        lep0 = ROOT.TLorentzVector()
        lep1 = ROOT.TLorentzVector()
        met = ROOT.TLorentzVector()
        if electron_id >= 0 and muon_id >= 0 and tau_id < 0:
            is_emu = 1
            is_etau = 0
            is_mutau = 0
            lep0.SetPtEtaPhiM(
                ev.el_pt[electron_id] / 1000.0,
                ev.el_eta[electron_id],
                ev.el_phi[electron_id],
                ELECTRON_MASS,
            )
            lep0_c = ev.el_charge[electron_id]
            lep1.SetPtEtaPhiM(
                ev.mu_pt[muon_id] / 1000.0,
                ev.mu_eta[muon_id],
                ev.mu_phi[muon_id],
                MUON_MASS,
            )
            lep1_c = ev.mu_charge[muon_id]
            met.SetPtEtaPhiM(ev.met_met, 0, ev.met_phi, 0)
            ll = lep0 + lep1
        elif electron_id >= 0 and tau_id >= 0 and muon_id < 0:
            is_emu = 0
            is_etau = 1
            is_mutau = 0
            lep0.SetPtEtaPhiM(
                ev.el_pt[electron_id] / 1000.0,
                ev.el_eta[electron_id],
                ev.el_phi[electron_id],
                ELECTRON_MASS,
            )
            lep0_c = ev.el_charge[electron_id]
            lep1.SetPtEtaPhiM(
                ev.tau_pt[tau_id] / 1000.0,
                ev.tau_eta[tau_id],
                ev.tau_phi[tau_id],
                TAU_MASS,
            )
            lep1_c = ev.tau_charge[tau_id]
            met.SetPtEtaPhiM(ev.met_met, ev.tau_eta[tau_id], ev.met_phi, 0)
            ll = lep0 + lep1 + met
        elif muon_id >= 0 and tau_id >= 0 and electron_id < 0:
            is_emu = 0
            is_etau = 0
            is_mutau = 1
            lep0.SetPtEtaPhiM(
                ev.mu_pt[muon_id] / 1000.0,
                ev.mu_eta[muon_id],
                ev.mu_phi[muon_id],
                MUON_MASS,
            )
            lep0_c = ev.mu_charge[muon_id]
            lep1.SetPtEtaPhiM(
                ev.tau_pt[tau_id] / 1000.0,
                ev.tau_eta[tau_id],
                ev.tau_phi[tau_id],
                TAU_MASS,
            )
            lep1_c = ev.tau_charge[tau_id]
            met.SetPtEtaPhiM(ev.met_met, ev.tau_eta[tau_id], ev.met_phi, 0)
            ll = lep0 + lep1 + met
        else:
            print("#### not a valid channel")
            continue

        # calculate weight

        # append variables
        chunk_dict["is_emu"].append(is_emu)
        chunk_dict["is_etau"].append(is_etau)
        chunk_dict["is_mutau"].append(is_mutau)
        chunk_dict["lep0_pt"].append(lep0.Pt())
        chunk_dict["lep0_eta"].append(lep0.Eta())
        chunk_dict["lep0_phi"].append(lep0.Phi())
        chunk_dict["lep0_e"].append(lep0.E())
        chunk_dict["lep0_c"].append(lep0_c)
        chunk_dict["lep1_pt"].append(lep1.Pt())
        chunk_dict["lep1_eta"].append(lep1.Eta())
        chunk_dict["lep1_phi"].append(lep1.Phi())
        chunk_dict["lep1_e"].append(lep1.E())
        chunk_dict["lep1_c"].append(lep1_c)
        chunk_dict["met"].append(met.Pt())
        chunk_dict["met_phi"].append(met.Phi())
        chunk_dict["ll_m"].append(ll.M())
        chunk_dict["ll_pt"].append(ll.Pt())
        chunk_dict["ll_y"].append(ll.Rapidity())
        chunk_dict["ll_dr"].append(lep0.DeltaR(lep1))
        chunk_dict["ll_dphi"].append(lep0.DeltaPhi(lep1))

    chunk_pd = pd.DataFrame(chunk_dict)
    #print(chunk_pd)

    # exit()

