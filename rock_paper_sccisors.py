import random


def play(player, opponent):
    if player == opponent:
        return f"It's a tie !"
    if is_win(player, opponent):
        return f"You have won!"
    
    return f"You have lost!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's' or player == 'p' and opponent == 'r' or player == 's' and opponent == 'p'):
        return True


def main():
    player = input("'r' for rock, 'p' for paper, 's' for sccissors: ").lower()
    opponent = random.choice(['r','p','s'])
    result = play(player, opponent)
    print(result)
    print(f"Double check {opponent}")


if __name__ == "__main__":
    main()