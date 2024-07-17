# une petite fonction qui permet de calculer le factoriel d'un nombre entier
def factoriel(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact
print("le factoriel de 5 est :", factoriel(5)
