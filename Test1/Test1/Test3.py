Num = 7

def findFactorial(num):
    numFac = 1
    for x in range(1,num):
        numFac *= x 
    print(numFac)
    return numFac

def findZeronumback(num):
    c=0
    strnum = str(num)
    for x in range(len(strnum)-1,0,-1):
        if strnum[x]=='0':
            c+=1
        else:
            break
        
    print("Num of Zero : "+str(c))
    
findZeronumback(findFactorial(Num))
