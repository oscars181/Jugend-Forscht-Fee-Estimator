import subprocess
import os
import sys
import json

'''
args = sys.argv

mode = sys.argv.get()
'''
adress = ""

def get_average_fee(**kwargs):
    if "block_height" in kwargs: 
        block_height = str(kwargs["block_height"])
    else: 
        print('else')   
        block_height = cliNode(["getblockcount"]).strip().decode('utf-8')
        print(block_height)
    try:    
        block_hash = cliNode(['getblockhash', str(block_height)]).strip().decode("utf-8")
    
    except:
        x = 0 
    else:
        block_subsidy = checkHalving(block_height)
        block_data_json = getBlockJSon(block_hash)
        block_weight = block_data_json["weight"] 
        block_time = block_data_json["time"]
        cb_vout = 0
        for output in block_data_json['tx'][0]['vout']:
            cb_vout = cb_vout + (output['value'])* 100000000 
        sum_fees = cb_vout - block_subsidy
        SatPByte = sum_fees / (block_weight / 4)
        text = str(block_time) + ' ' + str(block_height) + ' ' + str(SatPByte)
        return text

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
    
    block_data = cliNode(['getblock', block_hash, '2'])
    block_data_json = json.loads(block_data)
    
    return block_data_json

def writeInFile(text):
    datei = open('/home/oscar/jufobtc/data/fees_750.csv','ab')
    datei.write(str.encode(text + '\n'))
    datei.close
    
def cliNode(command): 
    command.insert(0,"bitcoin-cli")
    answer = None 
    try: 
        answer = subprocess.check_output(command, stderr=subprocess.DEVNULL )
    except:
        #print(str(command))
        #print(answer)
        c = 0
    else:
        return answer     
      
# copy comp of fee estimates
subprocess.Popen(["%s :/home/bitcoin/jugend_forscht/fee_estimator_comp.csv /home/oscar/jufobtc/data"%adress], shell=True)
# copy memtx 
subprocess.Popen(["%s :/home/bitcoin/jugend_forscht/mem_tx.csv /home/oscar/jufobtc/data" %adress], shell=True)
print('copied fee_comp and mem_tx')  

# get last line of average fee data 
line = subprocess.check_output(['cd ~/jufobtc/data && less fees_750.csv | tail -1'], shell=True).strip().decode('utf-8')
temp = line.split()

#print(temp)
last_block = temp[1]
print('last block in avg_fee: ', last_block)
cur_block = subprocess.check_output(["bitcoin-cli", "getblockcount"]).strip().decode('utf-8')
print('current block height in chain: ', cur_block)
last_block = int(last_block)
if int(last_block) == int(cur_block): 
    print('avg fees is already updated')
    exit(1)
else:   
    while True:
            
        if int(last_block) <= int(cur_block):
            last_block = last_block + 1
            temp = get_average_fee(block_height=last_block)
            if not temp == None: 
                print(temp)
                writeInFile(temp)

            
        else:
            print('updated average_fees')
            break
        
        
