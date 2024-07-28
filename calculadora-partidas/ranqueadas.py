def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    niveis = [
        (10, "Ferro"),
        (21, "Bronze"),
        (51, "Prata"),
        (81, "Ouro"),
        (91, "Diamante"),
        (101, "Lendário")
    ]

    nivel = "Imortal"  

    for limite, nome_nivel in niveis:
        if vitorias < limite:
            nivel = nome_nivel
            break

    return saldo_vitorias, nivel

vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

saldo_vitorias, nivel = calcular_nivel(vitorias, derrotas)

print(f"O Herói tem um saldo de {saldo_vitorias} e está no nível {nivel}")