import pytest

from game import Game


def test_game():
    game = Game()
    with pytest.raises(TypeError):
        game.guess(None)
    pass
