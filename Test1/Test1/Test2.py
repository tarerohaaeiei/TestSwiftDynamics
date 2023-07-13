Num = [1,2,1,3,5,6,4]
Num1 = [0,-2,-1,-3,-5,-6,-4]
Num2 = [-20,-2,-1,-3,-5,-6,-4]


def findMax(Num):
    Max =  Num[0]
    for x in range(1,len(Num)):
        if Num[x] > Max:
            Max = Num[x]
    print("Max number is : "+ str(Max)+"\n")

findMax(Num)
findMax(Num1)
findMax(Num2)
