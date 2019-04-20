
def continue_game() -> bool:
    choice = input("Want to play \
this game (Hit any key to continue or 'q' to quit): ")
    return True if choice.lower() != 'q' else False

def main():
    header = """
 .----..-..-.   .-. .----. .-. .-.    .---.   .--.  .-.   .-..----.
{ {__  | ||  `.'  |/  {}  \|  `| |   /   __} / {} \ |  `.'  || {_  
.-._} }| || |\ /| |\      /| |\  |   \  {_ }/  /\  \| |\ /| || {__ 
`----' `-'`-' ` `-' `----' `-' `-'    `---' `-'  `-'`-' ` `-'`----'
    """
    print(header)
    while(continue_game()):
        pass


if __name__ == "__main__":
    main()