from time import sleep
def main():

    tentativa = 3
    level = 1
    xp = 0
    sleep(0.5)
    print(f"Nome ⇾ {usuario}")
    sleep(0.5)
    print(f'Nível ⇾ {level}')
    sleep(0.5)
    print(f'XP ⇾ {xp}')
    sleep(0.5)
    print('-' * 30)
    print("Olá usuário(a). Bem vindo(a) ao QUIZ.")
    print('-' * 30)
    sleep(0.6)

usuario = input("Informe seu nome: ").strip().capitalize()

main()

def continuacao(cont):
  if cont == 'S':
      pass
  else:
      print("FIM!")
      quit()
sleep(0.7)
continuaçao=input("Deseja continuar? [S/N] ").strip().upper()[0]

continuacao(continuaçao)

def rules(r):
  erro = False
  while not erro:
    if r == '0':
      sleep(0.7)
      print('-'*30)
      print("-O usuário irá escolher um tema de sua preferência, com isso, será feito algumas perguntas sobre o tema.")
      print('-'*30)
      sleep(0.7)
      print("-Cada pergunta que o usuário acertar, ganhará uma quantia de xp.")
      print('-'*30)
      sleep(0.7)
      print("-À medida que o usuário acertar as perguntas, será acumulado o xp.")
      print('-'*30)
      sleep(0.7)
      print("-Caso o usuário erre a resposta, terá 3 tentativas.")
      print('-'*30)
      sleep(0.7)
      print("-Se as tentativas se esgotarem e o usuário voltar a errar, o XP irá zerar.")
      print('-'*30)
      erro = True
    else:
      sleep(0.7)
      print("Número incorreto! Digite novamente.")
      sleep(0.7)
      regras=input("Digite '0' para ver as regras: ").strip()
      if regras == '0':
       sleep(0.7)
       print('-'*30)
       print("-O usuário irá escolher um tema de sua preferência, com isso, será feito algumas perguntas sobre o tema.")
       print('-'*30)
       sleep(0.7)
       print("-Cada pergunta que o usuário acertar, ganhará uma quantia de xp.")
       print('-'*30)
       sleep(0.7)
       print("-À medida que o usuário acertar as perguntas, será acumulado o xp.")
       print('-'*30)
       sleep(0.7)
       print("-Com o xp o usuário poderá desbloquear novos níveis de perguntas: Fácil, Médio e Difícil.")
       print('-'*30)
       sleep(0.7)
       print("-Caso o usuário erre a resposta, terá 3 tentativas.")
       print('-'*30)
       sleep(0.7)
       print("-Se as tentativas se esgotarem e o usuário voltar a errar, o XP irá zerar e o usuário perde.")
       print('-'*30)
       erro = True

regras = (input(("Digite '0' para ver as regras: "))).strip()

rules(regras)


def perguntas(t):
    if t == '1':
        sleep(0.6)
        altG1 = "1)O maior oceano da Terra é o... \na) Oceano Pacífico \nb) Oceano Atlântico \nc) Oceano Índico \nd) Oceano Glacial Antártico"
        pGeo1 = {altG1: 'A'}

        print(altG1)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pGeo1[altG1]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativa >= 1:
                    sleep(0.6)
                    dnv = input('Quer tentar novamente? (Isso custará uma tentativa) [S/N] ').strip().upper()[0]
                    if dnv == 'S':
                        tentativa -= 1
                        sleep(0.6)
                        altG1 = "1)O maior oceano da Terra é o... \na) Oceano Pacífico \nb) Oceano Atlântico \nc) Oceano Índico \nd) Oceano Glacial Antártico"
                        pGeo1 = {altG1: 'A'}

                        print(altG1)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()
                        if escolha == pGeo1[altG1]:
                            sleep(0.6)
                            print('Resposta correta.')
                            break
                        else:
                            sleep(0.6)
                            print('Resposta incorreta.')

                    else:
                        sleep(0.6)
                        break
                else:
                    sleep(0.6)
                    print('Suas tentativas esgostaram.')
                    break

        sleep(0.6)
        altG2 = "2)Em que continente está localizado o Catar? \na) África \nb) Ásia \nc) Oceania \nd) América do Sul"
        pGeo2 = {altG2: 'B'}

        print(altG2)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == pGeo2[altG2]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativa >= 1:
                    sleep(0.6)
                    dnv = input('Quer tentar novamente? (Isso custará uma tentativa) [S/N] ').strip().upper()[0]
                    if dnv == 'S':
                        tentativa -= 1
                        sleep(0.6)
                        altG2 = "2)Em que continente está localizado o Catar? \na) África \nb) Ásia \nc) Oceania \nd) América do Sul"
                        pGeo2 = {altG2: 'B'}

                        print(altG2)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()
                        if escolha == pGeo2[altG2]:
                            sleep(0.6)
                            print('Resposta correta.')
                            break
                        else:
                            sleep(0.6)
                            print('Resposta incorreta.')

                    else:
                        sleep(0.6)
                        break

                else:
                    sleep(0.6)
                    print('Suas tentativas esgostaram.')
                    break



print("\033[1;94m                            NÍVEL 1!\033[1;97m")
temas=["[1] ⇾  Geografia", "[2] ⇾  História", "[3] ⇾  Ciências", "[4] ⇾  Matemática", "[5] ⇾  Gramática", "[6] ⇾  Futebol"]
for i in temas:
    print(i)
tema = input(f"Olá, \033[1;95m{usuario}\033[0;0m. Informe o número correspondente ao tema: ")
perguntas(tema)


