#PERGUNTAR O NOME DA PESSOA E TRATAR A STR
name = input(str('Qual é o seu nome? ')).strip().lower()

#TRATAMENTO DA STR RECEBIDA
name1 = name.title()

#APRESENTAR O NOME DA PESSOA COM UM OLÁ
print(f'Ola {name1}' + ", Obrigado por falar seu nome, burrao ")
