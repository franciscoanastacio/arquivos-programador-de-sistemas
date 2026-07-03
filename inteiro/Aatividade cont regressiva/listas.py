cliente = ['joão','maria','josé','ana']
print(cliente)
cliente.append('flavio')
print(cliente)
for i in range(3):
    nome = input('nome do cliente:')
    cliente.append(nome)
    print(cliente)