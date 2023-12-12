import matplotlib.pyplot as plt 
import csv 
import pandas as pd

#x = [] 
#y = [] 
  
with open('C:\\Users\\oscar\\Documents\\GitHub\\Jugend-Forscht-Fee-Estimator\\average_fee_per_vbyte.csv','r') as csvfile:
    df = pd.read_csv(csvfile,delimiter=';')
    #pd.options.display.max_rows = 25
    print(df) 
    df.plot(kind= 'scatter', x='block_height', y='fee_per_vbyte', s=1)
    print(df.info)
    #plt.xlim(109500,110500)
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