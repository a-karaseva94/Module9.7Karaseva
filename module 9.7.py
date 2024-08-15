# Задание по теме: "Декораторы"

def is_prime(func):
    def wrapper(a, b, c):
        origin_result = func(a, b, c)
        if origin_result > 2:
            for n in range(2, origin_result - 1):
                if origin_result % n == 0:
                    print('Составное')
                    break
            else:
                print('Простое')
        else:
            print('Это не простое и не составное число')
        return origin_result
    return wrapper

@is_prime
def sum_three(a, b, c):
    summa = int(a + b + c)
    return summa

# Пример:
result = sum_three(2, 3, 6)
print(result)