def determinar_nivel(xp):

    niveis = {
        (0, 1000): "Ferro",
        (1001, 2000): "Bronze",
        (2001, 5000): "Prata",
        (5001, 7000): "Ouro",
        (7001, 8000): "Platina",
        (8001, 9000): "Ascendente",
        (9001, 10000): "Imortal",
    }

    for intervalo, nivel in niveis.items():
        if intervalo[0] <= xp <= intervalo[1]:
            return nivel

    return "Radiante"

nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de XP do herói: "))

nivel = determinar_nivel(xp)

print(f"O Herói de nome {nome} está no nível de {nivel}")