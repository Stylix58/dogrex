from colorama import Fore, Back, Style
from colorama import init as init_colorama
init_colorama()

stopState = False
prom = "dogrex> "
inpt = ""

print("Welcome to DogRex, the dog simulator!")

def starting():
    print("What thing do you want to make?")
    print("\n1. New game\n2. Exit\n")
    return input(prom)

if __name__ == "__main__":
    try:
        while stopState == False:
            if starting() == 1:
                print("For now, this game is in early access and you can't play for now...")
                exit()
            else:
                print("Goodbye!")
                exit()
    except KeyboardInterrupt:
        print()
        print("Goodbye!")
        exit()