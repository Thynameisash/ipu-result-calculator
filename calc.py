import re
from typing import final
import pandas as pd
import numpy as np
import tabula

print("Conversion Done !\nNow evaluating result...")

tabula.convert_into("MCA_2ndsem.pdf", "converted.csv", output_format="csv", pages='all')

data = pd.read_csv('converted.csv')

df = pd.DataFrame()

# roll=data.iloc[82,2]
# print(roll)

# ---------Get roll num of stud------------
count,i=1,28
rollnums=[]
while i <343 :
    if count<=10:
        roll=data.iloc[i,2]
        rollnums.append(int(roll))
        count+=1
        i+=5
    else:
        i+=4
        count=1

# print(len(rollnums))
df["Roll No."]=rollnums

#---------Get names of stud------------
count,i=1,29
names=[]
while i <344 :
    if count<=10:
        name=data.iloc[i,2]
        count+=1
        i+=5
        names.append(name)
    else:
        i+=4
        count=1
df["Name"]=names
# print(names)
# # # with pd.ExcelWriter('aa.xlsx') as writer:
# # #     df.to_excel(writer, sheet_name='sheet1')

# -----------Get all marks for stud-------------------
# marks=[]
# for i in range(4,358,6):
#     for j in range(3,25,2):
#         marks.append(data.iloc[i,[j]][0])


# ------All Subjects array-------
subs=[]
count,i=1,32
# for i in range(32,79,5):
while(i<347):
    if count<=10:
        sub=[]
        for j in range(3,8,1):
            val=data.iloc[i,j]
            sub.append(int(re.sub(r'[^0-9]', '', val)))
        subs.append(sub)
        i+=5
        count+=1
    else:
        i+=4
        count=1
# print(subs)
finalmarks=[]
for i in subs:
    marks=[]
    for j in i:
        j=str(j)
        if len(j)>2:
            res =[int(j[idx : idx + 2]) for idx in range(0, len(j), 2)]
            for k in res:
                marks.append(k)
        else:
            marks.append(int(j))
    finalmarks.append(marks)
# print(finalmarks)
# ------- Converting subjects to cols----------
# narr = []
# # print(narr)
# flat = sum(finalmarks,[])
# for i in range(len(marks)):
#     subarr = []
#     for j in range(i,len(flat),12):
#         subarr.append(flat[j])
#     narr.append(subarr)

# print(narr,end="\n")

# for i in range(len(narr)):
#     df[i] = narr[i]

# ------Sum of subs-------
sums=[]
pers=[]
# print(subs)
for i in finalmarks:
    s=sum(i)
    sums.append(s)
    pers.append((s/1200)*100)
df["Total"]=sums
df["Percentage"]=pers

df.to_excel("result.xlsx")
print("Done !")
