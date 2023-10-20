"""_____________________________________________________________________________________________________
Este código tem muitos problemas de má prática, como repetição de código, lógica confusa e excesso de 
comentários, o que o torna mais difícil de ler e entender. Lembre-se de que na prática, é importante 
escrever um código claro e legível para facilitar a interpretação, manutenção e a colaboração. 
____________________________________________________________________________________________________"""


def cadastrar_people():
    print("Iniciando cadastro de pessoa...")

    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    email = input("Digite o e-mail da pessoa: ")
    telefone = input("Digite o telefone da pessoa: ")
    cidade = input("Digite a cidade da pessoa: ")
    escolaridade = input("Digite a escolaridade da pessoa: ")
    profissao = input("Digite a profissão da pessoa: ")

    cidadania = ""
    restricao = ""
    sus = ""
    regiao = ""

    if idade > 18:
        print("Cadastro direto da pessoa:")
        plano_saude = input("A pessoa possui plano de saúde? (S/N): ").upper()
        if plano_saude == 'S':
            print("A pessoa possui plano de saúde.")
            sus = "N/A"
        if plano_saude == 'S':
            sus = input("A pessoa utiliza o SUS? (S/N): ").upper()
        if sus == 'S':
            print("A pessoa utiliza o SUS.")
            else:
                print("A pessoa não utiliza o SUS.")
    
        restricao_alimentar = input("A pessoa possui alguma restrição alimentar? (S/N): ").upper()
        if restricao_alimentar == 'S':
            restricao = input("Descreva a restrição alimentar da pessoa: ")
            print("Restrição alimentar:", restricao)
        else:
            print("A pessoa não possui restrição alimentar.")
    else:
        print("A pessoa é menor de 18 anos. Informe os dados do responsável:")
        responsavel_nome = input("Digite o nome do responsável: ")
        responsavel_escolaridade= input("Digite o e-mail do responsável: ")
        responsavel_telefone = input("Digite o telefone do responsável: ")
        pais_brasileiros = input("A pessoa tem pai ou mãe brasileira? (S/N): ").upper()
        if pais_brasileiros == 'S':
            cidadania = "A pessoa recebe a cidadania brasileira."
        else:
            cidadania = "A pessoa não recebe a cidadania brasileira."
        restricao_alimentar = input("A pessoa possui alguma restrição alimentar? (S/N): ").upper()
        if restricao_alimentar == 'S':
            restricao = input("Descreva a restrição alimentar da pessoa: ")
        sus = input("A pessoa utiliza o SUS? (S/N): ").upper()
        if sus == 'S':
            print("A pessoa utiliza o SUS.")
        else:
            print("A pessoa não utiliza o SUS.")

        estado = input("Digite o estado onde a pessoa mora: ").capitalize()
        if estado == 'São Paulo' or estado == 'Rio de Janeiro' or estado == 'Minas Gerais' or estado == 'Espírito Santo':
            regiao = 'Sudeste'
        elif estado == 'Paraná' or estado == 'Santa Catarina' or estado == 'Rio Grande do Sul':
            regiao = 'Sul'
        elif estado == 'Goiás' or estado == 'Mato Grosso' or estado == 'Mato Grosso do Sul' or estado == 'Distrito Federal':
            regiao = 'Centro-Oeste'
        elif estado == 'Bahia' or estado == 'Sergipe' or estado == 'Alagoas' or estado == 'Pernambuco' or estado == 'Paraíba' or estado == 'Rio Grande do Norte' or estado == 'Ceará' or estado == 'Piauí' or estado == 'Maranhão':
            regiao = 'Nordeste'
        elif estado == 'Rondônia' or estado == 'Acre' or estado == 'Amazonas' or estado == 'Roraima' or estado == 'Pará' or estado == 'Amapá' or estado == 'Tocantins':
            regiao = 'Norte'
        else:
            regiao = 'Região não encontrada'
            
    print("\nResumo do Cadastro:")
    print("Nome:", nome)
    print("Idade:", idade)
    print("E-mail:", email)
    print("Telefone:", tefone)
    print("Cidade:", cidade)
    print("Escolaridade:", escolaridade)
    print("Profissão:", profissao)
    if i <= 18:
        print("Responsável Nome:", responsavel_nome)
        print("Responsável Email:", responsavel_email)
        print("Responsável Telefone:", responsavel_telefone)
        print("Cidadania:", cidadania)
        print("Restrição Alimentar:", restricao)
        print("Utilização do SUS:", sus)
        print("Região:", regiao)
        print("Pessoa cadastrada com sucesso!")
cadastrar_people()
