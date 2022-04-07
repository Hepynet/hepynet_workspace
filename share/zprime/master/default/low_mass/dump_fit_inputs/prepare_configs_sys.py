basic = """config:
    include:
        - "share/zprime/master/default/low_mass/train.yaml"

job:
    job_name: "dump_ntup_sys_{p_variation}"
    job_type: "apply"
    train_job_name: "default_train"

input:
    input_path: "zprime/data_frames/22-0120-sys/low_mass/{p_variation}/zprime_low_m_quadtype_2_unblind.feather"
    bkg_list:
        - "bkg_qcd"
        - "bkg_ggZZ"
        - "bkg_fakes_data"
        - "bkg_fakes_diboson"
        - "bkg_ttv"
        - "bkg_vvv"
        - "bkg_ttbar"
        - "bkg_zll"
    negative_weight_process: "keep"
    reset_feature: false

"""
apply = """
apply:
    book_fit_inputs: true
    fit_df:
        branches:
            - "mz1"
            - "mz2"
            - "mz1_mz2"
            - "ptz1"
            - "ptz2"
            - "mzz"
            - "ptzz"
        save_dir: "zprime/data_frames_fit/22-0120-sys/low_mass/{p_variation}"

"""
apply_nominal = """
apply:
    book_fit_inputs: true
    fit_df:
        branches:
            - "mz1"
            - "mz2"
            - "mz1_mz2"
            - "ptz1"
            - "ptz2"
            - "mzz"
            - "ptzz"
            - "weight_qcd_scale_up_mz1"
            - "weight_qcd_scale_down_mz1"
            - "weight_qcd_scale_up_mz2"
            - "weight_qcd_scale_down_mz2"
            - "weight_pdf_up_mz1"
            - "weight_pdf_up_mz2"
            - "weight_alpha_s_up_mz1"
            - "weight_alpha_s_up_mz2"
        save_dir: "zprime/data_frames_fit/22-0120-sys/low_mass/{p_variation}"

"""

temp = basic + apply
temp_nominal = basic + apply_nominal


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

for variation in variations:
    with open(f"sys_ntup_{variation}.yaml", "w+") as file:
        if variation == "tree_NOMINAL":
            file.write(temp_nominal.format(p_variation=variation))
        else:
            file.write(temp.format(p_variation=variation))
