# still use 5 sigma for performance checking as it's more stable due to higher 
# statistics compared with 2 sigma

config_template = """
config:
    include:
        - "share/zprime/master/eb-0712-low-mass-with-m4mu-cut/train.yaml"
        - "share/zprime/apply/apply_lm_single.sec.yaml"

job:
    job_name: "apply_{p_mass:02d}"
    job_type: "apply"
    train_job_name: "train_m4mu_cut"

input:
    # only remove negative events for training
    negative_weight_process: "keep"
    reset_feature: false
    cut_expression: "mz2 > {m_cut_low} & mz2 < {m_cut_high}"
    sig_list:
        - "sig_Zp{p_mass:03d}"

apply:
    book_importance_study: true
"""

low_mass_points = [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]


def get_mass_cut(mass):
    sigma_range = 5.0 * (-0.0202966 + 0.0190822 * mass)
    return (mass - sigma_range, mass + sigma_range)


for mass in low_mass_points:
    m_cut_low, m_cut_high = get_mass_cut(mass)
    config = config_template.format(
        p_mass=mass, m_cut_low=m_cut_low, m_cut_high=m_cut_high
    )
    file_name = f"apply_on_{mass:02d}.yaml"
    with open(file_name, "w") as file:
        file.write(config)
