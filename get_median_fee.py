import subprocess
import os
import sys
import json

args = sys.argv

 

def cliNode(command): 
    
    command.insert(0,"bitcoin-cli")
    answer = None 
    try: 
        answer = subprocess.check_output(command)
    except:
        dksajfhaskldjfh = 0 #pseudo line
    else:
        return answer
   

def writeInFile(text):
    #datei = open('/home/oscar/jufobtc/data/median_fees_750.csv','ab')
    datei.write(str.encode(text + '\n'))
    #datei.close

line = subprocess.check_output(['cd ~/jufobtc/data && less median_fees_750.csv | tail -1'], shell=True).strip().decode('utf-8')
temp = line.split()
start = int(temp[1]) + 1
end = subprocess.check_output(["bitcoin-cli", "getblockcount"]).strip().decode('utf-8')


with open('/home/oscar/jufobtc/data/median_fees_750.csv','ab') as datei:
    for block in range(int(start), int(end)):
        temp_block_data = json.loads(cliNode(["getblockstats", str(block)]))
        
        median_fee = temp_block_data["feerate_percentiles"][2]
        blocktime = temp_block_data["time"]
        text = str(blocktime) + " " + str(block) + " " + str(median_fee)
        print(text, end="\r")
        writeInFile(text)
        
    

        