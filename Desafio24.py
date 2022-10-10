# Verifica se o nome da cidade começa com Santo
c = str(input('Digite o nome da sua cidade: ')).strip().upper()
corta = c.split()
print('SANTO' in corta[0])

#Outra forma de fazer:
print(c[:5] == 'SANTO')
