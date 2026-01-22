# Trial 1

# a,b,c=int(input("Enter first number:")),int(input("Enter second number:")),int(input("Enter third number:"))
# if a>b: 
#     if a>c:
#         print(a,"a is grt")
#     else:
#         print(c,"c is grt")
# else:
#     if b>c:
#         print(b,"b is grt")
#     else:
#         print(c,"c is grt")

# if a!=b and a!=c:
#     if a>b and a>c:
#         print("a is grt")
#     elif b>c and b>a:
#         print("b is grt")
#     else:
#         print("c is grt")

# Trial 2

# 1. Input counter and Input set list
# approach: I have taken list to validate the incoming stream of inputs in real-time, In case of different variables these checks would increase the conditions format 
ipctr=0
ipSet=[]

# 2. While loop with cond., temp variable check if its digit then will be     
# approach: input counter will ensure that list would only have three elements, 
while(ipctr<3):
    temp=input("Enter value: ")
    if temp.isdigit()==True:
        ipctr+=1
        ipSet.append(int(temp))
    else:
        print("Enter Integer value")
# print(ipSet)
a,b,c=ipSet
if a>b: 
    if a>c:
        print(a,"a is grt")
    else:
        print(c,"c is grt")
else:
    if b>c:
        print(b,"b is grt")
    else:
        print(c,"c is grt")