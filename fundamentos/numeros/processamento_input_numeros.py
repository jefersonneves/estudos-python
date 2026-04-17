#Function que processa uma lista de entrada, separa o que é numero para retornar numa lista de números
# e noutra lista retorna o que não for número
def processar_numeros(numeros_lista):
    numeros_int = []
    invalidos = []

    for x in numeros_lista:
        x = x.strip()

        if not x:
            continue

        try:
            numero = int(x)
            numeros_int.append(numero)
        except ValueError:
            invalidos.append(x)

    return numeros_int, invalidos

#Function que recebe duas listas, uma de números e outra do que não for números, 
# imprimr o maior, o menor e a média dos números da lista numérica e imprime o que não era números
def mostrar_resultado(numeros_int, invalidos):
    if numeros_int:
        #print(f"Números ordenados: {numeros_int}") < Vai imprimir a lista 'crua', assim: [1, 2, 3]
        
        #Temos numeros_int = [1, 2, 3] e o join só funciona com strings, não com números.
        #Temos que mudar de [1, 2, 3] para ["1", "2", "3"], e o map(str, [1, 2, 3]) faz isso.
        print(f"Números ordenados: {', '.join(map(str, numeros_int))}")  
        # [str(x) for x in numeros_int] << Isso faz a mesma coisa que a linha acima, assim como:
        #lista_str = []
        #for x in numeros_int:
        #    lista_str.append(str(x))
        # faz a mesma coisa tbm

        print(f"Menor número informado: {min(numeros_int)}")
        print(f"Maior número informado: {max(numeros_int)}")
        print(f"Média dos números informados: {round(sum(numeros_int)/len(numeros_int), 2)}")
    else:
        print("Nenhum número válido informado")

    if invalidos:
        print(f"Valores inválidos: {', '.join(invalidos)}")
    else:
        print("Nenhum valor inválido informado.")

def main():
   numeros = input("Digite alguns números separados por vírgulas:") 

   if not numeros.strip():
       print("Nenhum número informado.")
       return
   
   numeros_lista = numeros.split(",")
   
   numeros_int, invalidos = processar_numeros(numeros_lista)
   numeros_int.sort()

   mostrar_resultado(numeros_int, invalidos)

if __name__ == "__main__":
    main()