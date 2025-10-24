def PrimeList(N):
    primes = []  # 存储素数的列表
    for num in range(2, N):  # 遍历从2到N-1的数
        is_prime = True  # 标记是否为素数
        # 检查是否能被2到num平方根之间的数整除
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:  # 能被整除，不是素数
                is_prime = False
                break
        if is_prime:  # 如果是素数，添加到列表
            primes.append(str(num))
    return " ".join(primes)  # 用空格连接素数字符串并返回

# 调用函数并打印结果，例如生成小于20的素数
print(PrimeList(20))  # 输出：2 3 5 7 11 13 17 19
