config_template = """
config:
    include:
        - "share/zprime/default_train/high_mass/apply_best.yaml"

job:
    job_name: "apply_{p_mass:02d}_fixed_m_truth"

input:
    reset_feature: true
    reset_feature_overwrite: True
    reset_feature_overwrite_value: {p_mass}
    cut_expression: "mz1 > {m_cut_low} & mz1 < {m_cut_high}"
    sig_list:
        - "sig_Zp{p_mass:03d}"

apply:
    book_history: false
    book_kine: false
    book_fit_inputs: false
    book_cut_kine_study: false
    book_importance_study: false
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
    file_name = f"apply_best_m{mass:02d}_fixed_m_truth.yaml"
    with open(file_name, "w") as file:
        file.write(config)