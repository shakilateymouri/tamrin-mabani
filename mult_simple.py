def matrix_mult(m1, m2):
    print(f"m1 is:{len(m1)}*{len(m1[0])}")
    print(f"m2 is:{len(m2)}*{len(m2[0])}")
    if len(m1[0]) != len(m2):
        print ("Not possible!!")
        return
    
    satr=len(m1)
    seton=len(m2[0])
    print(f"result will be :{satr} :{(seton)}")
    result=[[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    print(result)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
           for k in range(len(m2)):
               result[i][j] += m1[i][k] * m2[k][j]
    return result
a=[[1,2,3],
   [4,5,6]]
b=[[2],
   [3],
  [4]]
s=matrix_mult(a,b)
print(s)
c=[[1,2,3]]
s=matrix_mult(a,c)
