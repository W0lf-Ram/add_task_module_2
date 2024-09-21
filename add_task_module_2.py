number = int(input('Ведите число от 3 до 20: '))
if number < 3:
    print('Не верное число!')
else:
    password = []
    for i in range(1, 21):
        for j in range(2, 21):
            if i >= j:
                continue
            if number % (i +j) == 0:
                password.extend([i, j])
    print(*password)






