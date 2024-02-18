import json
import subprocess
import time
from operator import itemgetter
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import math

def cliNode(command): 
    
    command.insert(0,"bitcoin-cli")
    answer = None 
    try: 
        answer = subprocess.check_output(command)
    except:
        #print(str(command))
        #print(answer)
        c = 0
    else:
        return answer
    
    
def cliNode(command): 
    
    command.insert(0,"bitcoin-cli")
    answer = None 
    try: 
        answer = subprocess.check_output(command)
    except:
        #print(str(command))
        #print(answer)
        c = 0
    else:
        return answer

def btc_core_get_fee(range):
    data = cliNode(['estimatesmartfee', str(range)])
    data = json.loads(data)
    data["feerate"] = data["feerate"]*100000
    return data

def fee_MS_api():
    url = 'https://mempool.space/api/v1/fees/recommended'
    data = json.loads(fetch_data_url(url))
    return data

def fetch_data_url(link):
   data = urlopen(link).read()
   #data = json.loads(data.read())
   #print(data)
   return data

def wtfee_get_fee():    
    ts = time.time()
    ts = int(ts)
    url = 'https://whatthefee.io/data.json?c=1706726700'
    req = Request(url, headers={'User-Agent': 'Mozilla/6.0'})
    data = urlopen(req).read()
    data = json.loads(data)
    value = data["data"][0][4]
    fee = round(math.exp(value/100),1)
    return fee

def writeInFile(text):
    datei = open('/home/oscar/jufobtc/data/fee_estimator_comp.csv','a',newline='')
    datei.writelines(str(text))
    datei.close
      
    
def estimate_comp(**kwargs):
    write = kwargs.get("write", True)
    print(write)
        
    while True:
        block_height = int((["getblockcount"]))
        next_block = block_height + 1
        sec = time.time()
        t = time.ctime(sec)
        
        #print('aktuelle Blockhöhe:', block_height.strip().decode("utf-8"),'time:',t )
        
        data_btc_core = btc_core_get_fee(1)
        fee_btc_core = str(data_btc_core["feerate"])
        #print('Bitcoin Core Estimation for:', data_btc_core["blocks"], fee_btc_core)
        
        data_ms_api = fee_MS_api()
        fee_ms = str(data_ms_api["fastestFee"])
        fee_wtf = wtfee_get_fee()
        
        #print('Mempool.Space Estimation:', fee_ms)
        # syntax
        # block(next), mempool.space fee, btc core fee, wtfee fee, timestamp 
        # next block zu mappen der Gebühren später
        text = str(next_block) + ' ' +  str(fee_ms)+ ' ' + str(fee_btc_core) + ' ' + str(fee_wtf) + ' ' + str(t)
        text2 = str(next_block) + ' ' +  str(fee_ms)+ ' ' + str(fee_btc_core) + ' ' + str(fee_wtf) + ' ' + str(sec) + '\n'
        print(str(text))
        if write == True:
            writeInFile(text2)
        time.sleep(60)
        old_block = block_height


def get_average_fee(**kwargs):
    if "block_height" in kwargs: 
        block_height = str(kwargs["block_height"])
    else: 
        print('else')   
        block_height = (["getblockcount"]).strip().decode('utf-8')
        print(block_height)
        
    block_hash = (['getblockhash', str(block_height)]).strip().decode("utf-8")
    block_subsidy = checkHalving(block_height)
    block_data_json = getBlockJSon(block_hash)
    block_weight = block_data_json["weight"] 
    block_time = block_data_json["time"]
    cb_vout = 0
    for output in block_data_json['tx'][0]['vout']:
        cb_vout = cb_vout + (output['value'])* 100000000 
    sum_fees = cb_vout - block_subsidy
    SatPByte = sum_fees / (block_weight / 4)
    #text2 = str(block_time) + ' ' + str(block_height) + ' ' + str(SatPByte)
    return str(SatPByte)

def checkHalving(block_height):     	# abhänig vom der Blockhöhe, erhält der Miner einen unterschiedlichen Reward
    if int(block_height) < 210000:      # return in sat
        return 5000000000
    if int(block_height) < 420000:
        return 2500000000
    if int(block_height) < 630000:
        return 1250000000
    if int(block_height) < 840000:
        return 625000000
    
def getBlockJSon(block_hash):
    
    block_data = (['getblock', block_hash, '2'])
    block_data_json = json.loads(block_data)
    
    return block_data_json

estimate_comp()