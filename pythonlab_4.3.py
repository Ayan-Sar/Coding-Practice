string=input("Enter the string !!")
newstr=list(string)
newlist=[]
for j in newstr:
    if j not in newlist:
        newlist.append(j)
        count=0
        for i in range(len(newstr)):
            if j==newstr[i]:
                count+=1
        print("{}:{}".format(j,count))