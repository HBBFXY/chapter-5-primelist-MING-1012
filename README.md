import math

def PrimeList(N):
    primes = []  # 修正变量名：素数 -> primes（保持英文一致性）
    for num in range(2, N):  # 修正语法：对于...中的 -> for...in
        is_prime = True  # 修正：真 -> True
        # 检查从2到num的平方根之间的数是否能整除num
        for i in range(2, int(math.sqrt(num)) + 1):  # 修正语法错误：多余的括号
            if num % i == 0:  # 修正：如果 -> if；错误 -> False
                is_prime = False
                break  # 修正：破 -> break
        if is_prime:
            primes.append(str(num))
    # 用空格连接所有质数，返回结果
    return ' '.join(primes)
