#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:26:11 2021

@author: jacobnogas
"""
import pandas as pd

EXPERIMENT_ID_DICT = {"Additional Problem": 171, "Text Box": 170}

ALG_DICT = {"TS": 3, "TSPD": 14, "UR":1}


POLICY_PARAM_PATH = "../..//Data/Raw/public.engine_policyparameters/part-00000-66d80e42-3934-4715-b063-5007330d3751-c000.gz.parquet"


df=pd.read_parquet(POLICY_PARAM_PATH, engine='pyarrow')
# df=pd.read_parquet(POLICY_PARAM_PATH, engine='fastparquet')
experiment = "Additional Problem"

df_addprob = df[df["mooclet_id"] == EXPERIMENT_ID_DICT[experiment]]

alg_idx = ALG_DICT["TSPD"]

df_addprob_tspd = df_addprob[df_addprob["policy_id"] == alg_idx]

print(experiment, "-------")
for key in df_addprob_tspd["parameters"]:
    #print(key, df_addprob_tspd["parameters"][key])
    print(key)
    
experiment = "Text Box"

df_addprob = df[df["mooclet_id"] == EXPERIMENT_ID_DICT[experiment]]

alg_idx = ALG_DICT["TSPD"]

df_addprob_tspd = df_addprob[df_addprob["policy_id"] == alg_idx]

print(experiment, "-------")
for key in df_addprob_tspd["parameters"]:
    #print(key, df_addprob_tspd["parameters"][key])
    print(key)