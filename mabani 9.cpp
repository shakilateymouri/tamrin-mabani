#include<iostream.h>
main()
int sums(int n)
{
    int s=0 , m=n,counter =0;
    while(m ! =0)
    {
        s=s+(m%10;)
        m=m/10;
        counter++;
    }
    return s;
    int*sums(int n)
    {
        int s=0,m-n,counter=0;
        int *p;
        while (m !=0)
    }
    s=s+(m%10);
    m=m/10;
    counter++;
      p= &s;
      *(p+1)=counter;
      return p;
}