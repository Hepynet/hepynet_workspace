feature_list_in_emu = [
    "Electron_Pt",
    "Electron_Eta",
    "Electron_Phi",
    "Electron_E",
    "Electron_Charge",
    "Muon_Pt",
    "Muon_Eta",
    "Muon_Phi",
    "Muon_E",
    "Muon_Charge",
    "MET_Et",
    "MET_Phi",
    "DeltaPhi_ll",
    "DeltaPhi_DilMET",
    "RecoDilRapidity",
    "RecoDilPhi",
    "RecoDilMass",
    "RecoDilPt",
    "RecoWeight",
]

feature_list_out_emu = [
    "ele_pt",
    "ele_eta",
    "ele_phi",
    "ele_e",
    "ele_c",
    "mu_pt",
    "mu_eta",
    "mu_phi",
    "mu_e",
    "mu_c",
    "met_et",
    "met_phi",
    "ll_dphi",
    "ll_met_dphi",
    "ll_y",
    "ll_phi",
    "ll_m",
    "ll_pt",
    "weight",
]

bkg_dict = {
    "bkg_diboson": "output_nominal_Diboson_nomWeight",
    "bkg_top": "output_nominal_TopQuark_nomWeight",
    "bkg_wjets": "output_nominal_Wjets_nomWeight",
    "bkg_zll": "output_nominal_Ztoll_nomWeight",
}

