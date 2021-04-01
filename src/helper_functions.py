#############################################################
# Title: Grown Strong - March 2021 Survey Analysis
# Purpose: Data cleaning and manipulation helper functions
# Date: 2021-03-30
# Author: Edward Sims
#############################################################

import pandas as pd
import numpy as np


def extract_email_domain(string):
    """
    Helper function to extract domain name from 
    email address string values.
    """
    domain = string.split('@')[1].split('.')[0]
    return(domain)


def clean_free_text(data, col):
    ## Convert to lowercase
    data[col] = data[col].str.lower()
    ## Clean punctuation and abbreviations
    data[col] = data[col].str.replace("i’ll", 'i will', regex = False)
    data[col] = data[col].str.replace("i'll", 'i will', regex = False)
    data[col] = data[col].str.replace("i’m", 'i am', regex = False)
    data[col] = data[col].str.replace("i'm", 'i am', regex = False)
    data[col] = data[col].str.replace("i’ve", 'i have', regex = False)
    data[col] = data[col].str.replace("i've", 'i have', regex = False)
    data[col] = data[col].str.replace("it’s", 'it is', regex = False)
    data[col] = data[col].str.replace("it's", 'it is', regex = False)
    data[col] = data[col].str.replace("what’s", 'what is', regex = False)
    data[col] = data[col].str.replace("what's", 'what is', regex = False)
    data[col] = data[col].str.replace("can’t", 'can not', regex = False)
    data[col] = data[col].str.replace("can't", 'can not', regex = False)
    data[col] = data[col].str.replace("don’t", 'do not', regex = False)
    data[col] = data[col].str.replace("don't", 'do not', regex = False)
    data[col] = data[col].str.replace("didn’t", 'did not', regex = False)
    data[col] = data[col].str.replace("didn't", 'did not', regex = False)
    data[col] = data[col].str.replace("isn’t", 'is not', regex = False)
    data[col] = data[col].str.replace("isn't", 'is not', regex = False)
    data[col] = data[col].str.replace("wasn’t", 'was not', regex = False)
    data[col] = data[col].str.replace("wasn't", 'was not', regex = False)
    data[col] = data[col].str.replace("haven’t", 'have not', regex = False)
    data[col] = data[col].str.replace("haven't", 'have not', regex = False)
    data[col] = data[col].str.replace("shouldn’t", 'should not', regex = False)
    data[col] = data[col].str.replace("shouldn't", 'should not', regex = False)
    data[col] = data[col].str.replace("wouldn’t", 'would not', regex = False)
    data[col] = data[col].str.replace("wouldn't", 'would not', regex = False)
    data[col] = data[col].str.replace("couldn’t", 'could not', regex = False)
    data[col] = data[col].str.replace("couldn't", 'could not', regex = False)
    data[col] = data[col].str.replace("hitt", 'hiit', regex = False)
    data[col] = data[col].str.replace(r"\boly\b", 'olympic', regex = True)
    data[col] = data[col].str.replace(r"\bfb\b", 'facebook', regex = True)
    data[col] = data[col].str.replace(r"\bidk\b", 'i do not know', regex = True)
    data[col] = data[col].str.replace(" gs ", ' grownstrong ', regex = False)
    data[col] = data[col].str.replace("grown strong", 'grownstrong', regex = False)
    data[col] = data[col].str.replace(r'[^\w\s]+', ' ', regex = True)
    data[col] = data[col].str.replace(' s ', 's ', regex = False)
    ## Strip whitespace
    data[col] = data[col].str.replace('\n', ' ', regex = False)
    data[col] = data[col].str.replace('\s+', ' ', regex = True)
    data[col] = data[col].str.strip()
    data.loc[data[col] == '', col] = np.nan
    return(data[col])


def clean_fitness_cols(df, col_exclude, val_lookup, colname_new):
    """
    Rename fitness column names and convert column to boolean.
    """
    ## Get column containing val_lookup 
    col_lookup = df.drop(col_exclude, axis=1).columns[
        df.drop(col_exclude, axis=1).isin([val_lookup]).any()
    ].item()
    
    ## Rename above column to column_new
    df_return = df.rename(columns={col_lookup:colname_new})
    
    df_return.loc[df[col_lookup] == val_lookup, colname_new] = 1
    df_return.loc[df[col_lookup] != val_lookup, colname_new] = 0
    df_return[colname_new] = df_return[colname_new].astype('float')
    
    return df_return