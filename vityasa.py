#QUESTION 1

n=int(input("enter the number of items"))
stored_data1=[]
count=0
sumof=0
for i in range(0,n):
    data=input("enter the items")
    try:
        x=int(data)
        if x>0:
            stored_data1.append(x)
    except:
        y=data
print("valid :",len(stored_data1))
print("invalid :",n-len(stored_data1))
stored_data1.sort()
print("Min :",stored_data1[0])
print("Max :",stored_data1[-1])
for i in stored_data1:
        sumof=sumof+i
average=int(sumof/len(stored_data1))
print("average :",average)

