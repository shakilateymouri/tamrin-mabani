#include(iostream.h)
main()
int * sort(int*A)
{
    int i,j,temp;
    for(i-0;i<len(A);i++)
     for(j=i,j<len(A),j++)
      if(A[i]<A[j+1])
      {
        temp=A[i];
        A[j]=A[j+1];
        A[j+1]=temp;
      }
      return A
}