sig_dict_emu = {
    # QBH n1
    "sig_qbh_n1_200": "output_nominal_QBH_n1_emu200_nomWeight",
    "sig_qbh_n1_250": "output_nominal_QBH_n1_emu250_nomWeight",
    "sig_qbh_n1_300": "output_nominal_QBH_n1_emu300_nomWeight",
    "sig_qbh_n1_350": "output_nominal_QBH_n1_emu350_nomWeight",
    "sig_qbh_n1_400": "output_nominal_QBH_n1_emu400_nomWeight",
    "sig_qbh_n1_450": "output_nominal_QBH_n1_emu450_nomWeight",
    "sig_qbh_n1_500": "output_nominal_QBH_n1_emu500_nomWeight",
    "sig_qbh_n1_550": "output_nominal_QBH_n1_emu550_nomWeight",
    "sig_qbh_n1_600": "output_nominal_QBH_n1_emu600_nomWeight",
    "sig_qbh_n1_650": "output_nominal_QBH_n1_emu650_nomWeight",
    "sig_qbh_n1_700": "output_nominal_QBH_n1_emu700_nomWeight",
    # QBH n2
    "sig_qbh_n2_400": "output_nominal_QBH_n6_emu400_nomWeight",
    "sig_qbh_n2_450": "output_nominal_QBH_n6_emu450_nomWeight",
    "sig_qbh_n2_500": "output_nominal_QBH_n6_emu500_nomWeight",
    "sig_qbh_n2_550": "output_nominal_QBH_n6_emu550_nomWeight",
    "sig_qbh_n2_600": "output_nominal_QBH_n6_emu600_nomWeight",
    "sig_qbh_n2_650": "output_nominal_QBH_n6_emu650_nomWeight",
    "sig_qbh_n2_700": "output_nominal_QBH_n6_emu700_nomWeight",
    "sig_qbh_n2_750": "output_nominal_QBH_n6_emu750_nomWeight",
    "sig_qbh_n2_800": "output_nominal_QBH_n6_emu800_nomWeight",
    "sig_qbh_n2_850": "output_nominal_QBH_n6_emu850_nomWeight",
    "sig_qbh_n2_900": "output_nominal_QBH_n6_emu900_nomWeight",
    # SVT
    "sig_svt_500": "output_nominal_SVT_emu500_nomWeight",
    "sig_svt_700": "output_nominal_SVT_emu700_nomWeight",
    "sig_svt_1000": "output_nominal_SVT_emu1000_nomWeight",
    "sig_svt_1500": "output_nominal_SVT_emu1500_nomWeight",
    "sig_svt_2000": "output_nominal_SVT_emu2000_nomWeight",
    "sig_svt_2500": "output_nominal_SVT_emu2500_nomWeight",
    "sig_svt_3000": "output_nominal_SVT_emu3000_nomWeight",
    "sig_svt_3500": "output_nominal_SVT_emu3500_nomWeight",
    "sig_svt_4000": "output_nominal_SVT_emu4000_nomWeight",
    "sig_svt_4500": "output_nominal_SVT_emu4500_nomWeight",
    "sig_svt_5000": "output_nominal_SVT_emu5000_nomWeight",
    "sig_svt_5500": "output_nominal_SVT_emu5500_nomWeight",
    "sig_svt_6000": "output_nominal_SVT_emu6000_nomWeight",
    "sig_svt_6500": "output_nominal_SVT_emu6500_nomWeight",
    "sig_svt_7000": "output_nominal_SVT_emu7000_nomWeight",
    "sig_svt_7500": "output_nominal_SVT_emu7500_nomWeight",
    "sig_svt_8000": "output_nominal_SVT_emu8000_nomWeight",
    # Zprime
    "sig_zp_500": "output_nominal_Zprime_emu500_nomWeight",
    "sig_zp_700": "output_nominal_Zprime_emu700_nomWeight",
    "sig_zp_1000": "output_nominal_Zprime_emu1000_nomWeight",
    "sig_zp_1500": "output_nominal_Zprime_emu1500_nomWeight",
    "sig_zp_2000": "output_nominal_Zprime_emu2000_nomWeight",
    "sig_zp_2500": "output_nominal_Zprime_emu2500_nomWeight",
    "sig_zp_3000": "output_nominal_Zprime_emu3000_nomWeight",
    "sig_zp_3500": "output_nominal_Zprime_emu3500_nomWeight",
    "sig_zp_4000": "output_nominal_Zprime_emu4000_nomWeight",
    "sig_zp_4500": "output_nominal_Zprime_emu4500_nomWeight",
    "sig_zp_5000": "output_nominal_Zprime_emu5000_nomWeight",
    "sig_zp_5500": "output_nominal_Zprime_emu5500_nomWeight",
    "sig_zp_6000": "output_nominal_Zprime_emu6000_nomWeight",
    "sig_zp_6500": "output_nominal_Zprime_emu6500_nomWeight",
    "sig_zp_7000": "output_nominal_Zprime_emu7000_nomWeight",
    "sig_zp_7500": "output_nominal_Zprime_emu7500_nomWeight",
    "sig_zp_8000": "output_nominal_Zprime_emu8000_nomWeight",
}

m_truth_dict = {
    # QBH n1
    "sig_qbh_n1_200": 200,
    "sig_qbh_n1_250": 250,
    "sig_qbh_n1_300": 300,
    "sig_qbh_n1_350": 350,
    "sig_qbh_n1_400": 400,
    "sig_qbh_n1_450": 450,
    "sig_qbh_n1_500": 500,
    "sig_qbh_n1_550": 550,
    "sig_qbh_n1_600": 600,
    "sig_qbh_n1_650": 650,
    "sig_qbh_n1_700": 700,
    # QBH n2
    "sig_qbh_n2_400": 400,
    "sig_qbh_n2_450": 450,
    "sig_qbh_n2_500": 500,
    "sig_qbh_n2_550": 550,
    "sig_qbh_n2_600": 600,
    "sig_qbh_n2_650": 650,
    "sig_qbh_n2_700": 700,
    "sig_qbh_n2_750": 750,
    "sig_qbh_n2_800": 800,
    "sig_qbh_n2_850": 850,
    "sig_qbh_n2_900": 900,
    # SVT
    "sig_svt_500": 500,
    "sig_svt_700": 700,
    "sig_svt_1000": 1000,
    "sig_svt_1500": 1500,
    "sig_svt_2000": 2000,
    "sig_svt_2500": 2500,
    "sig_svt_3000": 3000,
    "sig_svt_3500": 3500,
    "sig_svt_4000": 4000,
    "sig_svt_4500": 4500,
    "sig_svt_5000": 5000,
    "sig_svt_5500": 5500,
    "sig_svt_6000": 6000,
    "sig_svt_6500": 6500,
    "sig_svt_7000": 7000,
    "sig_svt_7500": 7500,
    "sig_svt_8000": 8000,
    # Zprime
    "sig_zp_500": 500,
    "sig_zp_700": 700,
    "sig_zp_1000": 1000,
    "sig_zp_1500": 1500,
    "sig_zp_2000": 2000,
    "sig_zp_2500": 2500,
    "sig_zp_3000": 3000,
    "sig_zp_3500": 3500,
    "sig_zp_4000": 4000,
    "sig_zp_4500": 4500,
    "sig_zp_5000": 5000,
    "sig_zp_5500": 5500,
    "sig_zp_6000": 6000,
    "sig_zp_6500": 6500,
    "sig_zp_7000": 7000,
    "sig_zp_7500": 7500,
    "sig_zp_8000": 8000,
}


