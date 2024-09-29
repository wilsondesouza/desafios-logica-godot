import random
from time import sleep

class Heroi:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.vida = 100

    def atacar(self):
        ataques = {
            "mago": "usou magia",
            "guerreiro": "usou espada",
            "monge": "usou artes marciais",
            "ninja": "usou shuriken",
            "arqueiro": "usou arco e flecha",
            "cavaleiro": "usou lança",
            "druida": "usou poder da natureza",
        }
        ataque = ataques.get(self.tipo, "usou ataque desconhecido")
        dano = random.randint(10, 20)
        sleep(1)
        print(
            f"O {self.tipo} {self.nome} atacou usando {ataque} e causou {dano} de dano!"
        )
        sleep(1)
        return dano

class Inimigo:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.vida = 50

    def aparecer(self):
        sleep(1)
        print(f"Um {self.tipo} chamado {self.nome} apareceu!")

    def atacar(self):
        dano = random.randint(5, 15)
        sleep(1)
        print(f"{self.nome} atacou e causou {dano} de dano!")
        sleep(1)
        return dano

def batalha(heroi, inimigo):
    sleep(1)
    print(f"\nBatalha entre {heroi.nome} e {inimigo.nome} começou!")

    rodada = 1
    while heroi.vida > 0 and inimigo.vida > 0:
        sleep(1)
        print(f"\nRodada {rodada}")
        sleep(1)
        print(
            f"{heroi.nome}: {heroi.vida} de vida | {inimigo.nome}: {inimigo.vida} de vida"
        )

        # Herói ataca
        dano_heroi = heroi.atacar()
        inimigo.vida -= dano_heroi

        # Verifica se o inimigo foi derrotado
        if inimigo.vida <= 0:
            sleep(1)
            print(f"{inimigo.nome} foi derrotado!")
            break

        # Inimigo ataca
        dano_inimigo = inimigo.atacar()
        heroi.vida -= dano_inimigo

        # Verifica se o herói foi derrotado
        if heroi.vida <= 0:
            sleep(1)
            print(f"{heroi.nome} foi derrotado!")
            break

        rodada += 1

        # Pausa para o usuário acompanhar a batalha
        input("Pressione Enter para a próxima rodada...")
    sleep(1)
    print("\nFim da batalha!")
    quit()

# Criando heróis e inimigos
herois = [
    Heroi("Gandalf", "mago"),
    Heroi("Aragorn", "guerreiro"),
    Heroi("Legolas", "arqueiro"),
    Heroi("Aang", "monge"),
    Heroi("Naruto", "ninja"),
    Heroi("Lancelot", "cavaleiro"),
]

inimigos = [
    Inimigo("Sauron", "Senhor das Trevas"),
    Inimigo("Orc Feio", "Orc"),
    Inimigo("Nazgûl", "Espectro"),
    Inimigo("Ozai", "Senhor do Fogo"),
    Inimigo("Zabuza Momochi", "O demônio do gás oculto"),
    Inimigo("Morgana", "Feiticeira"),
]

# Simulação de várias batalhas
for i in range(3):
    heroi = random.choice(herois)
    inimigo = random.choice(inimigos)
    batalha(heroi, inimigo)

    # Restaura a vida dos personagens para a próxima batalha
    heroi.vida = 100
    inimigo.vida = 50

    if i < 2:  # Se não for a última batalha
        print("\nPreparando próxima batalha...")
        input("Pressione Enter para continuar...")