def make_encrypt(num):
    encrypt = []
    for i in range(1, 21):
        for j in range(i, 21):
            pair_sum = i + j
            if num % pair_sum == 0:
                encrypt.append(str(i) + str(j))
    result = ''.join(encrypt)
    print(f'{num} - {result}')


while True:
    num = int(input('Введите число от 3 до 20: '))
    if num < 3 or num > 20:
        continue
    make_encrypt(num)
    break
