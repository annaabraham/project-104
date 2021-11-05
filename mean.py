import csv
with open('SOCR-HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    nnum=fileData[i][1]
    newData.append(float(nnum))
total=0
for x in newData:
    total+=x
n=len(newData)
mean=total/n
print(mean)