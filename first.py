import math
import numpy as np

brojOcena=int(input("UNesi broj ocena:"))
listaOcena=[]

for i in range (brojOcena):
  ocene=int(input("unesi ocenu:"))
  listaOcena.append(ocene)

srednjaVrednost=np.mean(listaOcena)  
print(srednjaVrednost)

