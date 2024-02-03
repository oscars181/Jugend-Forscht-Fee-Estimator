import subprocess
import time
import json
import csv
import math


# before starting:
# cd C:\Program Files\Bitcoin\daemon <1
# bitcoind
# syntax for data: ,block_height,average_fee_per_vbyte
# data dir: C:\\Users\\oscar\\OneDrive\\Desktop\\Jugend Forscht BTC\\average_fee_per_vbyte



def writeInFile2(text):
    datei = open('C:\\Users\\oscar\\Documents\\GitHub\\Jugend-Forscht-Fee-Estimator\\average_fee_per_vbyte.csv','a',newline='')
    #datei.writelines(text)
    writer = csv.writer(datei, delimiter=';') #liest wahrscheinlich gesamte datei ein... nur über append möglich?
    for row in text:
        writer.writerow(row)
    datei.close()

def writeInFile(text):
    datei = open('C:\\Users\\oscar\\Documents\\GitHub\\Jugend-Forscht-Fee-Estimator\\average_fee_per_vbyte.csv','a',newline='')
    datei.writelines(str(text))
    datei.close
    

def setLatestBlock(text):
    datei = open('C:\\Users\\oscar\\Documents\\GitHub\\Jugend-Forscht-Fee-Estimator\\latestblock.txt','w')
    datei.writelines(text)
    datei.close()

def getLatestBlock():
    datei = open('C:\\Users\\oscar\\Documents\\GitHub\\Jugend-Forscht-Fee-Estimator\\latestblock.txt','r')
    latest_block = datei.readline()
    datei.close()
    return latest_block
    
def clear():
    datei = open('C:\\Users\\oscar\\Documents\\GitHub\\Jugend-Forscht-Fee-Estimator\\average_fee_per_vbyte.csv','w')
    datei.write("")
    datei.close()



def cliNode(command): 
    
    command.insert(0,"bitcoin-cli" )
    answer = None
        
    answer = subprocess.check_output(command)
    
    return answer

def getBlockJSon(block_hash):
    
    block_data = cliNode(['getblock', block_hash, '2'])
    block_data_json = json.loads(block_data)
    
    return block_data_json

def start():
    try:
        
        start_height = getLatestBlock()
        if start_height == '0':
            start_height = '1' 
    except:
        print('start nicht möglich \t definiere startpunkt')
    else:
        getFeePVByte(start_height)
    
def checkHalving(block_height):     	# abhänig vom der Blockhöhe, erhält der Miner einen unterschiedlichen Reward
    if int(block_height) < 210000:      # return in sat
        return 5000000000
    if int(block_height) < 420000:
        return 2500000000
    if int(block_height) < 630000:
        return 1250000000
    if int(block_height) < 840000:
        return 625000000
    

def getFeePVByte(block_height):
    i = 0
    while True: 
        block_height = int(block_height) + 1
        block_height = str(block_height)
        try:
            #print("trying")
            if block_height == 750000: break
            #print(block_height)
            block_hash = cliNode(['getblockhash', block_height])
        except: 
            time.sleep(5)
        else: 
            block_subsidy = checkHalving(block_height)
            
            block_hash_d = block_hash.strip().decode("utf-8")
        
            block_data_json = getBlockJSon(block_hash_d)
            
            #cbtx_hash = block_data_json["tx"][0]
            block_weight = block_data_json["weight"] 
            block_time = block_data_json["time"]
          
            cb_vout = 0
            
            for output in block_data_json['tx'][0]['vout']:
                cb_vout = cb_vout + (output['value'])* 100000000 
            sum_fees = cb_vout - block_subsidy
            SatPByte = sum_fees / (block_weight / 4)
            #setLatestBlock(block_height)
            #writeInFile('####\n')
            #text = [[str(block_time),str(block_height).rstrip(),str(SatPByte)]]
            text2 = str(block_time) + ' ' + str(block_height) + ' ' + str(SatPByte)
            #writeInFile(text2)
            #writeInFile(block_height)
            #writeInFile(",")
            #writeInFile(str(SatPByte))
            #writeInFile(',\n')
            print(text2)
            i = i+1
            
            
#getFeePVByte('8173017')

getFeePVByte(355000)
    

#start()
#getFeePVByte('817712')

