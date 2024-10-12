real = float(input('Quanto dinheiro vc tem na carteira? R$'))
dolar = real/ 5.61
print('Com R${:.2f} você pode compra US${:.2f}'.format(real,dolar))