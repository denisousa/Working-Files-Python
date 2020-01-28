# Gravando dados em um novo arquivo
with open('people.csv') as people_csv:
    # Default open() is mode 'r'
    with open('people.txt' ,'w') as out:
        for register in people_csv:
            person = register.strip().split(',')
            print('Nome: {} Sobrenome: {}'.format(*person), file=out)