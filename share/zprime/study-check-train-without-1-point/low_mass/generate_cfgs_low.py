temp = """config:
    include:
        - "share/zprime/study-check-train-without-1-point/low_mass/train.yaml"
        - "share/zprime/study-check-train-without-1-point/low_mass/apply_single.yaml"

job:
    job_name: "apply-{p_mass}"
    job_type: "apply"
    load_job_name: "train-no-19"

input:
    sig_key: "sig_Zp{p_mass:03d}"
    sig_list:
        - "sig_Zp{p_mass:03d}"
    # only remove negative events for training
    negative_weight_process: "keep"
    cut_expression: "mz2 > {p_mass_min} and mz2 < {p_mass_max}"

"""

temp2 = """config:
    include:
        - "share/zprime/study-check-train-without-1-point/low_mass/train.yaml"
        - "share/zprime/study-check-train-without-1-point/low_mass/apply_single.yaml"

job:
    job_name: "apply-{p_mass}"
    job_type: "apply"
    load_job_name: "train-no-19"

input:
    sig_key: "sig_Zp{p_mass:03d}"
    sig_list:
        - "sig_Zp{p_mass:03d}"
    # only remove negative events for training
    negative_weight_process: "keep"
    cut_expression: "mz2 > {p_mass_min} and mz2 < {p_mass_max}"

"""

for mass in [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]:
    sigma5 = 5 * (-0.0202966 + 0.0190822 * mass)
    with open(f"apply_{mass:02d}.yaml", "w+") as file:
        file.write(
            temp.format(p_mass=mass, p_mass_min=mass - sigma5, p_mass_max=mass + sigma5)
        )
    with open(f"apply_no_19_on_{mass:02d}.yaml", "w+") as file:
        file.write(
            temp.format(p_mass=mass, p_mass_min=mass - sigma5, p_mass_max=mass + sigma5)
        )

