from Utente import Utente

def main():
    r = parser("myheart.csv")
    print(r[1].getIdade())
    print(r[1].getSexo())
    print(r[1].getTensao())
    print(r[1].getColestrol())
    print(r[1].getBatimento())
    print(r[1].getTemDoenca())

    dist = doencaPorSexo(r)
    print(dist)

    novo,velho = maisNovoEmaisVelho(r)
    print(novo)
    print(velho)

    dist = doencaPorEscaloes(r)
    print(dist)




def parser(filepath):
    utentes = []
    linha = 2
    with open(filepath, "r") as file:
        next(file) # passar a primeira linha que apenas possúi os nomes das colunas

        for line in file:
            colunas = line.strip().split(',')
            if len(colunas) != 6: return print(f"A linha: {linha} não tem colunas suficientes!")
            idade = colunas[0]
            sexo = colunas[1]
            tensao = colunas[2]
            colestrol = colunas[3]
            batimento = colunas[4]
            temDoenca = colunas[5]
            utente = Utente(idade, sexo,tensao, colestrol, batimento, temDoenca)
            utentes.append(utente)
            linha += 1

    return utentes


def doencaPorSexo(utentes):
    dist = {"Masculino" : 0,
            "Feminino" : 0}
    for utente in utentes:
        if utente.getTemDoenca() == "1":
            if utente.getSexo() == "M":
                dist["Masculino"] += 1
            elif utente.getSexo() == "F":
                dist["Feminino"] += 1

    return dist


def doencaPorEscaloes(utentes):
    novo, velho = maisNovoEmaisVelho(utentes)
    limiteInf = (novo // 5) * 5
    limiteSup = ((velho // 5) + 1) * 5
    print("VELHO")
    print(limiteSup)
    dist = {}
    for i in range(limiteInf, limiteSup, 5):
        dist[(i, i+4)] = set()

    for utente in utentes:
        if utente.getTemDoenca() == "1":

            dist

    return dist


def maisNovoEmaisVelho(utentes):
    tempNovo = int(utentes[0].getIdade())
    tempVelho = int(utentes[0].getIdade())
    for utente in utentes:
        if int(utente.getIdade()) <= tempNovo:
            tempNovo = int(utente.getIdade())
        if int(utente.getIdade()) >= tempVelho:
            tempVelho = int(utente.getIdade())

    return tempNovo, tempVelho



main()

