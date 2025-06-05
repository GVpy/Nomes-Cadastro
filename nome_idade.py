try:
    nome = str(input("\n \n=== Cadastro de Usuário === \n \nDigite o seu nome: "))
    email = (input("Digite o e-mail: "))
    idade = int(input("Digite a sua idade: "))

    with open("cadastro.txt", "a") as arquivo:
        arquivo.write(f"{nome}  |  {email}  |  {idade} \n")
    arquivo.close()
   
    if idade >= 18:
        print ("Maior de Idade")
        Situação = "Maior de Idade"
    elif idade < 18:
        print ("Menor de Idade")
        Situação = "Menor de Idade"

    while idade < 18:
        print ("Tente Novamente Abaixo: ")
        nome = str(input("Digite o seu nome: "))
        email = (input("Digite o e-mail: "))
        idade = int(input("Digite a sua idade: "))


        arquivo = open("bebereborn.txt", "a")
        arquivo.write(f"Nome:{nome}  |  E-mail:{email}  |  Idade:{idade} \n")
        arquivo.close()


    if idade >= 18:
        print (f"\n \n=== Dados Cadastrados === \nNome:{nome}  \nE-mail:{email} \nIdade:{idade} \nSituação:{Situação}  \n \n \nDados salvos com sucesso no arquivo 'cadastros.txt'.")


except:
    print ("Coloque um número inteiro!")
