from faker import Faker
import pandas as pd

# puxando lib
fake = Faker()

# numero de dados
d = 30

# Cria uma lista de dicionários com dados falsos
data = []

r = 1
while r < d:
    dado = {
        'Nome': fake.name(),
        'Idade': fake.random_int(min=18, max=80, step=1),
        'Email': fake.email(),
        'Telefone': fake.phone_number()
    }
    data.append(dado)
    r += 1


df = pd.DataFrame(data)

# Salvando tabela
df.to_excel('tabelafalsa.xlsx', index=False)