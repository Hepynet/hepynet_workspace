import subprocess

job_list = [
    "share/zxll/ee/train_pnn.yaml",
    "share/zxll/ee/train_pnn_hmumu.yaml",
    "share/zxll/mm/train_pnn.yaml",
    "share/zxll/mm/train_pnn_hmumu.yaml",
]

for job_config in job_list:
    subprocess.run(["hepynet", "-t", job_config])
