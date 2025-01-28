# def loopingFor():
#     arr=[]
#     # for i in range(10):
#     #     n=int(input(f"Enter the {i+1}th element"))
#         # arr.append(n)
#     arr=[int(input(f"Enter the {i+1}th element")) for i in range(5)]
#     return arr

# arr=[i for i in range(10)]


#     arr=loopingFor()
#     print(sum(arr))

# l=[]
# print(l)

# l=["array",["report","open"]]
# print(l[0][1])

# l=(range(-2,3))

# l[2:5] will slice the list to index 2 to 5-1 
#print(b[-5:-2]) it will print the reverse slice of the array

# def sorte(arr):
#     mini=arr[0]
#     maxi=arr[0]
#     for i in arr:
#         if mini>i:
#             mini=i
#         elif maxi<i:
#             maxi=i
#     return maxi,mini

# def maxandmin():
#     arr=[int(input(f"Enter the {i+1}th element")) for i in range(5)]
#     maxi,mini=sorte(arr)
#     print("Max: ",maxi)
#     print("Min: ",mini)

# import math
# def prime(x):
#     #edge cases that can be eliminated
#     if (x < 2):
#         return False
#     if (x <= 3):
#         return True
#     if (x%2 == 0 or x%3 == 0):
#         return False
#     flag=0
#     if x==1:
#         return True
    
#     #iterate through the range of 5 due to eliminated edge cases 
#     #the math.sqrt is to ensure that we dont go beyond the range or multiplicity
#     #+1 to increase the range by 1

#     # for i in range(5,int(math.sqrt(x))+1):
#     i=5
#     while i<=(int(math.sqrt(x)+1)):
#         if x%i==0:
#             flag+=1
#         i+=2

#     if flag>=1:
#         return False
#     return True

# def looperforprime():
#     arr=[]
#     for i in range(1,10001):
#        if prime(i):
#         arr.append(i)
#     return arr

# def palindrome(t):
#     if t == t[::-1]:
#         print(t," Palindrome")
#     else:
#         print(t, " Not a palindrome")
    
# def splitter(entered_string):
#     temp=""
#     words=[]
#     for i in entered_string:
#         if i==" ":
#             if temp!="":
#                 words.append(temp)
#                 temp=""
#         else:
#             temp+=i
#     words.append(temp)
#     return words

# if __name__ == "__main__":
#     entered_string = input("Enter the string: ")
#     print(entered_string)
#     string_split=splitter(entered_string)
#     print(string_split)
#     for i in string_split:
#         palindrome(i)
        

# keyHolder = {"apples": 2, "banana": 5}
# keyHolder2=dict(name="bob", age=40)
# print(keyHolder)
# print(keyHolder2)
