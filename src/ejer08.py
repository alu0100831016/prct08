#! /usr/bin/python
import modulo
import math
PI = 3.1415926535897931159979634685441852
def error(nro_intervalos,n_test,umbral):
  fallos=0	
  for i in range(n_test):
    a= modulo.aprxpi(nro_intervalos)
    valor=abs(a-PI)
    if (valor >= umbral):
      fallos+=1
      
  por_error=(fallos/n_test)*100
  return por_error
 
nro_intervalos=int(raw_input('Introduzca el numero de intevalos (n > 0): '))
n_test=int(raw_input('Introduzca el numero de test: '))
umbral=float(raw_input('Introduzca el valor del umbral: '))
pr=error(nro_intervalos,n_test,umbral)
print pr 