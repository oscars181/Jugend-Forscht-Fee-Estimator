import pickle
import csv
import pandas as pd

def loadDict(dict_path):
    with open(dict_path, 'rb') as dict_save:
        dict = pickle.load(dict_save)
        #print(dict)
        dict_save.close()
        return dict

def checkEnterTime(tx_hash, dict):
    timestamp = dict[tx_hash]
    return timestamp
    

def checkTimeDiff(dict):
    i = 0
    with open('/home/oscar/jufobtc/iter_start_650000.csv', 'r') as iter_data:  
        for line in iter_data:
            if i == 10000: break #zum testen
            temp = line.rstrip().strip('[]').split(' ')
            tx_hash = temp[0]
            try: 
                enter_time = checkEnterTime(tx_hash, dict)
            except:
                #print(i)
                #i = i + 1
                #print(tx_hash, temp[2])
                continue
            else:
                i = i +1
                conf_time = temp[1]
                dif_time = int(conf_time) - (int(enter_time)/1000)
                print(tx_hash, dif_time, temp[2])
                #print('entertime: ', (enter_time/1000), 'conf_time = ',conf_time, '\n')

def start():
    dict = loadDict('/home/oscar/jufobtc/dict_mempool_start_650000.pkl')
    #print('loaded')
    #print(dict)
    checkTimeDiff(dict)
    #print('done')

start()
    