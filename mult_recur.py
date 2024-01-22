def mault_recursive(m1, m2):
    print(f"m1 is:{len(m1)}*{len(m1[0])}")
    print(f"m2 is:{len(m2)}*{len(m2[0])}")
    if len(m1[0]) != len(m2):
        print ("Not possible!!")
        return
 
    result = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]
 
    # recursive function
    def multiply(m1, m2, result, i, j, k):
        #no more rows remained
        if i >= len(m1):
            return
        #go to next row of first matrix:m1
        if j >= len(m2[0]):
            return multiply(m1, m2, result, i+1, 0, 0)
        
        #go to next column of m2
        if k >= len(m2):
            return multiply(m1, m2, result, i, j+1, 0)
        #set result
        result[i][j] += m1[i][k] * m2[k][j]
        multiply(m1, m2, result, i, j, k+1)
 
    #call recursive function with first row and first column
    multiply(m1, m2, result, 0, 0, 0)
    return result
 

m1 = [[1, 2, 3],
           [4, 5, 6]]

m2 = [[2],
           [3],
           [2]]
 
result = mault_recursive(m1, m2)
for row in result:
    print(row)