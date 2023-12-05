for number in range(100):
    if number != 99:
        print ("{n:02d}".format(n = number), end=", ")
    else:
        print ("{n:02d}".format(n = number), end="\n")