config_temp = """config:
    include:
        - "share/zprime/master/study_check_train_without_1_point/high_mass/train_no_63.yaml"
        - "share/zprime/apply/apply_hm_single.sec.yaml"

job:
    job_name: "apply_{p_mass}"
    job_type: "apply"
    train_job_name: "train_no_63"

input:
    # only remove negative events for training
    negative_weight_process: "keep"
    reset_feature: false
    cut_expression: "mz1 > {p_mass_min} & mz1 < {p_mass_max}"
    sig_list:
        - "sig_Zp{p_mass:03d}"

"""

for mass in [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]:
    sigma5 = 5 * (-0.0202966 + 0.0190822 * mass)

    with open(f"apply_no_63_on_{mass:02d}.yaml", "w+") as file:
        file.write(
            config_temp.format(
                p_mass=mass, p_mass_min=mass - sigma5, p_mass_max=mass + sigma5
            )
        )
