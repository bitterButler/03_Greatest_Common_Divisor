def GreatComDivisor(a, b):
    store_NUM_A = a
    store_NUM_B = b
    # example for better undestanding
    # GCD(360, 225): 360 = 225 * 1 -> Rest = 135
    #         225->(360-135) = Rest * 1 + 90 (Rest = 90)
    #         135->(225-90) =  Rest * 1 + 45 ...

    # with whiles, and if-else
    while (b > 0):  # 135 > 0
        R = a % b  # R = 360 % 225 -> 135
        if b > R:  # 225 > 135
            a = b  # a = 225
            b = R  # b = 135
            # a % b
            # print("a, b, : ", a, b, )
    print(
        f"The Greatest Common Divisor for {store_NUM_A} and {store_NUM_B} is: ", a)


GreatComDivisor(a=int(input("a num= ")), b=int(input("b num= ")))
