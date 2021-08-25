import requests
import pandas as pd

#Helper Functions

def unpack_json_from_api(end_point, key=None):
    """
    Transforms json data from api into a DataFrame
    """
    response = requests.get(end_point)
    json_data = response.json()
    if key is None:
        df = pd.DataFrame(json_data)
    else:
        df = pd.DataFrame(json_data[key])
    return json_data, df

def create_rolling_agg_features_by_golfer(df, field, n_shift, n_rolling, agg_func):
    """
    """
    df = df.copy()
    
    df['shifted_field'] = (df.groupby('dg_id')[field]
                           .shift(n_shift)
                           .fillna(0)
                          )
    
    return (df.groupby('dg_id')['shifted_field']
            .transform(lambda x: x.rolling(n_rolling, min_periods=1)
                       .agg(agg_func))
           )