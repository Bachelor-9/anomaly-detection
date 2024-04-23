import os
import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')



def open_dataset_at_date(f: dict) -> pd.DataFrame:
    """Opens a dataset file from a given ship and date and returns a Pandas DataFrame with time as index.

    Parameters
    ----------
        f: A dictionary containing the vessel ID and the date of the dataset to open. The dict should be on the following format:
        >>> f = {
                'ship': '13218',
                'year': '2023',
                'month': '9',
                'day': '4'
            }
       
    Returns
    ----------
        >>> pandas.DataFrame

    """
    path = f'drive/MyDrive/dataset/{f["ship"]}.parquet/year={f["year"]}/month={f["month"]}/day={f["day"]}.parquet'

    df = pd.read_parquet(path)
    df = df.sort_values(by = 'time')
    df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df = df.set_index(pd.DatetimeIndex(df['time']))
    df = df.drop('time', axis=1)
    df = df.drop('timestamp', axis=1)

    return df



def open_dataset_at_month(f: dict) -> pd.DataFrame:
    """Opens a dataset file from a given ship at a given year and month and returns a Pandas DataFrame with time as index.

    Parameters
    ----------
        f: A dictionary containing the vessel ID and the year and month of the dataset to open. The dict should be on the following format:
        >>> f = {
                'ship': '13218',
                'year': '2023',
                'month': '9'
            }
       
    Returns
    ----------
        >>> pandas.DataFrame

    """
    path = f'drive/MyDrive/dataset/{f["ship"]}.parquet/year={f["year"]}/month={f["month"]}/'

    all_files = [os.path.join(path, file) for file in os.listdir(path) if file.endswith('.parquet')]

    df = pd.DataFrame()

    for file in all_files:
        daily_data = pd.read_parquet(file)
        df = pd.concat([df, daily_data])

    df = df.sort_values(by = 'time')
    df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df = df.set_index(pd.DatetimeIndex(df['time']))
    df = df.drop('time', axis=1)
    df = df.drop('timestamp', axis=1)

    return df



def produce_modified_dataset(df: pd.DataFrame, x_attr: list, y_attr: list) -> tuple:
    """Produces a modified version of the dataset where:
    * Attributes with constant values are removed.
    * Attributes containing non-numeric values are removed.
    * Attributes attributes not present in neither ```x_attr``` and ```y_attr``` are removed.

    Parameters
    ----------
        df: The ```pandas.DataFrame```to modify.
        x_attr: List of x attributes to preserve if present in the dataset and not constant.
        y_attr: List of y attributes to preserve if present in the dataset and not constant.
        controlled_parameters: List of all attributes which exists in the dataset and also is numerical.
       
    Returns
    ----------
        Tuple with the modified ```pandas.DataFrame``` and the x and cylinder lists with constant attributes removed.
        >>> (pd.DataFrame, x_attr, y_attr)

    """
    for column in df.columns:
        if len(set(df[column].values)) == 1:
            if any(element == column for element in x_attr):
                x_attr.remove(column)
            if any(element == column for element in y_attr):
                y_attr.remove(column)

    numeric_columns = df.select_dtypes(include=[np.number])
    controlled_parameters = list(set(x_attr) & set(numeric_columns.columns.tolist()))
    controlled_parameters.sort()
    columns = controlled_parameters + y_attr

    return df[columns], x_attr, y_attr, controlled_parameters



def remove_rows_at(df: pd.DataFrame, constraint: str) -> pd.DataFrame:
    """Remove rows in the dataset which meets a given condition.

    Parameters
    ----------
        df: The ```pandas.DataFrame``` object. 

        constraint: String containing a logical expression as e.g.:
        >>> constraint = "df['21EL'] > 250"

    Returns
    ----------
        >>> pandas.DataFrame

    """
    return df[eval(constraint)]
