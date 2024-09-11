def make_encrypt(num):
    result = ""
    pairs = []
    for i in range(1, 21):
        for j in range(1, 21):
            if i != j and num % (i + j) == 0:
                pair = (i, j)
                if pair not in pairs and (j, i) not in pairs:
                    pairs.append(pair)
    for pair in pairs:
        result += str(pair[0]) + str(pair[1])
    return result

for n in range(3, 21):
    print(f"{n} - {make_encrypt(n)}")
