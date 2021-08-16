#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:45:29 2021

@author: jacobnogas
#/Users/jacobnogas/anaconda3/envs
"""
import pandas as pd

DATA_PATH = "../../Data/Raw/PCRS_Week10_Prepare_Fall2020_posttest_April 20, 2021_10.01.csv"


def get_students_inlist_and_completed(df):
    
    df_inlist = df[df["isInList"] == 'true']
    df_inlist_completed = df_inlist[df_inlist["completed"] == 'true']
    
    return df_inlist_completed

def filter_by_min_startdate_peruser(df):
    
    unqiue_id_list = df["user_id"].unique()
    
    min_starts = df.groupby(['user_id']).min()["StartDate"]
    
    min_starts = pd.DataFrame(min_starts)
    
    df_m =pd.merge(left=df,\
                   right=min_starts, how="inner", \
                       on ="user_id", suffixes=("","_min"))
        
    df_m = df_m[df_m["StartDate"] == df_m["StartDate_min"]]
    
    return df_m


if __name__ == "__main__":
    
    df_raw = pd.read_csv(DATA_PATH)
    df_inlist_completed = get_students_inlist_and_completed(df_raw)  
    
    df_inlist_completed["StartDate"] = \
        pd.to_datetime(df_inlist_completed["StartDate"],\
                       infer_datetime_format=True)
            
    df_inlist_completed_firstsub = filter_by_min_startdate_peruser(df_inlist_completed)

    df_inlist_completed_firstsub.to_csv(
        "../../Data/Processed/data_inlist_completed_firstsub.csv"
        )