# Group the daily_sales DF using both 'date_id' and 'make_name' and return unique lead IDs and unique 
# partner IDs associated with it.

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads = ('lead_id', 'nunique'),
        unique_partners = ('partner_id', 'nunique')
    ).reset_index()
    return df