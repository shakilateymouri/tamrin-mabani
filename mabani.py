#Sort :moratab sazi
L = []

for x in range(0,10):
    L.append(int(input("Enter Num :")))

print(L1)
def sort(get_l):
    for i in range(1, len(get_list)):
        if(get_l[i]<get_l[i-1]):
            j = i 
            while L[j] < get_l[j-1] and j>0:
                get_l[j],get_l[j-1] = get_l[j-1], get_l[j]
                j = j-1
    return get_list

print(sort(L))


 
