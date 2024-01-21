#include(iostream.h)
main()
{
    int n,fact =1;
    cin>>n;
    while(n>1)
     {
      fact=fact*n;
      n--;
     }
      cout<<fact;
}