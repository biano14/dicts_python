usuario = {}

usuario['Nome'] = input('Informe o nome a pessoa a ser cadastrada: ')
usuario['Sexo'] = input('Informe o genêro da pessoa a ser cadastrada: ')
usuario['CPF'] = input('Informe o CPF da pessoa a ser cadastrada: ')
usuario['RG'] = input('Informe o RG da pessoa a ser cadastrada: ')
usuario['Data de Nascimento'] = input('Informe a data de nascimento:')
usuario['Signo'] = input('Informe o signo:')
usuario['Mãe'] = input('Informe o nome da mãe: ')
usuario['Pai'] = input('Informe o nome do pai: ')
usuario['Email'] = input('Informe o email: ')
usuario['Senha'] = input('Informe o senha do email: ')
usuario['CEP'] = input('Informe o CEP: ')
usuario['Endereço'] = input('Informe o Endereço: ')
usuario['Número'] = input('Informe o número do Endereço: ')
usuario['Bairro'] = input('Informe o bairro do Endereço: ')
usuario['Cidade'] = input('Informe a Cidade: ')
usuario['Estado'] = input('Informe o Estado: ')
usuario['Telefone'] = input('Informe o telefone: ')
usuario['Celular'] = input('Informe o celular: ')
usuario['Altura'] = input('Informe a altura: ')
usuario['Peso'] = input('Informe o peso: ')
usuario['Tipo Sanguineo'] = input('Informe seu tipo sanguineo: ')
usuario['Cor'] = input ('Informe a cor favorita: ')

#exigir o dicionario
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')

