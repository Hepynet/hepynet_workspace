temp = """config:
    include:
        - "share/zprime/study-check-train-without-1-point/high_mass/train.yaml"
        - "share/zprime/study-check-train-without-1-point/high_mass/apply_single.yaml"

job:
    job_name: "apply-{p_mass}"
    job_type: "apply"
    load_job_name: "train-all-mass"

input:
    sig_key: "sig_Zp{p_mass:03d}"
    sig_list:
        - "sig_Zp{p_mass:03d}"
    # only remove negative events for training
    negative_weight_process: "keep"
    cut_expression: "mz1 > {p_mass_min} and mz1 < {p_mass_max}"

"""

temp2 = """config:
    include:
        - "share/zprime/study-check-train-without-1-point/high_mass/train.yaml"
        - "share/zprime/study-check-train-without-1-point/high_mass/apply_single.yaml"

job:
    job_name: "apply-{p_mass}"
    job_type: "apply"
    load_job_name: "train-no-63"

input:
    sig_key: "sig_Zp{p_mass:03d}"
    sig_list:
        - "sig_Zp{p_mass:03d}"
    # only remove negative events for training
    negative_weight_process: "keep"
    cut_expression: "mz1 > {p_mass_min} and mz1 < {p_mass_max}"

"""

for mass in [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]:
    sigma5 = 5 * (-0.0202966 + 0.0190822 * mass)
    with open(f"apply_{mass:02d}.yaml", "w+") as file:
        file.write(
            temp.format(p_mass=mass, p_mass_min=mass - sigma5, p_mass_max=mass + sigma5)
        )
    with open(f"apply_no_63_on_{mass:02d}.yaml", "w+") as file:
        file.write(
            temp2.format(
                p_mass=mass, p_mass_min=mass - sigma5, p_mass_max=mass + sigma5
            )
        )

