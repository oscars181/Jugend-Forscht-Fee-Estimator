import matplotlib.pyplot as plt 
import csv 
import pandas as pd
from datetime import datetime
import numpy as np
import seaborn as sns

#x = [] 
#y = [] 
colnames = ['time_stamp', 'conf_time','block_height']
with open('/home/oscar/jufobtc/code/test_comp_time.csv','r') as csvfile:
    df = pd.read_csv(csvfile,delimiter=' ', names=colnames)
    print('file read')
    #pd.options.display.max_rows = 25
    #df['time_stamp'] = pd.to_datetime(df['time_stamp'],unit='s')

    #print(df) 
    plot = df.plot(kind='scatter', x='block_height', y='conf_time', s=0.1)
    
    #sns.lmplot(x='block_height',y='conf_time', data=df)
    #print(df.info)
    #plt.xlim(109500,110500)
    plt.subplot = plt.hist('conf_time', cumulative=True, histtype='step')
    #plt.xlim(655900,None)
    #plt.ylim(0,500000)
    plt.grid()
    plt.show()
    
    """"
    for row in df: 
        x.append(int(row[1]))
        y.append(float(row[2])) 
        

    plt.plot(x, y, color = 'g', label = "fee", linestyle='dashed') 
    plt.xlabel('block_height') 
    plt.ylabel('fee per vbyte') 
    plt.title('Fees') 
    plt.legend() 
    plt.show() 
    """