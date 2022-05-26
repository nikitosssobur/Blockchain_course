import random as rnd
import time

#1. Количество вариантов ключей


bits_lenghts = [2**i for i in range(3,13)]
keys_space = []
for j in bits_lenghts:
    keys_space.append(2**j)
    print(f"Длина {j} бит: {keys_space[len(keys_space)-1]}",end='\n\n')


#2. Генерация ключей
def random_0x(start=0x0, end=0xFFFFFF):
    return hex(rnd.randint(start, end))

d = dict()
for i in keys_space:
    d[i] = random_0x(0,i)

print(f"Словарь сгенерированных значений: {d}")

#3. Функция поиска

def brutforce(dict_):
    for i in list(dict_.keys())[:4]:
        start_time = time.time()
        j = 0
        while not dict_[i] == hex(j):
            # print(hex(j))
            j += 1
        else:
            print("--- %s seconds ---" % (time.time() - start_time))

brutforce(d)
