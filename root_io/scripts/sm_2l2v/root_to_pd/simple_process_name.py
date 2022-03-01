import pandas as pd
from process_map import sample_map

# Path
in_df_path = "/net/s3_datae/yangz/sm_2l2v/data_frames/22-0213-mva/input.feather"
out_df_path = "/net/s3_datae/yangz/sm_2l2v/data_frames/22-0213-mva/input_simple.feather"

# Renaming
df:pd.DataFrame = pd.read_feather(in_df_path)
for name, sample_list in sample_map.items():
    df.loc[df["sample_name"].isin(sample_list), "sample_name"] = name

# DEBUG
# result = df.head()
# print(result)

# Save
df.to_feather(out_df_path)