import os
from collections import Counter
from leituraDados import load_data
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def group_by_tens(number):
    if number == 60:
        return 50
    return (number // 10) * 10

def process_data_general(data):
    numeros = [num for row in data for num in row]
    counter = Counter(numeros)
    sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    clear_screen()
    print("Números mais sorteados:\n")
    print(f'{"Ranking":<10}{"Número":<10}{"Frequência":<10}')
    for i, (num, freq) in enumerate(sorted_counter, start=1):
        print(f'{i:<10}{num:<10}{freq:<10}')
    return input("\nPressione ENTER para voltar ao menu ou digite 'sair' para encerrar o programa: ")

def process_data_by_tens(data):
    numeros = [num for row in data for num in row]
    counter = Counter(numeros)
    
    # Agrupando os números de acordo com as casas das dezenas
    grouped_by_tens = {}
    for num, freq in counter.items():
        tens = group_by_tens(num)
        if tens not in grouped_by_tens:
            grouped_by_tens[tens] = []
        grouped_by_tens[tens].append((num, freq))

    # Ordenando e exibindo os números mais sorteados nas casas das dezenas em ordem crescente
    clear_screen()
    for tens, numbers in sorted(grouped_by_tens.items(), key=lambda x: x[0]):
        sorted_numbers = sorted(numbers, key=lambda x: x[1], reverse=True)
        print(f"\nCasas das dezenas: {tens}-{tens+9}\n")
        print(f'{"Número":<10}{"Frequência":<10}')
        for num, freq in sorted_numbers:
            if tens <= num <= tens + 9 or (tens == 50 and num == 60):
                print(f'{num:<10}{freq:<10}')
    return input("\nPressione ENTER para voltar ao menu ou digite 'sair' para encerrar o programa: ")

def process_data_odd(data):
    numeros = [num for row in data for num in row if num % 2 != 0]
    counter = Counter(numeros)
    sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    clear_screen()
    print("Números ímpares mais sorteados:\n")
    print(f'{"Ranking":<10}{"Número":<10}{"Frequência":<10}')
    for i, (num, freq) in enumerate(sorted_counter, start=1):
        print(f'{i:<10}{num:<10}{freq:<10}')
    return input("\nPressione ENTER para voltar ao menu ou digite 'sair' para encerrar o programa: ")

def process_data_even(data):
    numeros = [num for row in data for num in row if num % 2 == 0]
    counter = Counter(numeros)
    sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    clear_screen()
    print("Números pares mais sorteados:\n")
    print(f'{"Ranking":<10}{"Número":<10}{"Frequência":<10}')
    for i, (num, freq) in enumerate(sorted_counter, start=1):
        print(f'{i:<10}{num:<10}{freq:<10}')
    return input("\nPressione ENTER para voltar ao menu ou digite 'sair' para encerrar o programa: ")

def count_odd_numbers(data):
    clear_screen()
    numeros = [num for row in data for num in row if num % 2 != 0]
    return len(numeros)

def count_even_numbers(data):
    numeros = [num for row in data for num in row if num % 2 == 0]
    return len(numeros)

def get_most_common_general(data):
    numeros = [num for row in data for num in row]
    counter = Counter(numeros)
    sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return [num for num, freq in sorted_counter[:6]]

def get_most_common_by_tens(data):
    numeros = [num for row in data for num in row]
    counter = Counter(numeros)
    
    grouped_by_tens = {}
    for num, freq in counter.items():
        tens = group_by_tens(num)
        if tens not in grouped_by_tens:
            grouped_by_tens[tens] = []
        grouped_by_tens[tens].append((num, freq))

    most_common_numbers = []
    for tens, numbers in sorted(grouped_by_tens.items(), key=lambda x: x[0]):
        sorted_numbers = sorted(numbers, key=lambda x: x[1], reverse=True)
        most_common_numbers.extend(num for num, freq in sorted_numbers[:6])
    return most_common_numbers

def get_most_common_odd(data):
    numeros = [num for row in data for num in row if num % 2 != 0]
    counter = Counter(numeros)
    sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return [num for num, freq in sorted_counter[:6]]

def get_most_common_even(data):
    numeros = [num for row in data for num in row if num % 2 == 0]
    counter = Counter(numeros)
    sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return [num for num, freq in sorted_counter[:6]]

def generate_most_likely_numbers(data):
    # Get the most drawn numbers in general
    most_drawn_general = get_most_common_general(data)
    # Get the most drawn numbers by tens
    most_drawn_by_tens = get_most_common_by_tens(data)
    # Get the most drawn odd numbers
    most_drawn_odd = get_most_common_odd(data)
    # Get the most drawn even numbers
    most_drawn_even = get_most_common_even(data)

    # Combine all the statistics
    all_statistics = most_drawn_general + most_drawn_by_tens + most_drawn_odd + most_drawn_even

    # Count the frequency of each number
    counter = Counter(all_statistics)

    # Get the 6 most common numbers
    most_common_numbers = [num for num, freq in counter.most_common(6)]

    return most_common_numbers

def check_user_numbers(data):
    while True:
        clear_screen()
        user_numbers = set(map(int, input("Digite 6 números separados por espaço: ").split()))

        # Inicializando contadores
        sena, quina, quadra, trinca, dois, um, zero = 0, 0, 0, 0, 0, 0, 0

        for row in data:
            matches = len(user_numbers & set(row))  # Conta o número de acertos
            if matches == 6:
                sena += 1
            elif matches == 5:
                quina += 1
            elif matches == 4:
                quadra += 1
            elif matches == 3:
                trinca += 1
            elif matches == 2:
                dois += 1
            elif matches == 1:
                um += 1
            else:
                zero += 1

        # Imprimindo os resultados
        print(f"\n6. acertos: {sena}")
        print(f"5. acertos: {quina}")
        print(f"4. acertos: {quadra}")
        print(f"3. acertos: {trinca}")
        print(f"2. acertos: {dois}")
        print(f"1. acerto: {um}")
        print(f"0. acertos: {zero}")

        choice = input("\nDigite 's' para escolher mais 6 números ou qualquer outra tecla para voltar ao menu principal: ")
        if choice.lower() != 's':
            break

def sorteio_mega_sena(user_numbers):
    # Gera 6 números aleatórios entre 1 e 60
    sorteio = set(random.sample(range(1, 61), 6))

    # Compara os números sorteados com os números escolhidos pelo usuário
    acertos = len(user_numbers & sorteio)

    # Imprime os números sorteados e a quantidade de acertos
    print(f"\nNúmeros sorteados: {sorted(sorteio)}")
    print(f"\nVocê acertou {acertos} número(s)!")
    
def main():
    file_name = 'MegaSenaGeral.xlsx'
    sheet_name = 'tabelaMegaSena'
    start_row = 8
    end_row = 2675
    start_col = 3
    end_col = 8

    # Chamando a função de carregamento de dados de main.py
    data_loaded = load_data(file_name, sheet_name, start_row, end_row, start_col, end_col)

    while True:
        # Menu de seleção
        clear_screen()
        print("\nEscolha uma opção:\n")
        print("1 - Ver números mais sorteados")
        print("2 - Ver números mais sorteados separados pelas dezenas")
        print("3 - Ver números ímpares mais sorteados")
        print("4 - Ver números pares mais sorteados")
        print("5 - Ver quantidade de números ímpares e pares sorteados")
        print("6 - Gerar os 6 números mais prováveis de serem sorteados")
        print("7 - Verificar se seus números já foram sorteados")
        print("8 - Efetuar um sorteio da Mega Sena")
        print("9 - Encerrar o programa")
        choice = input("\nDigite o número da opção desejada: ")

        if choice == '1':
            return_to_menu = process_data_general(data_loaded)
            if return_to_menu.lower() == 'sair':
                break
        elif choice == '2':
            return_to_menu = process_data_by_tens(data_loaded)
            if return_to_menu.lower() == 'sair':
                break
        elif choice == '3':
            return_to_menu = process_data_odd(data_loaded)
            if return_to_menu.lower() == 'sair':
                break
        elif choice == '4':
            return_to_menu = process_data_even(data_loaded)
            if return_to_menu.lower() == 'sair':
                break
        elif choice == '5':
            odd_count = count_odd_numbers(data_loaded)
            even_count = count_even_numbers(data_loaded)
            print(f'Quantidade de números ímpares sorteados: {odd_count}')
            print(f'Quantidade de números pares sorteados: {even_count}')
            input("\nPressione ENTER para voltar ao menu ou digite 'sair' para encerrar o programa: ")
        elif choice == '6':
            most_likely_numbers = generate_most_likely_numbers(data_loaded)
            clear_screen()
            print(f'Os 6 números mais prováveis de serem sorteados são: {most_likely_numbers}')
            input("\nPressione ENTER para voltar ao menu ou digite 'sair' para encerrar o programa: ")
        elif choice == '7':
            clear_screen()
            check_user_numbers(data_loaded)
            input("\nPressione ENTER para voltar ao menu ou digite 'sair' para encerrar o programa: ") 
        elif choice == '8':
             clear_screen()
             user_numbers = set(map(int, input("Digite 6 números separados por espaço: ").split()))
             sorteio_mega_sena(user_numbers)
             input("\nPressione ENTER para voltar ao menu ou digite 'sair' para encerrar o programa: ")
        elif choice == '9':
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3, 4, 5, 6, 7 ou 8.")

if __name__ == "__main__":
    main()