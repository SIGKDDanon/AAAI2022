#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 18:48:45 2021

@author: jacobnogas
"""
import pandas as pd
import numpy as np
import scipy.stats

UR_KEY = 1
TSPD_KEY = 14
TS_KEY = 3

DATA_PATH = "../../Data/Processed/data_inlist_completed_firstsub.csv"

EXPERIMENT_ID_DICT = {"Additional Problem": 171, "Text Box": 170}
ALG_DICT = {"TS": 3, "TSPD": 14, "UR":1}
EXP_FACTOR_DICT = {"Additional Problem": "problem", "Text Box": "big"}


def wald_test(mean1, mean2, n1, n2):
    se = np.sqrt(mean1*(1 - mean1)/n1 + mean2*(1 - mean2)/n2)
    test_stat = (mean1 - mean2)/se
    print("wald test stat =", np.round(test_stat, 3))
    
    wald_pval = (1 - scipy.stats.norm.cdf(np.abs(test_stat)))*2 
    
    print("wald pval =", np.round(wald_pval, 3))
    return "pval = {} \n test stat = {}".format(np.round(wald_pval, 3), np.round(test_stat, 3))


def hyp_test(df, experiment, alg):
    
    policy_id = EXPERIMENT_ID_DICT[experiment]
    
    #verify distribution of polcies is 50/50
    key = "policy_{}".format(policy_id)
    alg_key = ALG_DICT[alg]
    factor = EXP_FACTOR_DICT[experiment]
    print("\n {} With {} Experiment --------".format(alg, experiment))
    
    df_curr = df[df[key].isna() == False]
    
    df_curr_alg = df_curr[df_curr[key] == alg_key]
    
    mean1 = df_curr_alg[df_curr_alg[factor] == "yes"]["correct"].mean()
    mean2 = df_curr_alg[df_curr_alg[factor] == "no"]["correct"].mean() #looks like no effect, do wald test

    n1 = len(df_curr_alg[df_curr_alg[factor] == "yes"]["correct"])
    n2 = len(df_curr_alg[df_curr_alg[factor] == "no"]["correct"])
    
    print("mean1 =", np.round(mean1, 3), "\n mean2 =", \
          np.round(mean2, 3), "\n n1 =", n1, "\n n2 =", n2, "\n n1+n2 = ", n1+n2)
    #print(np.abs(mean1 - mean2))
   # print((mean1 + mean2)/2)
    ci1 = 1.96*np.sqrt(mean1*(1-mean1)/n1)
    ci2 = 1.96*np.sqrt(mean2*(1-mean2)/n2)

    print("ci 1", np.round(ci1, 3))
    print("ci 2", np.round(ci2, 3))
    return wald_test(mean1, mean2, n1, n2)

def get_perc_assignment(df, experiment):
    policy_id = EXPERIMENT_ID_DICT[experiment]
    
    #verify distribution of polcies is 50/50
    key = "policy_{}".format(policy_id)
    
    print("{} Experiment --------".format(experiment))
    print("percentage of people assigned with UR", (df[key] == UR_KEY).sum()/len(df))
    print("percentage of people assigned with TSPD" ,(df[key] == TSPD_KEY).sum()/len(df))
    print("percentage of people assigned with TSPD" ,(df[key] == TS_KEY).sum()/len(df))
    
    print("number of people assigned with UR", (df[key] == UR_KEY).sum())
    print("number of people assigned with TSPD" ,(df[key] == TSPD_KEY).sum())
    print("number of people assigned with TS" ,(df[key] == TS_KEY).sum())

if __name__ == "__main__":
    
    experiment = "Additional Problem"
    experiment = "Text Box"
    
    df = pd.read_csv(DATA_PATH)
    
    get_perc_assignment(df, experiment)
    
    #Check the final split of UR vs TS for TSPD

    # print("number of TSPD assignments with TS: ", (df_171_tspd["selection_method_171"] == 'thompson_sampling').sum())
    # print("number of TSPD assignments with UR: ", (df_171_tspd["selection_method_171"] == 'uniform_random').sum())
    # print("TS to UR ratio:", (df_171_tspd["selection_method_171"] == 'thompson_sampling').sum()/(df_171_tspd["selection_method_171"] == 'uniform_random').sum())
    
    if experiment == "Additional Problem":
        hyp_test(df, experiment, alg = "TS")
    hyp_test(df, experiment, alg = "TSPD")
    hyp_test(df, experiment, alg = "UR")
    # hyp_test(df_171_ts)
    # hyp_test(df_171_ur)

    
    
    
    
    