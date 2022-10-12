from random import randint
from time import sleep
lista_num = list()
jogos = list()
print('=' * 30)
print('     PALPITE MEGA SENA')
print('=' * 30)
num_jogos = int(input('Quantidade de jogos a ser sorteado: '))
total = 1
while total <= num_jogos:
    cont = 0
    while True:    
        numero = randint(1,60)
        if numero not in lista_num:
            lista_num.append(numero)
            cont += 1
        if cont >=6:
            break
    lista_num.sort()
    jogos.append(lista_num[:])
    lista_num.clear()
    total += 1    
print(f'Sorteando {num_jogos} jogos:')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(2)