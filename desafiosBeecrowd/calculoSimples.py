
peca1, quantidade1, valorUni1  = map(float,input().split())

peca2, quantidade2, valorUni2  = map(float,input().split())

total = (quantidade1 * valorUni1) + (quantidade2 * valorUni2)

print(f'VALOR A PAGAR: R$ {total:.2f}')