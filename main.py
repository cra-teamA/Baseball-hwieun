import random
from game import Game

def main():
    game = Game()
    answer= get_computer_question()
    game._question = str(answer)
    trial = 1
    while True:
        user_input = input()
        ret = game.guess(user_input)
        print(f'시도{trial}번째...\n성공 여부 : {ret.solved}\t| 스트라이크 : {ret.strikes}\t| 볼 : {ret.balls}')
        if ret.solved:
            print(f'통과! 정답은 {game._question} 이었습니다!!!')
            break
        print()
        trial += 1

def get_computer_question():
    while True:
        num = random.randint(100, 999)
        first_digit = num // 100
        second_digit = (num % 100) // 10
        third_digit = num % 10
        if first_digit != second_digit and \
            second_digit != third_digit and \
            third_digit != first_digit:
            return num

main()