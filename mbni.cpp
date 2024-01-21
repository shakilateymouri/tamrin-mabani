#include(iostream.h)
main()
{
    int m=1;n=0;fact,n;
      while(m>n)
      {
        fact=1;
        x=m-n;
        while (x>1)
        {
            fact=fact*n;
            x--;
        }
         cout<<fact;
         cin>>m>>n;
      }
}