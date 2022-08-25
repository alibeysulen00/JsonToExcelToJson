import pandas as pd
data_fr = pd.read_excel("Files/Excel_file.xlsx", index_col=0)
columns = data_fr.columns
array=["a","b","c","d","e","f","g","h","i","o","u","v","y","z","a1","b1","b2","c2","d2","e2","f2","g2","h2","i2","o2","u2","v2","y2","z2","a3","b3","c3","d3","e3","f3"]
for column in columns:
    json1 = data_fr[column]
    df11 = data_fr[column]
    df11.to_json(array[column]+'.json')
