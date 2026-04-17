#Retorna uma lista com informações de um arquivo 
def file_to_list(file_name):

    result = []

    try:
        with open(file_name, "r") as file:
            content = file.readlines()
    except FileNotFoundError:
        print("Arquivo inexistente.")
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return

    if not content:
       print("Arquivo vazio.")
       return
    else:
        for c in content:
            c = c.strip()

            if ":" in c:
                _, values = c.split(":", 1)
                result.append(values)

    return result

# Recebe uma 'lista de listas de strings separada por vírgulas e separa em listas distintas 
# o que é numero do que não é e retorna estas duas listas
def proc_numbers(entrada):

    int_numbers = []
    invalids = []

    for inp in entrada:

        numbers_list = inp.split(",")

        for num in numbers_list:
            num = num.strip()

            if not num:
                continue

            try:
                number = int(num)
                int_numbers.append(number)
            except ValueError:
                invalids.append(num)

    return int_numbers, invalids
    
# Recebe duas listas, uma de números e outra do que não for números, 
# imprimr o maior, o menor e a média dos números da lista numérica,
# imprime os numeros e o que não era números, sem repetições
def show_result(int_numbers, invalids):
    
    if int_numbers:

        #ordenado = list(dict.fromkeys(int_numbers)) >> Aqui mantém a ordem original, removemdo duplicados
        ordenado = sorted(set(int_numbers)) # Aqui remove duplicidades e ordena
        print(f"Números ordenados: {', '.join(map(str, ordenado))}")  
        
        maior = max(int_numbers)
        menor = min(int_numbers)
        media = round(sum(int_numbers) / len(int_numbers), 2)

        print(f"Menor número informado: {menor}")
        print(f"Maior número informado: {maior}")
        print(f"Média dos números informados: {media}")

    else:

        print("Nenhum número válido informado.")

    if invalids:
        print(f"Valores inválidos: {', '.join(list(dict.fromkeys(invalids)))}")
    else:
        print("Nenhum valor inválido informado.")

def main():

    list_numbers = file_to_list("data/ValoresEntrada.txt")

    int_numbers, invalids = proc_numbers(list_numbers)
 #   int_numbers.sort()

    show_result(int_numbers, invalids)

if __name__ == "__main__":
    main()