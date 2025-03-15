# Group the DF based on actor and director ID pairs and return the number of times they cooperated. Return
# the DF where the count is greater than or equal to 3.

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).agg(
        count = ('timestamp', 'count')
    ).reset_index()
    return df[df['count'] >= 3][['actor_id', 'director_id']]