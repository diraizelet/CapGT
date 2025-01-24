#for loop in comments remove them 
#comment the while loop and the variable i to run with the for loop

import math
def rotate(x,y):
    # for i in range(x,y+1):
    i=x
    while i<=y+1:
        print(i)
        print(prime(i))
        i+=1
def prime(x):
    #edge cases that can be eliminated
    if (x < 2):
        return False
    if (x <= 3):
        return True
    if (x%2 == 0 or x%3 == 0):
        return False
    flag=0
    if x==1:
        return True
    
    #iterate through the range of 5 due to eliminated edge cases 
    #the math.sqrt is to ensure that we dont go beyond the range or multiplicity
    #+1 to increase the range by 1


    # for i in range(5,int(math.sqrt(x))+1):
    i=5
    while i<=(int(math.sqrt(x)+1)):
        if x%i==0:
            print(x%i)
            flag+=1
        i+=2

    if flag>=1:
        return False
    return True
if __name__=="__main__":
    rotate(2,7)


#in the code we have to check for the input validity 
#or we can ask for upper and lower bounds