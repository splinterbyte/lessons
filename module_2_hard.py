def make_encrypt(num):
    encrypt = []
    for i in range(1, 21):
        for j in range(i, 21):
            pair_sum = i + j
            if num % pair_sum == 0:
                encrypt.append(str(i) + str(j))
    return ''.join(encrypt)

num = 9
print(make_encrypt(num))