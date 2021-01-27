"""Extracts data from files into memory.

Author: Adam Turner <turner.adch@gmail.com>
Notes: Python 3.8, UTF-8, tab is 4 spaces
"""

# python package index
import pandas as pd


def dataframe_from_pdf(fpath):
    print("PDF is not handled yet!")
    df = pd.DataFrame()

    return df


def dataframe_from_xlsx(fpath):
    fname = fpath.split("/")[-1]
    print(f"`{fname}`: Extracting data...")

    df = pd.read_excel(fpath, engine="openpyxl")
    df.dropna(axis=1, how="all", inplace=True)
    df.dropna(axis=0, how="all", inplace=True)

    print(f"`{fname}`: Extracted data!")

    return df
