import pytest
from game import Game
from game_result import GameResult

@pytest.fixture
def game():
    return Game()

def assert_illegal_argument(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)

@pytest.mark.parametrize("invalid_input", [None, "12", "1234", "12s", "121"])
def test_exception_when_invalid_input(game, invalid_input):
    assert_illegal_argument(game, invalid_input)

def assert_matched_number(result, solved, strikes, balls):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikes
    assert result.balls == balls

def test_return_solve_result_if_matched_number(game):
    game.question = "123"
    assert_matched_number(game.guess("123"), solved=True, strikes=3, balls=0)

def test_return_solve_result_if_unmatched_number(game):
    game.question = "123"
    assert_matched_number(game.guess("456"), solved=False, strikes=0, balls=0)

def test_return_solve_result_if_2strikes_0ball(game):
    game.question = "123"
    assert_matched_number(game.guess("523"), solved=False, strikes=2, balls=0)

def test_return_solve_result_if_1strikes_2ball(game):
    game.question = "123"
    assert_matched_number(game.guess("132"), solved=False, strikes=1, balls=2)
