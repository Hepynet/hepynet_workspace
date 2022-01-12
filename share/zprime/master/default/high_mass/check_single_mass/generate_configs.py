# still use 5 sigma for performance checking as it's more stable due to higher 
# statistics compared with 2 sigma

config_template = """
config:
    include:
        - "share/zprime/master/default/high_mass/train.yaml"
        - "share/zprime/apply/apply_hm_single.sec.yaml"

job:
    job_name: "apply_{p_mass:02d}"
    job_type: "apply"
    train_job_name: "default_train"

input:
    # only remove negative events for training
    negative_weight_process: "keep"
    reset_feature: false
    cut_expression: "mz1 > {m_cut_low} & mz1 < {m_cut_high}"
    sig_list:
        - "sig_Zp{p_mass:03d}"
"""

high_mass_points = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]


def get_mass_cut(mass):
    sigma_range = 3.0 * (0.193 - 0.002 * mass + 0.00035 * mass * mass) 
    return (mass - sigma_range, mass + sigma_range)


for mass in high_mass_points:
    m_cut_low, m_cut_high = get_mass_cut(mass)
    config = config_template.format(
        p_mass=mass, m_cut_low=m_cut_low, m_cut_high=m_cut_high
    )
    file_name = f"apply_on_{mass:02d}.yaml"
    with open(file_name, "w") as file:
        file.write(config)
