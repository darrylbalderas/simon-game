import os
import sys
import platform
import time
import random


def continue_game(play_again=False) -> bool:
    if play_again:
        message = "Want to play \
again this game (Hit any key to continue or 'q' to quit): "
    else:
        message = "Want to play \
(Hit any key to continue or 'q' to quit): "
        
    choice = input(message)
    return True if choice.lower() != 'q' else False


def breaks(n=0) -> str:
    return "\n"*n


def clear_output(wait_time=0) -> None:
    time.sleep(wait_time)
    if 'linux' in sys.platform or 'darwin' == sys.platform:
        os.system('clear') 
    else:
        os.system('cls') 


def level_message(sequence: list, level: int) -> None:
    message = "\033[1;95mSequence {}:\n\n\033[4m{}".format(level, " ".join(map(str, sequence)))
    return message


def reset_term_colors():
    print("\33[0m")


def print_message(message="", sleep_time=2):
    header = """\033[1;32;40m
 .----..-..-.   .-. .----. .-. .-.    .---.   .--.  .-.   .-..----.  ||| |||
{ {__  | ||  `.'  |/  {}  \|  `| |   /   __} / {} \ |  `.'  || {_    ||| |||
.-._} }| || |\ /| |\      /| |\  |   \  {_ }/  /\  \| |\ /| || {__   ||| |||
`----' `-'`-' ` `-' `----' `-' `-'    `---' `-'  `-'`-' ` `-'`----'   0   0
"""
    clear_output()
    print(header)
    reset_term_colors()
    if message:
        print(message)
    time.sleep(sleep_time)
    clear_output()
    reset_term_colors()


def create_simon(level: int) -> list:
    return random.randint(1, 4)


def print_failing_index(index):
    space = (index)*' '
    print(space + '^')


def input_error_message(invalid_msg, index, answers):
    print(invalid_msg + answers)
    print_failing_index(index + len(invalid_msg))


def validate_answers(answers) -> tuple:
    invalid_msg = "Answers can only be numbers from 1 through 4: "
    for index, value in enumerate(answers):
        try:
            seq_num = int(value)
            if seq_num < 0 or seq_num > 4:
                input_error_message(invalid_msg, index, answers)
                return index, False
        except:
            input_error_message(invalid_msg, index, answers)
            return index, False
    return None, True


def is_correct(level, user):  
    if len(level) != len(user):
        return False
    for i in range(len(level)):
        if level[i] != user[i]:
            return False
    return True


def main():
    print_message()
    lost = False
    level = 1
    play_game = continue_game()
    while play_game:
        print(breaks())
        print_message("Let's get started !!!!")
        sequence = []
        while not lost:
            sequence.append(create_simon(level))
            print_message(level_message(sequence, level))
            valid = False
            user_answer = []
            while not valid:
                clear_output(1)
                user_input = input("Type sequence: ")
                index, valid,  = validate_answers(user_input)
            user_answer = [int(val) for val in user_input ]
            print(sequence)
            print(user_answer)
            print(is_correct(sequence, user_answer))
            if not is_correct(sequence, user_answer):
                lost = True
                print("Sorry you lost !!!")
            level += 1
        if lost:
            play_game = continue_game()
            lost = False


if __name__ == "__main__":
    main()