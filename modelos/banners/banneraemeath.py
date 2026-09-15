from modelos.personagens import aemeath_personagem
import random
from modelos.cincoestrelas import POOL_5_ESTRELAS
from modelos.quatroestrelas import POOL_4_ESTRELAS
from modelos.quatroestrelas import POOL_4_ESTRELAS_PERSONAGENS
from modelos.tresestrelas import POOL_3_ESTRELAS


class BannerAemeath:
    NOME = "Canção Angelical"
    Personagem = aemeath_personagem
    pity = 90
    custo = 160

    @staticmethod
    def pull_aemeath(player):
        while True:
            print(f"Gemas: {player.gemas}")
            print("Banner da Aemeath\nO que deseja fazer?")
            print("\n1 --> 1 pull")
            print("2 --> 10 pulls")
            print("0 --> Sair")
            escolha = int(input("Digite qual opção você deseja --> "))
            if escolha == 1:
                BannerAemeath.dar_pull(player)
            elif escolha == 2:
                BannerAemeath.dar_10_pulls(player)
            elif escolha == 0:
                break
                
    @staticmethod
    def pull_5_estrelas(player):
        if player.cinquentacinquenta:
            decidir = random.random()*100
            if decidir>49:
                item = aemeath_personagem
                player.pity = 0
                player.cinquentacinquenta = True
            else:
                item = random.choice(POOL_5_ESTRELAS)
                player.pity = 0
                player.cinquentacinquenta = False
        else:
            item = aemeath_personagem
            player.pity = 0
            player.cinquentacinquenta = True

        return item

    @staticmethod
    def pull_4_estrelas(player):
        decidir = random.random()*100
        if decidir>49:
            item = random.choice(POOL_4_ESTRELAS_PERSONAGENS)
            player.pity4estrelas = 0
        else:
            item = random.choice(POOL_4_ESTRELAS)
            player.pity4estrelas = 0
        return item

    @staticmethod
    def dar_pull(player):
        if player.gemas < 160:
            print("Você não possui gemas o suficiente!")
            return
        sorteado = random.random() *100
        player.gemas -= 160
        player.pity+=1
        if player.pity >= 40 and player.pity < 67 and player.pity < 90:
            if sorteado <= 1.2:
                item = BannerAemeath.pull_5_estrelas(player)
            elif sorteado <=2.4 or player.pity4estrelas >= 10:
                item = BannerAemeath.pull_4_estrelas(player)
            else:
                item = random.choice(POOL_3_ESTRELAS)

        elif player.pity >=67:
            if sorteado <= 2:
                item = BannerAemeath.pull_5_estrelas(player)
            elif sorteado <=2.4 or player.pity4estrelas >= 10:
                item = BannerAemeath.pull_4_estrelas(player)
            else:
                item = random.choice(POOL_3_ESTRELAS)

        elif player.pity >= 90:
            item = BannerAemeath.pull_5_estrelas(player)
        else:
            if sorteado <= 1:
                item = BannerAemeath.pull_5_estrelas(player)
            elif sorteado <=2.4 or player.pity4estrelas >= 10:
                item = BannerAemeath.pull_4_estrelas(player)
            else:
                item = random.choice(POOL_3_ESTRELAS)
        player.itens[item] = ""

    @staticmethod
    def dar_10_pulls(player):
        if player.gemas < 1600:
            print("Você não possui gemas o suficiente!")
            return
        for _ in range(10):
            BannerAemeath.dar_pull(player)

