import pandas as pd
import numpy as np
main_data=pd.read_csv("/Users/chandrapavan1104/Harvestify/app/Data/disease_finder.csv")
main_data.drop(["Unnamed: 0"],axis=1,inplace=True)
print(main_data.info())
def linker(x):
    result=main_data[main_data["main_label"]==x].values.tolist()
    print(result)
linker("Apple___Apple_scab")