

temp = '''config:
    include:
        - "share/zprime/high_mass/train.yaml"

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

apply:
    plot_atlas_label: True
    atlas_label:
        status: "wip"
        simulation: "true"
        energy: "13 TeV"
        lumi: 139

    book_train_test_compare: true
    cfg_train_test_compare:
        plot_title: "train/test MVA scores compare"
        bins: 25
        range: [0, 1]
        density: true
        log: true
        save_format: "png"

    book_significance_scan: true
    cfg_significance_scan:
        significance_algo: "s_sqrt_b_rel"
'''

for mass in [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]:
    sigma5 = 5 * (-0.0202966 + 0.0190822 * mass)
    with open(f"apply_{mass:02d}.yaml", "w+") as file:
        file.write(
            temp.format(p_mass=mass, p_mass_min=mass - sigma5, p_mass_max=mass + sigma5)
        )

