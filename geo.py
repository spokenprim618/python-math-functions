def geo( n1,n2,nthTerm):
  d=n2/n1
  first=n1*(d)**(nthTerm-1)
  ans=round(first,3)
  return ans
print(geo(4, 5,7)) 
