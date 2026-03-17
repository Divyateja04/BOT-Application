import pandas as pd

def read_excel(file_path):
    
    df = pd.read_excel(file_path)

    data = df.to_dict(orient="records")

    return data