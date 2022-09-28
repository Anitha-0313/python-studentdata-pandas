import pandas as pd
data=pd.read_csv("st.csv")
ele=input()
print(data.loc[data["Name"]==ele])
