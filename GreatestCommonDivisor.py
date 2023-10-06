def GreatComDivisor(a, b):

    # example for better undestanding
    # GCD(360, 225): 360 = 225 * 1 -> Rest = 135
    #         225->(360-135) = Rest * 1 + 90 (Rest = 90)
    #         135->(225-90) =  Rest * 1 + 45 ...

    Rest = a % b  # 360 % 225
    print("Rest: ", Rest)  # = 135

    a = a - Rest  # 360-135 = 225
    print("a :", a)
    Rest = a % Rest  # 225 % 135
    print("Rest: ", Rest)  # Rest= 90

    a = a - Rest  # 225-90 = 135
    print("a :", a)
    Rest = a % Rest  # 135 % 90
    print("Rest: ", Rest)  # Rest= 45

    a = a - Rest  # 135-45 = 90
    print("a :", a)
    Rest = a % Rest  # 90 % 45 = 0, cuz 2x 45 = 90 and Rest = 0
    print("Rest:", Rest)


GreatComDivisor(a=360, b=225)
