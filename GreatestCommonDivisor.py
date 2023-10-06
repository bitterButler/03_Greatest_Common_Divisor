def GreatComDivisor(a, b):

    # example for better undestanding
    # GCD(360, 225): 360 = 225 * 1 -> Rest = 135
    #         225->(360-135) = Rest * 1 + 90 (Rest = 90)
    #         135->(225-90) =  Rest * 1 + 45 ...

    # with whiles, and if-else
    print("a / b: ", a % b)
    while (b > 0):  # 135 > 0
        R = a % b  # R = 360 % 225 -> 135
        if b > R:  # 225 > 135
            a = b  # a = 225
            b = R  # b = 135
            # a % b
            print("a, b, : ", a, b, )


GreatComDivisor(a=360, b=225)
