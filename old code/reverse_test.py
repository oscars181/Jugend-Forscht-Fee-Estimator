from file_read_backwards import FileReadBackwards
import bz2
from itertools import islice

path = '/home/oscar/jufobtc/code/test_comp_time.csv'

with open(path, 'r') as f:
    for line in f:
        print(line)
        i = i + 1;
        
