import csv

class Pessoa:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = int(idade)
        self.salario = self.tratar_salario(salario)

    def __repr__(self):
        return f"{self.nome} - {self.idade} anos - R$ {self.salario} \n"

    def tratar_salario(self, salario):
        try:
            return int(str(salario).strip())
        except (ValueError, TypeError):
            return 0

# Lê um csv com dados (idade e salario) de pessoas e retorna uma 
# lista de pessoas
def processa_csv(caminho_arquivo):

    pessoas = []

    try:
        with open(caminho_arquivo, newline = "", encoding = "latin-1") as f:
            dados = list(csv.DictReader(f, delimiter=";"))
    except FileNotFoundError:
        print("Arquivo inexistente.")
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return

    if not dados:
        print("Arquivo vazio.")
        return
    else:
        for linha in dados:
            p = Pessoa (
                linha["nome"], linha["idade"], linha["salario"]
            )
            pessoas.append(p)

    return pessoas

# calcula media salarial das pessoas da lista
def calcula_media_salarial(entrada):

    if not entrada:
        return 0

    return round(sum(p.salario for p in entrada) / len(entrada), 2)

# retona uma lista das pessoas com salários acima da media
def salarios_acima_media(entrada):

    media = calcula_media_salarial(entrada)

    #for p in entrada:
    #    if p.salario > media:
    #        pessoas.append(p)

    pessoas = [p for p in entrada if p.salario > media]

    return pessoas

#grava num csv as pessoas que tem salario acima da media
def grava_pessoas_sal_acima_media(pessoas, arquivo_saida):

    pessoas_acima_media = salarios_acima_media(pessoas)

    with open(arquivo_saida, "w", newline="", encoding="utf-8") as f:
        campos = ["nome", "idade", "salario"]
        writer = csv.DictWriter(f, fieldnames=campos)

        writer.writeheader()

        for p in pessoas_acima_media:
            writer.writerow({
                "nome": p.nome, "idade": p.idade, "salario": p.salario
            })

def main():
    pessoas = processa_csv("data/dados.csv")

    if not pessoas:
        print("Nenhuma pessoa carregada.")
        return

    pessoas_ordenadas =  sorted(pessoas, key=lambda p: p.salario)
    print(f"Pessoas ordenadas pelo salário: {pessoas_ordenadas}")

    print(f"Média salarial: {calcula_media_salarial(pessoas)}")
    print(f"Pessoas com salários acima da média: {salarios_acima_media(pessoas)}")

    grava_pessoas_sal_acima_media(pessoas, "data/dados_saida.csv")

if __name__ == "__main__":
    main()