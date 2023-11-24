


Maximum = int(input("Enter Number :"))

for i in range (1,10):
    Number = int(input("Enter Number :"))
    if Number >Maximum :
        Maximum = Number 
print(Maximum)



Number= int(input("Enter Number :"))

if (Number%2== 0):
    print("Even")
else :
    print("Add")





Number1 = int(input("Enter First Number :"))
Number2 = int(input("Enter Second Number :"))
L = []
for i in range(Number1+1,Number2):
    if (i%2 ==0):
        L.append(i)
print(L)





Number = int(input("Enter Number:"))
count = 0 

for i in range(2,Number):
    if (Number%i==0):
        count += 1 

if count > 0 :
    print("H")
else:
    print("F")
    





Number1 = int(input("Enter First Number :"))
Number2 = int(input("Enter Second Number :"))
L1 = []
count = 0

if Number1 > Number2 :
    Number1 = Number1+Number2
    Number2 = Number1-Number2
    Number1 = Number1-Number2

for number in range(Number1+1, Number2):
    for j in range(2,number):
        if (number%j==0):
            count += 1 
            break
        if count != 0 :
            L.append(number)
            break
print(L)
                
        


 c
