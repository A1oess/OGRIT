import pandas as pd

path1 = "../scenarios/data/ind/08_tracks.csv"
path2 = "../new_data/01_tracks.csv"

df = pd.read_csv(path1)
selected_rows = pd.DataFrame()
for i, row in df.iterrows():
    if i % 25 == 0:
        selected_rows = selected_rows.append(row)
    if i > 25*25:
        break

selected_rows.to_csv(path2, mode = 'a',header = False, index = False)
