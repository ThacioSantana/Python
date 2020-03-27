from colorama import Fore, Style

for x in range(1, 30, 2):
    if x == 1:
        print(Style.BRIGHT + Fore.YELLOW + "{:^36}".format("\u2721"))
    elif x == 15:
        print(Fore.GREEN + "{:^36}".format('Feliz Hanukkah!!!!'))
    elif x == 19:
        print(Fore.RED + "{:^36}".format('Feliz Natal!!!!'))
    elif x == 23:
        print(Fore.YELLOW + "{:^36}".format('Feliz Kwanzaa!!!!'))
    else:
        print(Fore.WHITE + "{:^36}".format("*" * x))
print("{:^36}".format('|||'))
print("{:^36}".format('|||'))