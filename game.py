from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number) -> GameResult | None:
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True, 3, 0)

        strike_cnt, ball_cnt = self.get_strike_and_ball_count(guess_number)
        return GameResult(False, strike_cnt, ball_cnt)

    def get_strike_and_ball_count(self, guess_number):
        strike_cnt = 0
        ball_cnt = 0
        for num, ans_num in zip(guess_number, self._question):
            if num == ans_num:
                strike_cnt += 1
            elif num in self._question:
                    ball_cnt += 1
        return strike_cnt, ball_cnt

    def _assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError("입력이 None 입니다.")

        if len(guess_number) != 3:
            raise TypeError("입력은 3 자리 문자열이어야 합니다.")

        if not guess_number.isdigit():
            raise TypeError("모든 문자는 숫자로 구성되어야 합니다.")

        if self._is_duplicated_number(guess_number):
            raise TypeError("중복된 숫자가 존재합니다.")

    def _is_duplicated_number(self, guessNumber):
        return len(set(guessNumber)) != 3