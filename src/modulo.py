#! /usr/bin/python

def aprxpi(n):
  f=1
  while n>0 and f==1:
    f+=1
  s = 0.0
  for i in range(1,n+1):
    x_i = float((i-0.5)/n)
    fx_i = float(4.0/(1.0 + x_i * x_i))
    s = s + fx_i
    r = s / n
  return r
   
if __name__=="__main__":
  import sys
  if(len(sys.argv)==3):
    parametro1 = int(sys.argv[1])
    parametro2 = int(sys.argv[2])
    l = [ ]
    for i in range(1,parametro2+1):
      a = aprxpi(parametro1+1)
      l = l+[a]
      print a
    print l
  else:
    print  'Debe introducir los dos valores correspondientes en la linea de comando'
    p1=5
    p2=5
    l = [ ]
    for i in range(1,p2+1):
      a = aprxpi(p1+1)
      l = l+[a]
    print l
    