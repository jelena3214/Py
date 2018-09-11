import math

def kvadratniKoren(broj):
  brojac=0
  if broj>=0:
    while brojac**2<broj:
      brojac=brojac+1
    if brojac**2!=broj:
      print("Nije savrsen koren")
      print (None)
    else: return brojac
  else:
   print("Broj je negativan ili nula")
m=kvadratniKoren(25)
print(m)
