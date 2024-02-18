import zmq
import json
from bitcoinlib.transactions import transaction_deserialize
import time
import pickle



pub_raw_tx_ip = 'tcp://127.0.0.1:29000'

#pickle_path = '/home/oscar/jufobtc/data/dict_mempool_tx.pkl'
#pickle_path = '/home/jugend_forscht/mem_tx.csv'

#mem_tx_path = '/home/oscar/jufobtc/data/mem_tx.csv'
mem_tx_path = '/home/jugend_forscht/mem_tx.csv'

def writeInFile(text, file):
    datei = open(file,'a',newline='')
    datei.writelines(str(text))
    datei.close

def connect():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE, 'hashtx')
    socket.connect(pub_raw_tx_ip)
    return socket

def start():
    
    temp = []
    tx_dict = {}
    #save = open(pickle_path, 'ab')
    socket = connect()
    while True:
        topic, hash, number = socket.recv_multipart()
        
        hash = hash.hex()
        timestamp = time.time()
        print(number.hex())
        temp_tx = str(hash) + ' ' +  str(timestamp) + '\n'
        #tx_dict[str(hash)] = str(timestamp)
        
        writeInFile(temp_tx, mem_tx_path)
        print(temp_tx)

start()