import pickle
import csv
import os
import bz2
import json
from itertools import islice
import subprocess

pickle_path = '/home/oscar/jufobtc/data/dict_mempool_tx.pkl'
mem_data_path = '/home/oscar/jufobtc/data/mem_tx.csv'
line = []
dict = {}
i = 0
dict_state = 0
cnt_add = 0

def intit_dict():
    with open(pickle_path, 'wb') as dict_save:
        print('loaded pkl file')
        #print(dict)
        pickle.dump(dict, dict_save)

        dict_save.close()
        #print(dict)

def cliNode(command): 
    
    command.insert(0,"bitcoin-cli")
    answer = None 
    try: 
        answer = subprocess.check_output(command)
    except:
        print(str(command))
        print(answer)
    else:
        return answer
    
            
def save():
    print('loaded pkl file')
    #print(dict)
    pickle.dump(dict, dict_save)
    print('dumped', i)
    #dict_save.close()
    #print(dict)
    dict.clear()
    
                        
intit_dict()   
                        
with open(mem_data_path, 'rb') as file:
    with open(pickle_path, 'wb') as dict_save:
        
        #dict = pickle.load(open(pickle_path, 'rb'))
        print('dict loaded')
        for line in islice(file,0,None):
            #if i == 1000000000: break
            try: 
                line = line.strip().decode('utf-8')
                (tx_hash, time_stamp) = line.split()
            except:
                #print('not working: ', end='') 
                print(line)
                #print(i)
                i = i + 1
                continue
            else:
                #print(dict_state, i)
                #time_stamp = time_stamp.decode().strip('[b]')
                #print(tx_hash, time_stamp)
                if tx_hash in dict.keys(): continue
                
                dict[tx_hash] = time_stamp
                i = i + 1
                cnt_add = cnt_add + 1 
                
            #if i % 100000 == 0:
                #save()

        save()



print('total added to dic: ', cnt_add)
print('total lines in file: ', i)
print('doppelte tx: ', (i - cnt_add))





  