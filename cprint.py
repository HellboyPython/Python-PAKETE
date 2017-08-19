def cprint(a,b):
    xx = 0
    try:
        b = str(b)
    except:
        print("\033[1;31;40m[Error]:pleas instert a color")
        xx = 1


    if (b == "BLACK"):
        print("\033[0;30;48m" + str(a))
    if (b == "RED"):
        print("\033[0;31;48m" + str(a))
    if (b == "GREEN"):
        print("\033[0;32;48m" + str(a))
    if (b == "BROWN"):
        print("\033[0;33;48m" + str(a))
    if (b == "BLUE"):
        print("\033[0;34;48m" + str(a))
    if (b == "PURPLE"):
        print("\033[0;35;48m" + str(a))
    if (b == "CYAN"):
        print("\033[0;36;48m" + str(a))
    if (b == "LIGHT GRAY"):
        print("\033[0;37;48m" + str(a))

    if (b == "DARK GRAY"):
        print("\033[1;30;48m" + str(a))
    if (b == "LIGHT RED"):
        print("\033[1;31;48m" + str(a))
    if (b == "LIGHT GREEN"):
        print("\033[1;32;48m" + str(a))
    if (b == "YELLOW"):
        print("\033[1;33;48m" + str(a))
    if (b == "LIGHT BLUE"):
        print("\033[1;34;48m" + str(a))
    if (b == "LIGHT PURPLE"):
        print("\033[1;35;48m" + str(a))
    if (b == "LIGHT CYAN"):
        print("\033[1;36;48m" + str(a))
    if (b == "WHITE"):
        print("\033[1;37;48m" + str(a))

def help():
    print("CONTEXT: cprint(Text, Color)")
    print("COLORS:")
    print("BLACK")
    print("RED")
    print("GREEN")
    print("BROWN")
    print("BLUE")
    print("PURPLE")
    print("CYAN")
    print("YELLOW")
    print("WHITE")

    print("DARK GRAY")
    print("LIGHT GRAY")
    print("LIGHT RED")
    print("LIGHT GREEN")
    print("LIGHT BLUE")
    print("LIGHT PURPLE")
    print("LIGHT CYAN")