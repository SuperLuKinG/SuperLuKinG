import time
usuario = input("Informe seu nome: ").strip().capitalize()
tentativas = 3
level = 1
xp = 0
time.sleep(0.5)
print(f"Nome ⇾ {usuario}")
time.sleep(0.5)
print(f'Nível ⇾ {level}')
time.sleep(0.5)
print(f'XP ⇾ {xp}')
time.sleep(0.5)
time.sleep(0.5)

def continuacao(cont):
  if cont == 'S':
      pass
  else:
      print("FIM!")
      quit()
time.sleep(1)
continuaçao=input("Deseja continuar? [S/N] ").strip().upper()[0]
continuacao(continuaçao)

def rules(r):
  erro=False
  while not erro:
    if r == '0':
      time.sleep(0.7)
      print('-'*30)
      print("-O usuário irá escolher um tema de sua preferência, com isso, será feito algumas perguntas sobre o tema.")
      print('-'*30)
      time.sleep(0.7)
      print("-Cada pergunta que o usuário acertar, ganhará uma quantia de xp.")
      print('-'*30)
      time.sleep(0.7)
      print("-À medida que o usuário acertar as perguntas, será acumulado o xp.")
      print('-'*30)
      time.sleep(0.7)
      print("-Caso o usuário erre a resposta, terá 3 tentativas.")
      print('-'*30)
      time.sleep(0.7)
      print("-Se as tentativas se esgotarem e o usuário voltar a errar, o XP irá zerar.")
      print('-'*30)
      erro = True
    else:
      time.sleep(0.7)
      print("Número incorreto! Digite novamente.")
      time.sleep(0.7)
      regras=input("Digite '0' para ver as regras: ").strip()
      if regras == '0':
       time.sleep(0.7)
       print('-'*30)
       print("-O usuário irá escolher um tema de sua preferência, com isso, será feito algumas perguntas sobre o tema.")
       print('-'*30)
       time.sleep(0.7)
       print("-Cada pergunta que o usuário acertar, ganhará uma quantia de xp.")
       print('-'*30)
       time.sleep(0.7)
       print("-À medida que o usuário acertar as perguntas, será acumulado o xp.")
       print('-'*30)
       time.sleep(0.7)
       print("-Com o xp o usuário poderá desbloquear novos níveis de perguntas: Fácil, Médio e Difícil.")
       print('-'*30)
       time.sleep(0.7)
       print("-Caso o usuário erre a resposta, terá 3 tentativas.")
       print('-'*30)
       time.sleep(0.7)
       print("-Se as tentativas se esgotarem e o usuário voltar a errar, o XP irá zerar.")
       print('-'*30)
       erro = True

print('-'*30)
print('-'*30)
print("Olá usuário(a). Bem vindo(a) ao QUIZ.")
print('-'*30)
print('-'*30)
time.sleep(0.6)

regras=(input(("Digite '0' para ver as regras: "))).strip()

rules(regras)

def temasEasy(t):
    if t == '1':
        print("Você escolheu Geografia!")
        time.sleep(0.6)
        altG = ["1)O maior oceano da Terra é o...", "a) Oceano Pacífico", "b) Oceano Atlântico", "c) Oceano Índico",
                "d) Oceano Glacial Antártico", ]
        for a in altG:
            time.sleep(0.6)
            print(a)
        escolha = input("Qual a alternativa? ")
        if escolha == 'a' or escolha == 'A':
            xp =+ 10
            time.sleep(0.8)
            print("Resposta correta.")
        else:
            falha = False
            time.sleep(0.8)
            print("Resposta incorreta.")
            while not falha:
                dnv = input("Quer tentar de novo? (Isso irá te custar uma tentativa)[S/N] ")
                if dnv == 'S' or dnv == 's':
                    tentativa =- 1
                    time.sleep(0.6)
                    altG = ["1)O maior oceano da Terra é o...", "a) Oceano Pacífico", "b) Oceano Atlântico",
                        "c) Oceano Índico",
                        "d) Oceano Glacial Antártico", ]
                    for a in altG:
                        time.sleep(0.8)
                        print(a)
                    escolha = input("Qual a alternativa? ")
                    if escolha == 'a' or escolha == 'A':
                        xp = + 10
                        time.sleep(0.8)
                        print("Resposta correta.")
                        time.sleep(0.8)
                    else:
                        print("Resposta incorreta.")
                else:
                    falha = True


    elif t == '2':
      print()
      perguntas2 = {}
    elif t == '3':
      print()
      perguntas3 = {}
    elif t == '4':
      print()
      perguntas4 = {}
    elif t == '5':
      print()
      perguntas5 = {}
    elif t == '6':
      print()
      perguntas6 = {}
    else:
        print("Dígito incorreto. Tente novamente.")


print("\033[1;94m                            NÍVEL 1!\033[1;97m")
temas=["[1] ⇾  Geografia", "[2] ⇾  História", "[3] ⇾  Ciências", "[4] ⇾  Matemática", "[5] ⇾  Gramática", "[6] ⇾  Futebol"]
for i in temas:
    print(i)
tema = input(f"Olá, \033[1;95m{usuario}\033[0;0m. Informe o número correspondente ao tema: ")
temasEasy(tema)


