# Eigener Fee Estimator

import subprocess
import time
import json
import matplotlib.pyplot as plt 
import csv 
import pandas as pd
from datetime import datetime
import numpy as np
import seaborn as sns  
import pickle
from itertools import islice
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import vq
from scipy import stats
import sys



tx_dict = {}
tx_dict_path = "/home/oscar/jufobtc/data/dict_mempool_tx.pkl"

args = sys.argv



def main():
    global target
    global current_height
    global dict
    
    dict = loadDict()
    
    print("dict loaded")
    #target = input("what is the block target (1-6) ? ")
    
    #print(target, current_height)
    
    data = getLastPercentiles()
    
    df = pd.DataFrame(data, columns=["10_percentile","50_percentile","avg_fee","blockheight","timestamp"])
    
    df["blocktime"] = df["timestamp"].diff()
    df.drop(index=1)
    #print(df)
    
    median_latest_block = getLastMedian()
    cleaned_median_latest_block = median_latest_block - df["blocktime"].tail(1).item()
    
    print(median_latest_block, cleaned_median_latest_block)
    
    last_percentiles = df["50_percentile"].rolling(3).mean().tail(1).item()
    print(last_percentiles)
    
    if cleaned_median_latest_block > -127: 
        factor = 0.9
        trend = "fallend"
    else: 
        factor = 1.1
        trend = "steigend"
    
    fee_estimate = last_percentiles * factor
    
    print("fee estimate: ", fee_estimate, trend)
    
def getLastPercentiles():
    global current_height
    data_list = []
    for i in range(0,12):
        temp_data = []
        temp_block = int(current_height)-i
        temp_block_data = json.loads(cliNode(["getblockstats", str(temp_block)]))
        
        
        temp_data = [temp_block_data["feerate_percentiles"][0],temp_block_data["feerate_percentiles"][2], temp_block_data["avgfeerate"],temp_block_data["height"], temp_block_data["time"]]
        data_list.insert(0, temp_data)
        
        #print(temp_data)
    
    return data_list

def getLastMedian():
    global current_height
    hash = cliNode(["getblockhash", str(current_height)]).strip().decode('utf-8')
    #print(hash)
    data = json.loads(cliNode(["getblock", hash]))
    #print(data)
    
    cnt_in_dict = cnt_not_in_dict = 0
    times = []
    
    #print(data ["tx"])
    for tx in data["tx"]:
        try:
            time = dict[tx]
            
        except:
            cnt_not_in_dict = cnt_not_in_dict + 1
        else: 
            diff_time = int(data["time"]) - int(float(time))
            cnt_in_dict = cnt_in_dict + 1
            times.append(diff_time)
            
    print("cnt in:", cnt_in_dict, "cnt not:", cnt_not_in_dict)
    
    times.sort()
    
    #print(times)
    
    #print(times[int(len(times)/2)])
    
    return times[int(len(times)/2)]

def cliNode(command): 
    
    command.insert(0,"bitcoin-cli")
    answer = None 
    try: 
        answer = subprocess.check_output(command)
    except:
        dksajfhaskldjfh = 0 #pseudo line
    else:
        return answer


def updateDict():
    test = 0
    
def loadDict():
    global dict
    dict = pickle.load(open(tx_dict_path, 'rb'))
    return dict
    








if __name__ == "__main__":
    global current_height
    global target
    try:
        current_height = args[2]
        target = args[1]
    except:
        target = 1
        current_height = cliNode(["getblockcount"]).strip().decode('utf-8')
    else:
        x=0    
        
    print("Target:", target)
    print("Für Blockhöhe:", current_height)
        
    main()