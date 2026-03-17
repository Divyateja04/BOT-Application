import pandas as pd
def map_data(input_file, output_file):
    df = pd.read_excel(input_file)
    # Example mapping
    new_df = pd.DataFrame({
        "Name": df.iloc[:, 0],
        "Value": df.iloc[:, 1]
    })
    new_df.to_excel(output_file, index=False)
    return output_file