#============== ass2 =================================

num=int(input("enter number"))
ml=[]
counter=1

for i in range(1,num+1):
    apended_list=[]

    for x in range(1, i + 1):
        if (x == i):
            apended_list.append(i * x)
            ml.append(apended_list)
            break
        else:
            apended_list.append(i * x)


print(ml)