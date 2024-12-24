import pandas as pd

for x in range(1,10):
    # Add nflId of 0 to the football so its easier to animate
    df = pd.read_csv(f"/Users/jsatchell/Documents/Projects/NFL-Big-Data-2025/data/tracking_week_{x}.csv")
    df.loc[df['displayName'] == 'football', 'nflId'] = 0
    df.to_csv(f"/Users/jsatchell/Documents/Projects/NFL-Big-Data-2025/data/tracking_week_{x}.csv", index=False)