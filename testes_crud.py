# Inserindo dados para testes

objeto_dml = CrudSQLite(nome_banco='desafio')

# Inserir registros
dados = [
    {
        'nome_cliente': 'João',
        'cpf': '111.111.111-11',
        'email': 'joao@servidor',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'data_cadastro': '2020-01-01'
    },
    {
        'nome_cliente': 'Maria',
        'cpf': '222.222.222-22',
        'email': 'maria@servidor',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'data_cadastro': '2020-01-01'
    },
]
# Para cada dicionário na lista de dados, invoca o método de inserção
for valor in dados:
    objeto_dml.inserir_registro(tabela='cliente', registro=valor)

# Carrega dados salvos
dados_carregados = objeto_dml.ler_registros(tabela='cliente')
for dado in dados_carregados:
    print(dado)
    
# Atualiza registro
dado_atualizar = {'telefone': '(11) 1111-1111'}
condicao = {'id_cliente': 1}

objeto_dml.atualizar_registro(tabela='cliente', dado=dado_atualizar, condicao=condicao)

dados_carregados = objeto_dml.ler_registros(tabela='cliente')
for dado in dados_carregados:
    print(dado)

# Apaga registro
condicao = {'id_cliente': 1}

objeto_dml.apagar_registro(tabela='cliente', condicao=condicao)
