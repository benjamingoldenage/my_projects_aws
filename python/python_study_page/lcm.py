def lcm(num1,num2):
    common_multiplication = []
    for i in range(max(num1,num2), num1*num2+1):
        if i%num1==0 and i%num2==0:
            common_multiplication.append(i)
    return min(common_multiplication)