import pandas as pd
def read_data(file_path):
    data=pd.read_csv(file_path)
    return data

def analyze_data(data):
    print("First few rows of the data:")
    print(data.head())
    print("\n Basic Statistics of the data:")
    print(data.describe())
    grouped_data=data.groupby('Category')['Value'].mean()
    print("\n Average value per category:")
    print(grouped_data)
    filtered_data=data[data['Value']>50]
    print("\n Data where value>50:")

    print(filtered_data)

if __name__=="__main__":
    file_path="data.csv"
    data=read_data(file_path)
    analyze_data(data)
