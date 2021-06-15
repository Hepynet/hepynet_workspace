config_temp = """config:
    include:
        - "share/zprime/master/study_check_train_without_1_point/low_mass/train_no_19.yaml"
        - "share/zprime/apply/apply_lm_single.sec.yaml"

job:
    job_name: "apply_{p_mass:02d}"
    job_type: "apply"
    train_job_name: "train_no_19"

input:
    # only remove negative events for training
    negative_weight_process: "keep"
    reset_feature: false
    cut_expression: "mz2 > {p_mass_min} and mz2 < {p_mass_max}"
    sig_list:
        - "sig_Zp{p_mass:03d}"

"""

for mass in [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]:
    sigma5 = 5 * (-0.0202966 + 0.0190822 * mass)

    with open(f"apply_no_19_on_{mass:02d}.yaml", "w+") as file:
        file.write(
            config_temp.format(p_mass=mass, p_mass_min=mass - sigma5, p_mass_max=mass + sigma5)
        )
