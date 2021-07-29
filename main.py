from time import sleep

def funçao():
    for i in l:
        print(i)
        sleep(0.6)
l = ['-' * 30]
funçao()

def continuacao(cont):
  if cont == 'S':
      pass
  else:
      print("FIM!")
      quit()
sleep(0.6)
print("Olá usuário(a). Bem vindo(a) ao QUIZ.")

funçao()

continuaçao = input("Deseja continuar? [S/N] ").strip().upper()[0]
sleep(0.6)

continuacao(continuaçao)


def rules(r):
  erro = False
  while not erro:
    if r == '0':
          funçao()
          print("-O usuário irá escolher um tema de sua preferência, com isso, será feito algumas perguntas sobre o tema.")
          funçao()
          print("-Caso o usuário erre a resposta, terá 3 tentativas.")
          funçao()
          print("-Se as tentativas se esgotarem e o usuário voltar a errar, o usuário perde.")
          funçao()
          erro = True
    else:
      sleep(0.6)
      print("Número incorreto! Digite novamente.")
      sleep(0.6)
      regras=input("Digite '0' para ver as regras: ").strip()
      if regras == '0':
           funçao()
           print("-O usuário irá escolher um tema de sua preferência, com isso, será feito algumas perguntas sobre o tema.")
           funçao()
           print("-Caso o usuário erre a resposta, terá 3 tentativas.")
           funçao()
           print("-Se as tentativas se esgotarem e o usuário voltar a errar, o usuário perde.")
           funçao()
           erro = True

regras = (input(("Digite '0' para ver as regras: "))).strip()

rules(regras)