# "output_nominal_QBH_n1_emu200_nomWeight"
# "output_nominal_QBH_n1_emu250_nomWeight"
# "output_nominal_QBH_n1_emu300_nomWeight"
# "output_nominal_QBH_n1_emu350_nomWeight"
# "output_nominal_QBH_n1_emu400_nomWeight"
# "output_nominal_QBH_n1_emu450_nomWeight"
# "output_nominal_QBH_n1_emu500_nomWeight"
# "output_nominal_QBH_n1_emu550_nomWeight"
# "output_nominal_QBH_n1_emu600_nomWeight"
# "output_nominal_QBH_n1_emu650_nomWeight"
# "output_nominal_QBH_n1_emu700_nomWeight"
# "output_nominal_QBH_n1_etau200_nomWeight"
# "output_nominal_QBH_n1_etau250_nomWeight"
# "output_nominal_QBH_n1_etau300_nomWeight"
# "output_nominal_QBH_n1_etau350_nomWeight"
# "output_nominal_QBH_n1_etau400_nomWeight"
# "output_nominal_QBH_n1_etau450_nomWeight"
# "output_nominal_QBH_n1_etau500_nomWeight"
# "output_nominal_QBH_n1_etau550_nomWeight"
# "output_nominal_QBH_n1_etau600_nomWeight"
# "output_nominal_QBH_n1_etau650_nomWeight"
# "output_nominal_QBH_n1_etau700_nomWeight"
# "output_nominal_QBH_n1_mutau200_nomWeight"
# "output_nominal_QBH_n1_mutau250_nomWeight"
# "output_nominal_QBH_n1_mutau300_nomWeight"
# "output_nominal_QBH_n1_mutau350_nomWeight"
# "output_nominal_QBH_n1_mutau400_nomWeight"
# "output_nominal_QBH_n1_mutau450_nomWeight"
# "output_nominal_QBH_n1_mutau500_nomWeight"
# "output_nominal_QBH_n1_mutau550_nomWeight"
# "output_nominal_QBH_n1_mutau600_nomWeight"
# "output_nominal_QBH_n1_mutau650_nomWeight"
# "output_nominal_QBH_n1_mutau700_nomWeight"
# "output_nominal_QBH_n6_emu400_nomWeight"
# "output_nominal_QBH_n6_emu450_nomWeight"
# "output_nominal_QBH_n6_emu500_nomWeight"
# "output_nominal_QBH_n6_emu550_nomWeight"
# "output_nominal_QBH_n6_emu600_nomWeight"
# "output_nominal_QBH_n6_emu650_nomWeight"
# "output_nominal_QBH_n6_emu700_nomWeight"
# "output_nominal_QBH_n6_emu750_nomWeight"
# "output_nominal_QBH_n6_emu800_nomWeight"
# "output_nominal_QBH_n6_emu850_nomWeight"
# "output_nominal_QBH_n6_emu900_nomWeight"
# "output_nominal_QBH_n6_etau400_nomWeight"
# "output_nominal_QBH_n6_etau450_nomWeight"
# "output_nominal_QBH_n6_etau500_nomWeight"
# "output_nominal_QBH_n6_etau550_nomWeight"
# "output_nominal_QBH_n6_etau600_nomWeight"
# "output_nominal_QBH_n6_etau650_nomWeight"
# "output_nominal_QBH_n6_etau700_nomWeight"
# "output_nominal_QBH_n6_etau750_nomWeight"
# "output_nominal_QBH_n6_etau800_nomWeight"
# "output_nominal_QBH_n6_etau850_nomWeight"
# "output_nominal_QBH_n6_etau900_nomWeight"
# "output_nominal_QBH_n6_mutau400_nomWeight"
# "output_nominal_QBH_n6_mutau450_nomWeight"
# "output_nominal_QBH_n6_mutau500_nomWeight"
# "output_nominal_QBH_n6_mutau550_nomWeight"
# "output_nominal_QBH_n6_mutau600_nomWeight"
# "output_nominal_QBH_n6_mutau650_nomWeight"
# "output_nominal_QBH_n6_mutau700_nomWeight"
# "output_nominal_QBH_n6_mutau750_nomWeight"
# "output_nominal_QBH_n6_mutau800_nomWeight"
# "output_nominal_QBH_n6_mutau850_nomWeight"
# "output_nominal_QBH_n6_mutau900_nomWeight"
# "output_nominal_SVT_emu1000_nomWeight"
# "output_nominal_SVT_emu1500_nomWeight"
# "output_nominal_SVT_emu2000_nomWeight"
# "output_nominal_SVT_emu2500_nomWeight"
# "output_nominal_SVT_emu3000_nomWeight"
# "output_nominal_SVT_emu3500_nomWeight"
# "output_nominal_SVT_emu4000_nomWeight"
# "output_nominal_SVT_emu4500_nomWeight"
# "output_nominal_SVT_emu500_nomWeight"
# "output_nominal_SVT_emu5000_nomWeight"
# "output_nominal_SVT_emu5500_nomWeight"
# "output_nominal_SVT_emu6000_nomWeight"
# "output_nominal_SVT_emu6500_nomWeight"
# "output_nominal_SVT_emu700_nomWeight"
# "output_nominal_SVT_emu7000_nomWeight"
# "output_nominal_SVT_emu7500_nomWeight"
# "output_nominal_SVT_emu8000_nomWeight"
# "output_nominal_SVT_etau1000_nomWeight"
# "output_nominal_SVT_etau1500_nomWeight"
# "output_nominal_SVT_etau2000_nomWeight"
# "output_nominal_SVT_etau2500_nomWeight"
# "output_nominal_SVT_etau3000_nomWeight"
# "output_nominal_SVT_etau3500_nomWeight"
# "output_nominal_SVT_etau4000_nomWeight"
# "output_nominal_SVT_etau4500_nomWeight"
# "output_nominal_SVT_etau500_nomWeight"
# "output_nominal_SVT_etau5000_nomWeight"
# "output_nominal_SVT_etau5500_nomWeight"
# "output_nominal_SVT_etau6000_nomWeight"
# "output_nominal_SVT_etau6500_nomWeight"
# "output_nominal_SVT_etau700_nomWeight"
# "output_nominal_SVT_etau7000_nomWeight"
# "output_nominal_SVT_etau7500_nomWeight"
# "output_nominal_SVT_etau8000_nomWeight"
# "output_nominal_SVT_mutau1000_nomWeight"
# "output_nominal_SVT_mutau1500_nomWeight"
# "output_nominal_SVT_mutau2000_nomWeight"
# "output_nominal_SVT_mutau2500_nomWeight"
# "output_nominal_SVT_mutau3000_nomWeight"
# "output_nominal_SVT_mutau3500_nomWeight"
# "output_nominal_SVT_mutau4000_nomWeight"
# "output_nominal_SVT_mutau4500_nomWeight"
# "output_nominal_SVT_mutau500_nomWeight"
# "output_nominal_SVT_mutau5000_nomWeight"
# "output_nominal_SVT_mutau5500_nomWeight"
# "output_nominal_SVT_mutau6000_nomWeight"
# "output_nominal_SVT_mutau6500_nomWeight"
# "output_nominal_SVT_mutau700_nomWeight"
# "output_nominal_SVT_mutau7000_nomWeight"
# "output_nominal_SVT_mutau7500_nomWeight"
# "output_nominal_SVT_mutau8000_nomWeight"
# "output_nominal_Zprime_emu1000_nomWeight"
# "output_nominal_Zprime_emu1500_nomWeight"
# "output_nominal_Zprime_emu2000_nomWeight"
# "output_nominal_Zprime_emu2500_nomWeight"
# "output_nominal_Zprime_emu3000_nomWeight"
# "output_nominal_Zprime_emu3500_nomWeight"
# "output_nominal_Zprime_emu4000_nomWeight"
# "output_nominal_Zprime_emu4500_nomWeight"
# "output_nominal_Zprime_emu500_nomWeight"
# "output_nominal_Zprime_emu5000_nomWeight"
# "output_nominal_Zprime_emu5500_nomWeight"
# "output_nominal_Zprime_emu6000_nomWeight"
# "output_nominal_Zprime_emu6500_nomWeight"
# "output_nominal_Zprime_emu700_nomWeight"
# "output_nominal_Zprime_emu7000_nomWeight"
# "output_nominal_Zprime_emu7500_nomWeight"
# "output_nominal_Zprime_emu8000_nomWeight"
# "output_nominal_Zprime_etau1000_nomWeight"
# "output_nominal_Zprime_etau1500_nomWeight"
# "output_nominal_Zprime_etau2000_nomWeight"
# "output_nominal_Zprime_etau2500_nomWeight"
# "output_nominal_Zprime_etau3000_nomWeight"
# "output_nominal_Zprime_etau3500_nomWeight"
# "output_nominal_Zprime_etau4000_nomWeight"
# "output_nominal_Zprime_etau4500_nomWeight"
# "output_nominal_Zprime_etau500_nomWeight"
# "output_nominal_Zprime_etau5000_nomWeight"
# "output_nominal_Zprime_etau5500_nomWeight"
# "output_nominal_Zprime_etau6000_nomWeight"
# "output_nominal_Zprime_etau6500_nomWeight"
# "output_nominal_Zprime_etau700_nomWeight"
# "output_nominal_Zprime_etau7000_nomWeight"
# "output_nominal_Zprime_etau7500_nomWeight"
# "output_nominal_Zprime_etau8000_nomWeight"
# "output_nominal_Zprime_mutau1000_nomWeight"
# "output_nominal_Zprime_mutau1500_nomWeight"
# "output_nominal_Zprime_mutau2000_nomWeight"
# "output_nominal_Zprime_mutau2500_nomWeight"
# "output_nominal_Zprime_mutau3000_nomWeight"
# "output_nominal_Zprime_mutau3500_nomWeight"
# "output_nominal_Zprime_mutau4000_nomWeight"
# "output_nominal_Zprime_mutau4500_nomWeight"
# "output_nominal_Zprime_mutau500_nomWeight"
# "output_nominal_Zprime_mutau5000_nomWeight"
# "output_nominal_Zprime_mutau5500_nomWeight"
# "output_nominal_Zprime_mutau6000_nomWeight"
# "output_nominal_Zprime_mutau6500_nomWeight"
# "output_nominal_Zprime_mutau700_nomWeight"
# "output_nominal_Zprime_mutau7000_nomWeight"
# "output_nominal_Zprime_mutau7500_nomWeight"
# "output_nominal_Zprime_mutau8000_nomWeight"
