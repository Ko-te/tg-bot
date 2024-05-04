from collections import Counter
from faker import Faker


fake = Faker("ru_RU")


x = [fake.first_name_male() for i in range(100000)]
y = [fake.first_name_female() for i in range(100000)]

for i in range(1990, 2025):
    with open (f'boys_{i}.txt', 'w', encoding='utf-8') as file:
        for name in x:
            file.write(name + '\n')

    with open (f'girls_{i}.txt', 'w', encoding='utf-8') as file:
        for name in y:
            file.write(name + '\n')



