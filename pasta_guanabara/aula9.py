# # nomecompleto = str(input('Qual é o seu nome completo? '))
# # maiusculo = nomecompleto.upper()
# # minusculo = nomecompleto.lower()
# # numeros = len(nomecompleto.replace(" ", ""))
# # primeiro_nome = nomecompleto.split()[0]
# # print('Maiusculo é: {}, Minusculo é : {} Quantidade de numeros : {} Seu primeiro nome é: {}'.format(maiusculo,minusculo,numeros,primeiro_nome))

# pedindo_numero = input('Qual é o seu numero? ')
# formatado = pedindo_numero.zfill(4)

# divizao_milhar = formatado[0]
# divizao_centena = formatado[1]
# divizao_dezena = formatado[2]
# divizao_unidade  = formatado[3]
# print('Seu numero em unidade de medida é: ')
# print(f'Unidade:{divizao_unidade}')
# print(f'Dezena:{divizao_dezena}')
# print(f'Centena:{divizao_centena}')
# print(f'Milhar:{divizao_milhar}')

nome = input('Qual é o seu nome COMPLETO? ').strip()
nome1 = nome.upper().split()
nomesilva = 'SILVA' in nome1
print(f'Seu nome tem Silva? {nomesilva}')


    