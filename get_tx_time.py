import pickle
import csv
import pandas as pd
import subprocess
import json
import sys

# DEFINE PATHS

blockchain_data_path = '/home/oscar/jufobtc/data/test.csv'
dict_path = '/home/oscar/jufobtc/data/dict_mempool_tx.pkl'
diff_times_path = '/home/oscar/jufobtc/data/tx_times.csv'

cnt_added = 0


def loadDict(dict_path):
    with open(dict_path, 'rb') as dict_save:
        dict = pickle.load(dict_save)
        #print(dict)
        dict_save.close()
        return dict

def checkEnterTime(tx_hash, dict):
    timestamp = dict[tx_hash]
    return timestamp

def checkConfTime(tx_hash):
    answ = cliNode(['getrawtransaction', tx_hash, 'true'])
    answ = json.loads(answ)
    ret = answ["blocktime"].strip().decode("utf-8")
    
    return ret

def writeInFile(text, file):
    datei = open(file,'a',newline='')
    datei.writelines(str(text))
    datei.close   
    
def cliNode(command): 
    
    command.insert(0,"bitcoin-cli")
    answer = None 
    answer = subprocess.check_output(command)
    return answer

def checkTimeDiff(dict):
    i = 0
    cnt_added = 0
    cnt_not_added = 0
    with open(diff_times_path, "w") as csv_file:
        with open(blockchain_data_path, 'r') as blockchain_data:  
            for line in blockchain_data:
                temp = line.rstrip().strip('[]').split(' ')
                if len(temp) == 2:
                    block_height = temp[1]
                    timestamp_in_chain = temp[0]
                    continue
                #temp.append(block_height)
                if temp[0] in dict.keys():
                    timestamp = dict[temp[0]]
                    time_diff = int(timestamp_in_chain) - int(float(timestamp))
                    output = str(temp[0]) + ' ' +  str(time_diff) + ' ' +  str(block_height) + '\n'
                    csv_file.writelines(str(output))
                    cnt_added = cnt_added + 1
                    
                    
                else:
                    cnt_not_added = cnt_not_added + 1
                    
                    #print(temp)
                print("cnt added: ", cnt_added,"count not added:",  cnt_not_added, end="\r" ) 
                #print("count not added:",  cnt_not_added)
                #sys.stdout.flush()
                
dict = loadDict(dict_path)
#print(dict)
#print('loaded')
print(len(dict.keys()))
#print(dict.keys())
checkTimeDiff(dict)

print(cnt_added)
#print(dict.keys())
#print('done')
