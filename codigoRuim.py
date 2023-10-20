"""_____________________________________________________________________________________________________
Este código tem muitos problemas de má prática, como repetição de código, lógica confusa e excesso de 
comentários, o que o torna mais difícil de ler e entender. Lembre-se de que na prática, é importante 
escrever um código claro e legível para facilitar a interpretação, manutenção e a colaboração. 
____________________________________________________________________________________________________"""


# Função para cadastrar pessoa
def cadastrar_people():
    # Iniando cadastro
    print("Iniciando cadastro de pessoa...")

    # Nome da pessoa 
    n = input("Digite o nome da pessoa: ")
    #Idade da pessoa
    i = int(input("Digite a idade da pessoa: "))
    # Email da pessoa
    email = input("Digite o e-mail da pessoa: ")
    # Telefone da pessoa
    t = input("Digite o telefone da pessoa: ")
    # Cidade da pessoa
    c = input("Digite a cidade da pessoa: ")
    # Escolaridade da pessoa
    e = input("Digite a escolaridade da pessoa: ")
    # Profissão da pessoa
    p = input("Digite a profissão da pessoa: ")

    # Inicializa cidadania, restricao, sus e regiao
    cidadania = ""
    restricao = ""
    sus = ""
    regiao = ""

    # Condição para maior de 18 anos
    if i > 18:
        print("Cadastro direto da pessoa:")

        # Condição para plano de saúde ou sus
        plano_saude = input("A pessoa possui plano de saúde? (S/N): ").upper()
        # Inicializando condição
        if plano_saude == 'S':
            # Imprimindo condição
            print("A pessoa possui plano de saúde.")
            sus = "N/A"
        else:
            # Verificando se a pessoa usa o sus
            sus = input("A pessoa utiliza o SUS? (S/N): ").upper()
            # se sim, imprimir que utiliza o sus
            if sus == 'S':
                print("A pessoa utiliza o SUS.")
            else:
                # se não, imprimir que ela não usa e não plano de saúde
                print("A pessoa não possui plano de saúde e não utiliza o SUS.")
        
        # Restrição alimentar
        restricao_alimentar = input("A pessoa possui alguma restrição alimentar? (S/N): ").upper()
        # Condição para essa restrição
        if restricao_alimentar == 'S':
            restricao = input("Descreva a restrição alimentar da pessoa: ")
            print("Restrição alimentar:", restricao)
        # Condição se a pessoa não possui restrição alimentar
        else:
            print("A pessoa não possui restrição alimentar.")
    # Condição para a pessoa menor de 18 anos
    else:
        print("A pessoa é menor de 18 anos. Informe os dados do responsável:")
        # Nome do responsavel
        responsavel_n = input("Digite o nome do responsável: ")
        # Email do responsavel
        responsavel_e = input("Digite o e-mail do responsável: ")
        # telefone do responsavel
        responsavel_t = input("Digite o telefone do responsável: ")

        # os pais são brasileiros?
        pais_brasileiros = input("A pessoa tem pai ou mãe brasileira? (S/N): ").upper()
        # se sim, recebe cidadania
        if pais_brasileiros == 'S':
            cidadania = "A pessoa recebe a cidadania brasileira."
        # se não, não recebe
        else:
            cidadania = "A pessoa não recebe a cidadania brasileira."
        # Restrição alimentar
        restricao_alimentar = input("A pessoa possui alguma restrição alimentar? (S/N): ").upper()
        # se a pessoa possui
        if restricao_alimentar == 'S':
            # qual restrição?
            restricao = input("Descreva a restrição alimentar da pessoa: ")
        # a pessoa utiliza o sus
        sus = input("A pessoa utiliza o SUS? (S/N): ").upper()
        # se sim, imprimir que utilza
        if sus == 'S':
            print("A pessoa utiliza o SUS.")
        # se não, imprimir que não utiliza
        else:
            print("A pessoa não utiliza o SUS.")

        # estado que a pessoa mora
        estado = input("Digite o estado onde a pessoa mora: ").capitalize()
        # Sudeste
        if estado == 'São Paulo' or estado == 'Rio de Janeiro' or estado == 'Minas Gerais' or estado == 'Espírito Santo':
            regiao = 'Sudeste'
        # Sul
        elif estado == 'Paraná' or estado == 'Santa Catarina' or estado == 'Rio Grande do Sul':
            regiao = 'Sul'
        # Centro-Oeste
        elif estado == 'Goiás' or estado == 'Mato Grosso' or estado == 'Mato Grosso do Sul' or estado == 'Distrito Federal':
            regiao = 'Centro-Oeste'
        # Nordeste
        elif estado == 'Bahia' or estado == 'Sergipe' or estado == 'Alagoas' or estado == 'Pernambuco' or estado == 'Paraíba' or estado == 'Rio Grande do Norte' or estado == 'Ceará' or estado == 'Piauí' or estado == 'Maranhão':
            regiao = 'Nordeste'
        # Norte
        elif estado == 'Rondônia' or estado == 'Acre' or estado == 'Amazonas' or estado == 'Roraima' or estado == 'Pará' or estado == 'Amapá' or estado == 'Tocantins':
            regiao = 'Norte'
        # Nenhum
        else:
            regiao = 'Região não encontrada'

    # imprimindo resultados
    print("\nResumo do Cadastro:")
    # Nome
    print("Nome:", n)
    # Idade
    print("Idade:", i)
    # Email
    print("E-mail:", email)
    # Telefone
    print("Telefone:", t)
    # Cidade
    print("Cidade:", c)
    # Escolaridade
    print("Escolaridade:", e)
    # Profissão
    print("Profissão:", p)
    # Condição menoridade para imprimir
    if i <= 18:
        # Nome
        print("Responsável Nome:", responsavel_n)
        # Email
        print("Responsável Email:", responsavel_e)
        # Telefone
        print("Responsável Telefone:", responsavel_t)
    # Cidadania
    print("Cidadania:", cidadania)
    # Restrição Alimentar
    print("Restrição Alimentar:", restricao)
    # Utiliza sus
    print("Utilização do SUS:", sus)
    # Região
    print("Região:", regiao)
    # imprimi que foi cadastrado com sucesso
    print("Pessoa cadastrada com sucesso!")

# Chama a função para cadastrar pessoa (cadastrar_pessoa())
cadastrar_people()
