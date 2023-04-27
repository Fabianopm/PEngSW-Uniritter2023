from models.cliente import Cliente
from models.conta import Conta

fabiano: Cliente = Cliente('Fabiano Pacheco', 'fpmonteiro@gmail.com', '98765432343', '24/10/2000')
danielle: Cliente = Cliente('Danielle Bandeira', 'danibs@gmail.com', '09878765454', '27/06/2001')

# print(fabiano)
# print(danielle)

contaf: Conta = Conta(fabiano)
contaa: Conta = Conta(danielle)

print(contaf)
print(contaa)
