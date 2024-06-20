#desafio beecrowd | 2455 Gangorra

p1,c1,p2,c2 = map(int,input().split())

if p1*c1==p2*c2:print("0") #gangorra em equlibrio
elif p1*c1<p2*c2:print("1") #gangora esta inclinada para direita pq P2 é maior
else:print("-1") # se não P1 eh maior e esta inclinada pára esquerda