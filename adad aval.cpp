#ihnclude (iostreamok)
main()
{
    int n,i,sum = 0;
    cin>>n;
    for (i=1,i<=n,i++)
      if (n%i==0)
        sum+=i;
    if(sum==2*n)
       cout<<'true'
    else
    cout<<'false'
      
}