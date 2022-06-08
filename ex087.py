from datetime import datetime
workers = dict()
workers['name'] = str(input('Name: ')).strip()
born = int(input('Birth Date: '))
workers['age'] = datetime.now().year - born
workers['ctps'] = int(input('Carteira de trabalho [0 não tem] '))
if workers['ctps'] == 0:
    for k, v in workers.items():
        print(f'{k} = {v}')
elif workers['ctps'] != 0:
    workers['hirig'] = int(input('Year of hiring: '))
    workers['retirement'] = workers['hirig'] + 35 - born
    workers['wage'] = int(input('Wage: '))
    for k, v in workers.items():
        print(f'{k} = {v}')
