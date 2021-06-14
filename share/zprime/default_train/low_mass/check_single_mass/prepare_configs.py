config_template = """
config:
    include:
        - "share/zprime/default_train/low_mass/apply_best_limit.yaml"

job:
    job_name: "apply_{p_mass:02d}"

input:
    # only remove negative events for training
    negative_weight_process: "keep"
    reset_feature: false
    cut_expression: "mz2 > {m_cut_low} & mz2 < {m_cut_high}"
    sig_list:
        - "sig_Zp{p_mass:03d}"

apply:
    book_history: false
    book_kine: false
    book_fit_inputs: false
    book_cut_kine_study: false
    book_importance_study: false
"""

low_mass_points = [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]


def get_mass_cut(mass):
    sigma_range = 3.0 * (-0.0202966 + 0.0190822 * mass)
    return (mass - sigma_range, mass + sigma_range)


for mass in low_mass_points:
    m_cut_low, m_cut_high = get_mass_cut(mass)
    config = config_template.format(
        p_mass=mass, m_cut_low=m_cut_low, m_cut_high=m_cut_high
    )
    file_name = f"apply_best_limit_m{mass:02d}.yaml"
    with open(file_name, "w") as file:
        file.write(config)