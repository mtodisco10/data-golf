import requests
import pandas as pd

#Helper Functions

def unpack_json_from_api(end_point, key=None):
    """
    Transforms json data from api into a DataFrame

    Args:
    end_point (str): url of the api
    key (str, optional): drill-down into the json when necessary
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
    Returns a pandas series, which is an aggregation of previous activity over a
    specified period of time (n_rolling).

    Args:
    field (str): the field being used in the calculation
    n_shift (int): number of rows to shift the DataFrame
    n_rolling (int): number of periods for the window to look back
    agg_func (str): type of aggregation ie sum, mean, etc.
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

def create_map_to_aggregates(df, col_to_groupby, col_to_agg, agg):
	"""
	Returns a dictionary to be used to map data to a column in a dataframe

	Args:
		df (DataFrame): the DataFrame to aggregate from
		col_to_groupby (str): the field to group
		col_to_agg (str): the field to agggregate
		agg (str): type of aggregation ie sum, mean, etc.
	"""
	mapping_dict = df.groupby(col_to_groupby)[col_to_agg].agg(agg).to_dict()
	return mapping_dict