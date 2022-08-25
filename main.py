import pandas as pd
import os
import openpyxl
array = ""
dir = "../jsonToExcelToJson/Files" # Dosya yolu
os.chdir(dir)
for i in os.listdir():
    if i.endswith(".json"): # Döngü içinde uzantısı .json olan tüm dosyaları okur
        array += i + ","    # Okunan dosyalar boş bir stringe atılır , Virgülle ayrılması sağlanır
disp = 1
loop = 0

json1 = array.split(",")[loop]     #Virgüle kadarki dosya adı okunur ve a değişkenine atılır
df = pd.read_json(json1, 1, 1) # Pandas kütüphanesinden bir seri oluşturulur
data_frame = pd.DataFrame(df) # Excele yazdırmak için seri dataframe e dönüştürülür
loop += 1

while loop < 3:                 #  dosya içindeki json sayısı kadar döner
    json2 = array.split(",")[loop]   #Virgüle kadarki dosya adı okunur ve b değişkenine atılır
    df1 = pd.read_json(json2, 1, 0) # Yeni bir seri oluşturulur , oluşturlan bu seri döngü boyunca değişecektir

    data_frame[disp] = df1          # Oluşan her yeni seri Excelde yeni bir kolona eklenecektir
    loop += 1
    disp += 1

data_frame.to_excel("Excel_file.xlsx", sheet_name='1')    # Pandas kütüphanesi ile dataframe excele dönüştürülür

