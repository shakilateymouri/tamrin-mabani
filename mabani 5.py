


Number1 = int(input("Enter First Number :"))
L = []
count = 0

if Number1 > Number2 :
    Number1 = Number1+Number2
    Number2 = Number1-Number2
    Number1 = Number1-Number2

    
b = 0
for i in range(1, Number1+1):
    if (Number1 % i == 0):
        b += i 

if (b ==Number1*2) :
    print("Yes")
else:
    print("No")





Number1 = int(input("Enter First Number :"))
Number2 = int(input("Enter Second Number :"))
L = []


if Number1 > Number2 :
    Number1 = Number1+Number2
    Number2 = Number1-Number2
    Number1 = Number1-Number2

for i in range (Number1, Number2+1):
    count = 0
    for j in range(1,i+1):
        if (i%j ==0):
            count += j  
    if (count== 2*i):
        print("True")
        
    else:
        print("False")
        
print(L)





#Adad Zoj 

Number1 = int(input("Enter Number1 :"))
Number2 = int(input("Enter Number2 :"))
L = []

if Number1 > Number2 :
    Number1 = Number1+Number2
    Number2 = Number1-Number2
    Number1 = Number1-Number2

if (Number1%2 == 0):
    for i in range(Number1+2, Number2,2):
        L.append(i)    
else:
    for j in range(Number1+1, Number2, 2):
        L.append(j)


for i in range(Number1, Number2,2):
    L.append(i)
    
print(L)





s1 = []
s2 = []

for i in range(0, 10):
    s1.append(int(input("Enter Num for list 1 :")))
    
for j in range(0, 10):
    s2.append(int(input("Enter Num for list 2: ")))

s3 = s1+s2

def sort(get_list):
    for i in range(1, len(get_list)):
        if(get_list[i]<get_list[i-1]):
            j = i 
            while s3[j] < get_list[j-1] and j>0:
                get_list[j],get_list[j-1] = get_list[j-1], get_list[j]
                j = j-1
    return get_list

print(sort(s3))







