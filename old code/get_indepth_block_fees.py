import subprocess
import time
import json



    
    
    
    
def cliNode(command): 
    
    command.insert(0,"bitcoin-cli" )
    answer = None
    try:
        answer = subprocess.check_output(command, cwd='C:\Program Files\Bitcoin\daemon' ,shell=True)
    except:
        print('failed')
    return answer

def getBlockJSon(block_hash):
    
    block_data = cliNode(['getblock', block_hash])
    block_data_json = json.loads(block_data)
    
    return block_data_json

def getFeesPerTx(raw_cbtx_decoded_json):
    tx_in = tx_out = 0
    for output in raw_cbtx_decoded_json['vout']:
                
                tx_out = tx_out + (output['value'])* 100000000
    
    for input in raw_cbtx_decoded_json['vin']:
                
                tx_in = tx_in + (input['value'])* 100000000
                
    sum_fee = tx_in - tx_out
    if sum_fee <= 0:
        return 0 
    return sum_fee


def start(block_height):
    
    block_hash = cliNode(['getblockhash', block_height])
    block_hash_d = block_hash.strip().decode("utf-8")
    block_data_json = getBlockJSon(block_hash_d)
    i = 0
    sum_fees = 0
    sum_weight = 0
    
    for tx in block_data_json['tx']:
        try:
            tx_hash = tx            
            raw_tx = cliNode(['getrawtransaction', tx_hash, 'true', block_hash_d])    
        except: 
            break

        # raw_tx = cliNode(['getrawtransaction', tx_hash, 'true', block_hash_d])
        raw_tx_decoded = raw_tx.decode("utf-8")
        raw_tx_decoded_json = json.loads(raw_tx_decoded) # summe der outputs nehmen 
        tx_in = 0
        sum_weight = sum_weight + raw_tx_decoded_json['vsize']
        print(sum_weight + sum_fees + (sum_fees / sum_weight))
        sum_fees = getFeesPerTx(raw_tx_decoded_json)
    print(sum_weight + sum_fees)
    
        
start('819890')