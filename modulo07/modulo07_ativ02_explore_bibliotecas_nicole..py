'''
Programador: as variáveis serão inseridas no app - BACK-end

Dev: existe interação com o usuário - web design (Front-End)
'''
import utilidades
from datetime import datetime
from faker import Faker

fake = Faker('pt_BR')  # gera dados fictícios em português

# Boas-vindas ao usuário
nome = input('Olá! Qual é o seu nome? ')
print(f'\nSeja bem-vindo(a), {nome}! Vamos usar a calculadora.')

historico = []  # guarda cada operação realizada com data/hora

while True:
    print('\n===== CALCULADORA =====')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Divisão Inteira')
    print('6 - Calcular Média')
    print('7 - Verificar se um número é par')
    print('8 - Ver histórico')
    print('9 - Cadastro')
    print('0 - Sair')

    opcao = input('Escolha uma opção: ')
    agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    if opcao == '0':
        print(f'Encerrando o programa... Até logo, {nome}!')
        break

    elif opcao == '1':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = utilidades.soma(num1, num2)
        print(f'Resultado: {resultado} (calculado em {agora})')
        historico.append(f'[{agora}] Soma({num1}, {num2}) = {resultado}')

    elif opcao == '2':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = utilidades.subtra(num1, num2)
        print(f'Resultado: {resultado} (calculado em {agora})')
        historico.append(f'[{agora}] Subtração({num1}, {num2}) = {resultado}')

    elif opcao == '3':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = utilidades.multiplicar(num1, num2)
        print(f'Resultado: {resultado} (calculado em {agora})')
        historico.append(f'[{agora}] Multiplicação({num1}, {num2}) = {resultado}')

    elif opcao == '4':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = utilidades.divisão(num1, num2)
        print(f'Resultado: {resultado} (calculado em {agora})')
        historico.append(f'[{agora}] Divisão({num1}, {num2}) = {resultado}')

    elif opcao == '5':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = utilidades.divisao_inteira(num1, num2)
        print(f'Resultado: {resultado} (calculado em {agora})')
        historico.append(f'[{agora}] Divisão Inteira({num1}, {num2}) = {resultado}')

    elif opcao == '6':
        quantidade = int(input('Quantos números deseja usar na média? '))
        lista = []
        for i in range(quantidade):
            numero = float(input(f'Digite o número {i + 1}: '))
            lista.append(numero)
        resultado = utilidades.calcular_media(lista)
        print(f'Média: {resultado} (calculado em {agora})')
        historico.append(f'[{agora}] Média({lista}) = {resultado}')

    elif opcao == '7':
        numero = float(input('Digite um número: '))
        resultado = 'par' if utilidades.e_par(numero) else 'ímpar'
        print(f'{numero} é {resultado} (verificado em {agora})')
        historico.append(f'[{agora}] Verificação de paridade({numero}) = {resultado}')

    elif opcao == '8':
        if not historico:
            print('Nenhuma operação realizada ainda.')
        else:
            print('\n--- HISTÓRICO DE OPERAÇÕES ---')
            for item in historico:
                print(item)

    elif opcao == '9':
        usuario_fake = {
            'nome': fake.name(),
            'telefone': fake.phone_number(),
            'email': fake.email(),
            'cidade': fake.city(),
            'data_cadastro': fake.date_time_this_year().strftime('%d/%m/%Y %H:%M:%S')
        }
        print('\n--- CADASTRO REALIZADO ---')
        print(f"Nome: {usuario_fake['nome']}")
        print(f"Telefone: {usuario_fake['telefone']}")
        print(f"E-mail: {usuario_fake['email']}")
        print(f"Cidade: {usuario_fake['cidade']}")
        print(f"Cadastrado em: {usuario_fake['data_cadastro']}")

    else:
        print('Opção inválida! Tente novamente.')