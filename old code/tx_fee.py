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


current_block_height = 0 
temp_block_height = 0
fee_per_vbyte = 0
i = 0
block_sum_fees = 0
block_count = 0
#dict_mempool = open('/home/oscar/jufobtc/dict_mempool_start_600000.pkl', 'r')

#conf_time_csv = open('/home/oscar/jufobtc/code/test_comp_time.csv','r')
#colnames = ['time_stamp', 'dif_time','block_height']
#df_conf_time = pd.read_csv(conf_time_csv,delimiter=' ', names=colnames)
#print('df loaded')
dict = {}
iter_file = open('/home/oscar/jufobtc/iter_start_650000_660000_verb.csv','r')
dict_save = open('/home/oscar/jufobtc/dict_fee_block_65000.pkl', 'wb')

for line in iter_file:
    try:
        if block_count == 10000: break
        line.rstrip()
        tx_hash, tx_size, tx_total_fee = line.split(' ')    
    except:
        block_count += 1
        block_height = line.rstrip()
        continue
    else:
        tx_fee = int(tx_total_fee) / int(tx_size)
        #print(tx_hash, tx_fee)
        if tx_fee > 0:
            block_sum_fees = block_sum_fees + tx_fee
            dict[tx_hash] = int(tx_fee)
        else:
            tx_fee = 0
            dict[tx_hash] = 0

    print(tx_hash, tx_fee, block_height)
#print(dict)


