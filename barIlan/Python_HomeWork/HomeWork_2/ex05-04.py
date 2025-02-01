import pandas as pd

filedata=pd.read_csv('kc_house_data.csv')

print(f'there are {filedata.shape[0]} houses in the list.\n')
#there are 21613 houses in the list.

max=filedata['price'].max()
min=filedata['price'].min()
avr=pd.Series.mean(filedata['price'])
std=pd.Series.std(filedata['price'])
print(f'the max is : {max} , the min is : {min} , the avr is : {avr} , the std is : {std}\n')
#the max is : 7700000.0 , the min is : 75000.0 , the avr is : 540088.1417665294 , the std is : 367127.19648269983

lowId=filedata.loc[filedata['price']==filedata['price'].min()]
lowIdIndex=lowId.index[0]
print(f"the lowest price has the id of:{filedata.iloc[lowIdIndex].id}")
highId=filedata.loc[filedata['price']==filedata['price'].max()]
highIdIndex=highId.index[0]
print(f"the highest price has the id of:{filedata.iloc[highIdIndex].id}\n")
#the highest price has the id of:6762700020
#the lowest price has the id of:3421079032

print(f"the earliest house was built in {filedata['yr_built'].min()}\n")
#the earliest house was built in 1900
#there are more than one house that was built in 1900 so I'll print every
#house that built in 1900 and if he was renovated.
for i in range(filedata.shape[0]):
    if filedata.iloc[i]["yr_built"] == 1900:
        if filedata.iloc[i]["yr_renovated"] == 0:
            print(f"id:{filedata.iloc[i]['id']} was built in 1900 (the oldest house that was built in this list) and isn't renovated")
        else:
            print(f"id:{filedata.iloc[i]['id']} was built in 1900 (the oldest house that was built in this list) and is renovated")

print(f"the average year is {int(filedata['yr_built'].mean())}\n")
#the average yr_built is 1971


repaired=filedata.loc[filedata['yr_renovated']>0]
print(f"the percentage of houses the were repaired is:{(repaired.shape[0]/filedata.shape[0])*100}%.({repaired.shape[0]} houses out of {filedata.shape[0]})\n")
#the percentage of houses the were repaired is:4.228936288344977%.(914 houses out of 21613)

twentyFourteen=0
tweentyfighteen=0
for i in range(0,filedata.shape[0]):
    if filedata.iloc[i]["date"][:4] == '2014':
        twentyFourteen += 1
    else:
        tweentyfighteen += 1
if twentyFourteen > tweentyfighteen:
    print("Most of the houses were bought in 2014")
else:
    print("Most of the houses were bought in 2015")
# Most of the houses were bought in 2014