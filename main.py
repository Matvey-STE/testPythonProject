import pandas as pd
from fastapi import FastAPI


data = {
    'col1':['a1', 'a2', 'a3'],
    'col2':['a1', 'a2', 'a3'],
        
}

df = pd.DataFrame(data)

print(df)