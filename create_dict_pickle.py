import bz2
import json
import pickle
from itertools import islice


path = '/home/oscar/jufobtc/times.lst.bz2'
line = []
dict = {}
i = 0
dict_state = 0

with bz2.BZ2File(path) as file:
    for line in islice(file,310000000,None):
        if i == 0: print('islice loaded')
        #if i == 1000000000: break
        try: 
            (tx_hash, time_stamp) = line.split()
        except:
            #print('not working: ', end='') 
            #rint(line)
            #print(i)
            i = i + 1
            continue
        else:
            #print(dict_state, i)
            time_stamp = time_stamp.decode().strip('[b]')
            time_stamp = int(time_stamp)
            
            if i % 10000000 == 0 and dict_state == 0: print(i, time_stamp)
            i = i + 1
            
            if time_stamp == 1571443399790: # tx_hash von block 600000
                i = 1
                dict_state = 1
                print('start reached')               
            if dict_state == 1:
                #if i == 10000000: break
                #tx_hash = tx_hash.decode().strip()
                tx_hash = tx_hash.decode().strip()
                #print(tx_hash, time_stamp)
                dict[tx_hash] = int(time_stamp)
                if i % 10000000 == 0:
                    with open('/home/oscar/jufobtc/dict_mempool_start_600000.pkl', 'ab') as dict_save:
                        print('loaded pkl file')
                        #print(dict)
                        pickle.dump(dict, dict_save)
                        print('dumped', i)
                        dict_save.close()
                        #print(dict)
                    dict.clear()
                    

        #with open('/home/oscar/jufobtc/dict_mempool_start_65000.pkl', 'rb') as dict_save:
            #dict = pickle.load(dict_save)
            #print('done')
            #dict_save.close()
 
            