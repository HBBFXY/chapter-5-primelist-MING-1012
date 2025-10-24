import math

def PrimeList(N):
    primes = []  # 用于存储质数的列表
    for num in range(2, N):  # 遍历 2 到 N-1 的所有数
        is_prime = True  # 假设当前数字是质数
        for i in range(2, int(math.sqrt(num)) + 1):  # 检查是否能被 2 到 sqrt(num) 之间的数整除
            if num % i == 0:
                is_prime = False  # 如果能整除，则不是质数
                break
        if is_prime:
            primes.append(str(num))  # 是质数则加入列表，转为字符串方便后续拼接
    return ' '.join(primes)  # 用空格将质数连接成一个字符串并返回
