import random

nomes = []

while True:
    print('1 - Inserir nome na lista.')
    print('2 - Sortear.')
    print('3 - Sair do programa.')
         
    opcao = input('Opção desejada: ')

    match opcao:
        case '1':
            nome = input('Imsira o nome: ')
            nomes.append(nome)
            print(f'{nome} inserido com sucesso.')
            continue
        case '2':
            indice_sorteado = random.randint(0, len(nomes)-1)
            print(f'Nome sorteado: {nomes[indice_sorteado]}.')
            continue
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opçao inválida.')
            continue