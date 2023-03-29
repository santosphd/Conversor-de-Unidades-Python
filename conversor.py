# Conversor de Unidades
import os

celsius = 0
fahrenheit = 0
kelvin = 0
metro = 0
milha = 0
polegada = 0
execucao = True
continuar_if = True

print('O que deseja converter?')
opcao_conversao = input('Digite 1 para TEMPERATURA ou digite 2 para DISTÂNCIA ou qualquer tecla para sair: ')
opcao_conversao = int(opcao_conversao)

while execucao == True:

# Condição se a opção for conversão de temperatura
    if opcao_conversao == 1:
        print('1 - Celsius para Fahrenheit')
        print('2 - Celsius para Kelvin')
        print('3 - Fahrenheit para Celsius')
        print('4 - Fahrenheit para Kelvin')
        print('5 - Kelvin para Celsius')
        print('6 - Kelvin para Fahrenheit')
        opcao_conversao_temperatura = int(input('Digite uma das opções: '))
        if opcao_conversao_temperatura == 1:
            celsius = input('Temperatura em Graus Celsius: ')
            celsius = float(celsius)
            fahrenheit = (celsius * (9/5)) + 32
            print(f'{celsius}°C são {fahrenheit}°F')
        elif opcao_conversao_temperatura == 2:
            celsius = input('Temperatura em Graus Celsius: ')
            celsius = float(celsius)
            kelvin = celsius + 273.15
            print(f'{celsius}°C são {kelvin}°K')
        elif opcao_conversao_temperatura == 3:
            fahrenheit = input('Temperatura em Graus Fahrenheit: ')
            fahrenheit = float(fahrenheit)
            celsius = (fahrenheit - 32 ) * (5/9)
            print(f'{fahrenheit}°F são {celsius}°C')
        elif opcao_conversao_temperatura == 4:
            fahrenheit = input('Temperatura em Graus Fahrenheit: ')
            fahrenheit = float(fahrenheit)
            kelvin = (fahrenheit - 32) * (5/9) + 273,15
            print(f'{fahrenheit}°F são {kelvin}°K')
        elif opcao_conversao_temperatura == 5:
            kelvin = input('Temperatura em Graus Kelvin: ')
            kelvin = float(kelvin)
            celsius = (kelvin - 273.15)
            print(f'{kelvin}°K são {celsius}°C')
        elif opcao_conversao_temperatura == 6:
            kelvin = input('Temperatura em Graus Kelvin: ')
            kelvin = float(kelvin)
            fahrenheit = ((kelvin - 273.15) * 9/5) + 32
            print(f'{kelvin}°K são {fahrenheit}°F')
        else:
            os.system('clear')
            print('Digite uma opção válida.')
            continue

# Condição se a opção de conversão for distancia
    elif opcao_conversao == 2:
        print('1 - Metros para Milhas')
        print('2 - Metros para Polegadas')
        print('3 - Milhas para Metros')
        print('4 - Milhas para Polegadas')
        print('5 - Polegadas para Metros')
        print('6 - Polegadas para Milhas')
        opcao_conversao_distancia = int(input('Digite uma das opções: '))
        if opcao_conversao_distancia == 1:
            metro = input('Digite a distância em metros: ')
            metro = float(metro)
            milha = metro / 1609
            print(f'{metro} metros são {milha} milhas')
        elif opcao_conversao_distancia == 2:
            metro = input('Digite a distância em metros: ')
            metro = float(metro)
            polegada = metro * 39.37
            print(f'{metro} metros são {polegada} polegadas')
        elif opcao_conversao_distancia == 3:
            milha = input('Digite a distância em milhas: ')
            milha = float(milha)
            metro = milha * 1609
            print(f'{milha} milhas são {metro} metros')
        elif opcao_conversao_distancia == 4:
            milha = input('Digite a distância em milhas: ')
            milha = float(milha)
            polegada = milha * 63360
            print(f'{milha} milhas são {polegada} polegadas')
        elif opcao_conversao_distancia == 5:
            polegada = input('Digite a distância em polegadas: ')
            polegada = float(polegada)
            metro = polegada / 39.37
            print(f'{polegada} polegadas são {metro} metros')
        elif opcao_conversao_distancia == 6:
            polegada = input('Digite a distância em polegadas: ')
            polegada = float(polegada)
            milha = polegada / 63360
            print(f'{polegada} polegadas são {milha} milhas')
        else:
            os.system('clear')
            print('Digite uma opção válida.')
            continue
    else:
        print('Até a próxima')
        break

# Laço de repetição para a opção de continuar ou não a execução do programa
    while continuar_if == True:
        opcao_continuar = input('Deseja continuar? Digite 1 para SIM  e 2 para NÃO: ')
        opcao_continuar = int(opcao_continuar)
        if opcao_continuar == 1:
            execucao = True
            continuar_if = False
            os.system('clear')
        elif opcao_continuar == 2:
            execucao = False
        else:
            print('Digite uma opção válida')
            continuar_if = True
            
    
        
        
    
    

        

