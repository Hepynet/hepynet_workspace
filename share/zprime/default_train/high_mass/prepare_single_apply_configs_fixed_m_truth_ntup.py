config_template = """
config:
    include:
        - "share/zprime/default_train/high_mass/train_best.yaml"

job:
    job_name: "apply_{p_mass:02d}_fixed_m_truth"
    job_type: "apply"
    train_job_name: "train-all-mass-best"
    #rdm_seed: 111

input:
    # only remove negative events for training
    negative_weight_process: "keep"
    reset_feature: true
    reset_feature_overwrite: True
    reset_feature_overwrite_value: {p_mass}
    sig_list:
        - "sig_Zp{p_mass:03d}"

apply:
    book_fit_inputs: true
    fit_df:
        branches:
            - "mz1"
            - "mz2"
        save_dir: "zprime/data_frames_fit/21-0120-sys-best-hyper/high_mass_fixed_m_truth/m_{p_mass:02d}"
"""

high_mass_points = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]


def get_mass_cut(mass):
    sigma_range = 3.0 * (-0.0202966 + 0.0190822 * mass)
    return (mass - sigma_range, mass + sigma_range)


for mass in high_mass_points:
    m_cut_low, m_cut_high = get_mass_cut(mass)
    config = config_template.format(
        p_mass=mass, m_cut_low=m_cut_low, m_cut_high=m_cut_high
    )
    file_name = f"apply_best_m{mass:02d}_fixed_m_truth_ntup.yaml"
    with open(file_name, "w") as file:
        file.write(config)