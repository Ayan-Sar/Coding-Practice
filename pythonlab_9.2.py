mylist=[1,2,3,"4",5]
sum=0
for i in mylist:
    try:
        sum=sum+i
        if(i<4):
            continue
            print(sum)
        print(mylist[5])
    except Exception as e:
            print('error code:',e)