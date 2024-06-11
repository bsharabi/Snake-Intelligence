
def menu():
    print("What's the programming language you want to learn? ")
    print("1. Running the Game")
    print("2. Running the AI")
    print("3. exit")

if __name__ == "__main__":
    menu()
    lang = int(input())
    match lang:
        case 1:
            from game.snake import Snake
            snake=Snake()
            snake()
        case 2:
            from ai.agent import train
            train()
            pass
        case 3:
            exit(0)
            pass
        case _:
            print("Invalid")