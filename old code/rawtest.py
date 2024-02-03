import subprocess
import time
import json
import csv
import math


def cliNode(command): 
    
    command.insert(0,"bitcoin-cli" )
    answer = None
        
    answer = subprocess.check_output(command, cwd='C:\\Program Files\\Bitcoin\\daemon' ,shell=True)
    
    return answer
def checkHalving(block_height):     	# abhänig vom der Blockhöhe, erhält der Miner einen unterschiedlichen Reward
    if int(block_height) < 210000:      # return in sat
        return 5000000000
    if int(block_height) < 420000:
        return 2500000000
    if int(block_height) < 630000:
        return 1250000000
    if int(block_height) < 840000:
        return 625000000
    
block_hash = '00000000000000000024fb37364cbf81fd49cc2d51c09c75c35433c3a1945d04'
block_height = 500000
block_data = cliNode(['getblock', block_hash, '2'])

print('worked')

block_data_json = json.loads(block_data)

block_weight = block_data_json['weight']

block_subsidy = checkHalving(500000)
cb_vout = 0

for output in block_data_json['tx'][0]['vout']:
    cb_vout = cb_vout + (output['value'])* 100000000 

sum_fees = cb_vout - block_subsidy

print(sum_fees / (block_weight / 4))