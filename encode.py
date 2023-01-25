import pandas as pd
import matplotlib.pyplot as plt
dict = {'DATE':[31-1-2020,29-2-2020,30-3-2020,31-4-2020,30-5-2020],
'PRICE':[10000,7000,20000,8000,9000],'PRODUCT_ID':[91,92,93,94,95],
'QUATITY_PURCHASED':[1,2,3,4,5],'SERIAL_NO':[101,102,103,104,105],
'USR_ID':[1001,1002,1003,1004,1005],'USR_TYPE':['A','B','C','D','E'],
'USR_CLASS':['UPR','UPR','MDL','LWR','MDL'],
'PUR_WEEK':['MON','TUE','WED','MON','FRI']}

df = pd.DataFrame(dict)
df.to_csv("df.csv")
print(df.head)