def perguntas(t):
    tentativas = 3
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
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()[0]
                    if dnv == 'S':
                        tentativas -= 1
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
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas})  [S/N] ').strip().upper()[0]
                    if dnv == 'S':
                        tentativas -= 1
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

        sleep(0.6)
        altG3 = "3)O que significa extrativismo? \na) utilizar processos de escavação para a coleta e estudo de fósseis \nb) estudo da estrutura externa de um ser vivo \nc) processo que investiga a existência de extraterrestres \nd) extrair da natureza produtos para fins comerciais ou industriais"
        pGeo3 = {altG3: 'D'}

        print(altG3)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pGeo3[altG3]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[0]

                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altG3 = "3)O que significa extrativismo? \na) utilizar processos de escavação para a coleta e estudo de fósseis \nb) estudo da estrutura externa de um ser vivo \nc) processo que investiga a existência de extraterrestres \nd) extrair da natureza produtos para fins comerciais ou industriais"
                        pGeo3 = {altG3: 'D'}

                        print(altG3)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()
                        if escolha == pGeo3[altG3]:
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
        altG4 = "4)Qual dos países abaixo não está localizado no continente africano? \na) Angola \nb) Tunísia \nc) Togo \nd) Armênia"
        pGeo4 = {altG4: 'D'}

        print(altG4)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pGeo4[altG4]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altG4 = "4)Qual dos países abaixo não está localizado no continente africano? \na) Angola \nb) Tunísia \nc) Togo \nd) Armênia"
                        pGeo4 = {altG4: 'D'}

                        print(altG4)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()
                        if escolha == pGeo4[altG4]:
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

    elif t == '2':
        sleep(0.6)
        altH1 = "1)Entre as características do Período Neolítico, destaca-se: \na) Sedentarismo e o início da agricultura. \nb) A produção do fogo \nc) O nomadismo \nd) A invenção do arco e da flecha."
        pHist1 = {altH1: 'A'}

        print(altH1)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pHist1[altH1]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altH1 = "1)Entre as características do Período Neolítico, destaca-se: \na) Sedentarismo e o início da agricultura. \nb) A produção do fogo \nc) O nomadismo \nd) A invenção do arco e da flecha."
                        pHist1 = {altH1: 'A'}

                        print(altH1)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pHist1[altH1]:
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
                    print('Suas tentativas esgotaram.')
                    break



        sleep(0.6)
        altH2 = "2)Em que ano foi assinada a Lei Áurea no Brasil? \na) 1889 \nb) 1888 \nc) 1788 \nd) 1876."
        pHist2 = {altH2: 'B'}

        print(altH2)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pHist2[altH2]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altH2 = "2)Em que ano foi assinada a Lei Áurea no Brasil? \na) 1889 \nb) 1888 \nc) 1788 \nd) 1876."
                        pHist2 = {altH2: 'B'}

                        print(altH2)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pHist2[altH2]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altH3 = "3) A denominação científica do homem moderno é: \na) Homo sapiens sapiens \nb) Homo ergaster \nc) Homo erectus \nd) Homem de Neandertal"
        pHist3 = {altH3: 'A'}

        print(altH3)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pHist3[altH3]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altH3 = "3) A denominação científica do homem moderno é: \na) Homo sapiens sapiens \nb) Homo ergaster \nc) Homo erectus \nd) Homem de Neandertal"
                        pHist3 = {altH3: 'A'}

                        print(altH3)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pHist3[altH3]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altH4 = "4) Quem descobriu a América? \na) Cristóvão Colombo \nb) Pedro Alvares Cabral \nc) Vasco da Gama \nd) Marco Polo"
        pHist4 = {altH4: 'A'}

        print(altH4)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pHist4[altH4]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altH4 = "4) Quem descobriu a América? \na) Cristóvão Colombo \nb) Pedro Alvares Cabral \nc) Vasco da Gama \nd) Marco Polo"
                        pHist4 = {altH4: 'A'}

                        print(altH4)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pHist4[altH4]:
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
                    print('Suas tentativas esgotaram.')
                    break

    elif t == '3':
        sleep(0.6)
        altC1 = "1)Qual dos animais abaixo não é uma ave? \na) avestruz \nb) ema \nc) coruja \nd) craca"
        pCien1 = {altC1: 'D'}

        print(altC1)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pCien1[altC1]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativa >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativa -= 1
                        sleep(0.6)
                        altC1 = "1)Qual dos animais abaixo não é uma ave? \na) avestruz \nb) ema \nc) coruja \nd) craca"
                        pCien1 = {altC1: 'D'}

                        print(altC1)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pCien1[altC1]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altC2 = "2)Metabolismo é o... \na) conjunto de transformações que as substâncias químicas sofrem no interior dos organismos vivos \nb) exercício da inteligência humana através de testes de raciocínio \nc) processo que pode levar à atrofia da mandíbula de um indivíduo \nd) uso de substâncias para aumentar a performance de atletas de alto nível"
        pCien2 = {altC2: 'A'}

        print(altC2)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pCien2[altC2]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altC2 = "2)Metabolismo é o... \na) conjunto de transformações que as substâncias químicas sofrem no interior dos organismos vivos \nb) exercício da inteligência humana através de testes de raciocínio \nc) processo que pode levar à atrofia da mandíbula de um indivíduo \nd) uso de substâncias para aumentar a performance de atletas de alto nível"
                        pCien2 = {altC2: 'A'}

                        print(altC2)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pCien2[altC2]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altC3 = "3)Os anfíbios são animais que... \na) são caracterizados pela presença de glândulas mamárias  \nb) possuem bicos e penas \nc) vivem apenas em ambiente aquático \nd) podem viver tanto em terra como na água"
        pCien3 = {altC3: 'D'}

        print(altC3)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pCien3[altC3]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altC3 = "3)Os anfíbios são animais que... \na) são caracterizados pela presença de glândulas mamárias  \nb) possuem bicos e penas \nc) vivem apenas em ambiente aquático \nd) podem viver tanto em terra como na água"
                        pCien3 = {altC3: 'D'}

                        print(altC3)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pCien3[altC3]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altC4 = "4)Qual dos animais abaixo não é um crustáceo? \na) camarão \nb) siri \nc) congro \nd) lagosta"
        pCien4 = {altC4: 'C'}

        print(altC4)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pCien4[altC4]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altC4 = "4)Qual dos animais abaixo não é um crustáceo? \na) camarão \nb) siri \nc) congro \nd) lagosta"
                        pCien4 = {altC4: 'C'}

                        print(altC4)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pCien4[altC4]:
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
                    print('Suas tentativas esgotaram.')
                    break
    elif t == '4':
        sleep(0.6)
        altM1 = "1)Em Matemática, arredondar significa: \na) transformar um quadrado em círculo \nb) transformar um círculo em uma elipse \nc) multiplicar um número pelo seu sucessor \nd) fazer uma aproximação do valor de um número"
        pMat1 = {altM1: 'D'}

        print(altM1)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pMat1[altM1]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altM1 = "1)Em Matemática, arredondar significa: \na) transformar um quadrado em círculo \nb) transformar um círculo em uma elipse \nc) multiplicar um número pelo seu sucessor \nd) fazer uma aproximação do valor de um número"
                        pMat1 = {altM1: 'D'}

                        print(altM1)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pMat1[altM1]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altM2 = "2)Quantos centímetros existem em 5 metros? \na) 500 cm \nb) 5000 cm \nc) 0,5 cm \nd) 0,05 cm"
        pMat2 = {altM2: 'A'}

        print(altM2)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pMat2[altM2]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altM2 = "2)Quantos centímetros existem em 5 metros? \na) 500 cm \nb) 5000 cm \nc) 0,5 cm \nd) 0,05 cm"
                        pMat2 = {altM2: 'A'}

                        print(altM2)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pMat2[altM2]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altM3 = "3)Estatística é a parte da Matemática que... \na) estuda as figuras planas \nb) coleta, analisa e apresenta informações numéricas \nc) estuda as combinações entre os números \nd) trabalha com figuras em quatro dimensões"
        pMat3 = {altM3: 'B'}

        print(altM3)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pMat3[altM3]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altM3 = "3)Estatística é a parte da Matemática que... \na) estuda as figuras planas \nb) coleta, analisa e apresenta informações numéricas \nc) estuda as combinações entre os números \nd) trabalha com figuras em quatro dimensões"
                        pMat3 = {altM3: 'B'}

                        print(altM3)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pMat3[altM3]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altM4 = "4) Chamamos de eneágono um... \na) gráfico tridimensional \nb) conjunto de n números \nc) polígono de n lados \nd) polígono de 9 lados"
        pMat4 = {altM4: 'D'}

        print(altM4)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pMat4[altM4]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altM4 = "4) Chamamos de eneágono um... \na) gráfico tridimensional \nb) conjunto de n números \nc) polígono de n lados \nd) polígono de 9 lados"
                        pMat4 = {altM4: 'D'}

                        print(altM4)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pMat4[altM4]:
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
                    print('Suas tentativas esgotaram.')
                    break


    elif t == '5':
        sleep(0.6)
        altP1 = "1) Empatia é... \na) o contrário de simpatia \nb) um jogo que termina empatado \nc) aptidão para se identificar com o outro \nd) um tipo de hepatite"
        pPort1 = {altP1: 'C'}

        print(altP1)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pPort1[altP1]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altP1 = "1) Empatia é... \na) o contrário de simpatia \nb) um jogo que termina empatado \nc) aptidão para se identificar com o outro \nd) um tipo de hepatite"
                        pPort1 = {altP1: 'C'}

                        print(altP1)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pPort1[altP1]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altP2 = '2)Na frase "João passou no concurso" o sujeito é: \na) inteligente \nb) estudioso \nc) competente \nd) João'
        pPort2 = {altP2: 'D'}

        print(altP2)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pPort2[altP2]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altP2 = '2)Na frase "João passou no concurso" o sujeito é: \na) inteligente \nb) estudioso \nc) competente \nd) João'
                        pPort2 = {altP2: 'D'}

                        print(altP2)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pPort2[altP2]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altP3 = '3)Aquele que revela inquietação, aflito, angustiado: \na) ancioso \nb) ansiozo \nc) anciozo \nd) ansioso'
        pPort3 = {altP3: 'D'}

        print(altP3)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pPort3[altP3]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altP3 = '3)Aquele que revela inquietação, aflito, angustiado: \na) ancioso \nb) ansiozo \nc) anciozo \nd) ansioso'
                        pPort3 = {altP3: 'D'}

                        print(altP3)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pPort3[altP3]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altP4 = '4)Meu filho está _________ com os brinquedos dele. \na) intretido \nb) intertido \nc) entretido \nd) entertido'
        pPort4 = {altP4: 'C'}

        print(altP4)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pPort4[altP4]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altP4 = '4)Meu filho está _________ com os brinquedos dele. \na) intretido \nb) intertido \nc) entretido \nd) entertido'
                        pPort4 = {altP4: 'C'}

                        print(altP4)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pPort4[altP4]:
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
                    print('Suas tentativas esgotaram.')
                    break


    elif t == '6':
        sleep(0.6)
        altF1 = '1)O jogador considerado o melhor de todos os tempos é: \na) Diego Maradona \nb) Lionel Messi \nc) Cristiano Ronaldo \nd) Pelé'
        pFut1 = {altF1: 'D'}

        print(altF1)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pFut1[altF1]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altF1 = '1)O jogador considerado o melhor de todos os tempos é: \na) Diego Maradona \nb) Lionel Messi \nc) Cristiano Ronaldo \nd) Pelé'
                        pFut1 = {altF1: 'D'}

                        print(altF1)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pFut1[altF1]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altF2 = '2)Qual é a seleção mais antiga? \na) Inglesa \nb) Holandesa \nc) Brasileira \nd) Belga'
        pFut2 = {altF2: 'A'}

        print(altF2)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pFut2[altF2]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altF2 = '2)Qual é a seleção mais antiga? \na) Inglesa \nb) Holandesa \nc) Brasileira \nd) Belga'
                        pFut2 = {altF2: 'A'}

                        print(altF2)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pFut2[altF2]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altF3 = '3)O time com mais títulos da copa Libertadores é: \na) Independiente \nb) Boca Juniors \nc) Flamengo \nd) Peñarol'
        pFut3 = {altF3: 'A'}

        print(altF3)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pFut3[altF3]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altF3 = '3)O time com mais títulos da copa Libertadores é: \na) Independiente \nb) Boca Juniors \nc) Flamengo \nd) Peñarol'
                        pFut3 = {altF3: 'A'}

                        print(altF3)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pFut3[altF3]:
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
                    print('Suas tentativas esgotaram.')
                    break

        sleep(0.6)
        altF4 = '4)Seleção campeã da copa de 2014: \na) Holanda \nb) Brasil \nc) Alemanha \nd) Argentina'
        pFut4 = {altF4: 'C'}

        print(altF4)
        sleep(0.6)
        escolha = input('\nQual a alternativa correta? ').upper().strip()

        if escolha == pFut4[altF4]:
            sleep(0.6)
            print('Resposta correta.')
        else:
            sleep(0.6)
            print('Resposta incorreta.')
            while True:
                if tentativas >= 1:
                    sleep(0.6)
                    dnv = input(
                        f'Quer tentar novamente? Isso custará uma tentativa (Suas tentativas {tentativas}) [S/N] ').strip().upper()[
                        0]
                    if dnv == 'S':
                        tentativas -= 1
                        sleep(0.6)
                        altF4 = '4)Seleção campeã da copa de 2014: \na) Holanda \nb) Brasil \nc) Alemanha \nd) Argentina'
                        pFut4 = {altF4: 'C'}

                        print(altF4)
                        sleep(0.6)
                        escolha = input('\nQual a alternativa correta? ').upper().strip()

                        if escolha == pFut4[altF4]:
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
                    print('Suas tentativas esgotaram.')
                    break


print("\033[1;94m                            NÍVEL 1!\033[1;97m")
temas = ["[1] ⇾  Geografia", "[2] ⇾  História", "[3] ⇾  Ciências", "[4] ⇾  Matemática", "[5] ⇾  Gramática", "[6] ⇾  Futebol"]
for i in temas:
    print(i)

tema = input(f"\nInforme o número correspondente ao tema: \n")

perguntas(tema)