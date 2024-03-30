
x = int(input("enter your number"))
#make error if to convert becouse dont forget eng say any input read as string

for i in range(1, x + 1):
    for j in range(1, i + 1):
     print(" "+ "*", end="")
    print("\r")

# dont forget indentation line 7 its belong to for parent
# how i make it from left ???

# name = "mostafa"
# print(name.replace("mo","kh"))


#x="ooo"
# check all character all in string is numric
"""
if(x.isdigit()):
    print("m")
else:
    print("j")
"""

"""
name = "kopkoooo"
print(name.count('o'))
"""

""""
for x in range(1,num+1):
   if(x==num):
        print(num * counter,ml.append(num*counter))
        break
   else:
        print(num * counter,ml.append(num*counter))
        counter+=1
"""
# this algorism which make until num
#============== ass2 =================================
"""
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

"""