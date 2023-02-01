notaMedia = 6
aulasSemestre = 105
DP = 0
atividadeExtra = 0
atividadeFalta = 0


aluno = input("\nInforme o nome do aluno: \n")

#Faz entrada do aluno
n1 = int(input('Entre com a 1ª nota! :'))
while n1 > 10:      #Verifica a nota do aluno se é valida
    n1 = int(input('\nOPS!!!\nVocê digitou errado. \n \nPor favor! Entre com a 1ª nota! :'))

#Verifica a nota do aluno
if notaMedia < n1:
    print('\n{} conseguiu nota!'.format(aluno))
elif notaMedia == 6:
    print('\n{} passou raspando! Tome cuidado!!'.format(aluno))
else:
    print(' {} não alcançou nota, solicitar atividade extra!'.format(aluno))
    atividadeExtra += 1

#verifica falta do aluno
faltas1 = int(input('\nQuantas vezes este aluno faltou neste semestre? :'))
if faltas1 <=13:
    print('\n{} não estourou em faltas, \nMas verificar situação e solicitar trabalho.'.format(aluno))
  #  atividadeFalta += 1
elif faltas1 <=26:
    print('{} estourou em faltas! \nVerificar situação e solicitas trabalho.'.format(aluno))
 #   atividadeFalta += 2
else:
    print('Aluno {}, Reprovado neste semetre por falta!'.format(aluno))
    DP += 1

n2 = int(input('\nEntre com a 2ª nota! :'))

while n2 > 10:
    n2 = int(input('\nOPS!!!\nVocê digitou errado. \n \nPor favor! Entre com a 2ª nota! :'))
media1 = (n1 + n2) /2
print('Sua média atual é {}'.format(media1))

n3 = int(input('\nEntre com a 3ª nota! :'))
while n3 > 10:
    n3 = int(input('\nOPS!!!\nVocê digitou errado. \n \nPor favor! Entre com a 3ª nota! :'))
media2 = (n1 + n2 + n3) /3
print('Sua média atual é {}'.format(media2))

n4 = int(input('\nEntre com a 4ª e ultima nota! :'))
while n4 > 10:
    n4 = int(input('\nOPS!!!\nVocê digitou errado. \n \nPor favor! Entre com a 4ª nota! :'))
mediaFinal = (n1 + n2 + n3 + n4) /4
print('\nA sua média final é {}'.format(mediaFinal))
if mediaFinal <notaMedia:
    print('\nObjetivo não alcançado!\n \nAluno REPROVADO!!!')
else:
    print('\nObjetivo alcançado!\n \nAluno APROVADO!!! ')
