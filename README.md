import math

def PrimeList(N):
    primes = []
    for num in range(2, N):
        is_prime = True
        # 检查从2到num的平方根之间的数是否能整除num
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 用空格连接所有质数，返回结果
    return ' '.join(primes)
