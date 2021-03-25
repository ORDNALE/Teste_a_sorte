# -----TENTE ADIVINHAR O NUMERO SORTEADO DE 1 A 6---------
import random

print(f'OLA, TESTE SUA SORTE TENTANDO ADIVINHAR O NUMERO GERADO PELO COMPUTADOR! \n BOA SORTE!!')
numero_certo = []
pts = 0
cont = 0
rodada = []

while True:
    cont += 1
    print(f'TENTATIVA {cont} ')
    dado = int(input('Digite um numero inteiro entre 1 e 6! '))
    print(f'Seu Numero [{dado}] ')
    rodar = random.randint(1, 6)

    if dado == rodar:
        print('Você ACERTOU! Ganhou 10pts')
        pts += 10
        numero_certo.append(dado)
        rodada.append(cont)
    else:
        print(f'Não foi dessa vez! o numero sorteado foi {rodar}')

    repetir = input('deseja jogar novamente?')
    if repetir not in ('s', 'sim'):

        print(
            f'VOCÊ FEZ {pts} PONTOS !\n Acertou com (o)s numero(s) {numero_certo} \nna(s) rodada(s) {rodada}  !!')
        print(f'OBRIGADO VOLTE SEMPRE!')
        break
