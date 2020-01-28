file_open = open('people.csv')
datas = file_open.read()
file_open.close()

for registro in datas.splitlines():
    print('Nome: {} e Sobrenome:{}'.format(*registro.split(',')))