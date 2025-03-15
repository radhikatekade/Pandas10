# Group the activities DF using 'sell_date'. agg() function is used because we want to apply multiple 
# functionality to the same grouping. Using agg() we get the total number of unique products sold and also
# get the names of all those unique products by joining a string of sorted set of product names. 
# Note: agg() function directly returns a DF, not a series like we get using transform()

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby(['sell_date']).agg(
        num_sold = ('product', 'nunique'), 
        products = ('product', lambda x: ','.join(sorted(set(x))))
        ).reset_index()
    return df