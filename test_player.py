import pytest
from player import Player


def test_players_have_kinds():
    player = Player()
    player.kind = 'computer'
    assert player.kind == 'computer'


def test_kind_invalid_value():
    player = Player()
    with pytest.raises(ValueError):
        player.kind = 'alien'


def test_players_have_names():
    player = Player()
    player.name = 'Rob'
    assert player.name == 'Rob'


def test_computer_players_choose_randomly():
    player1 = Player()
    player1.kind = 'computer'
    player1.name = 'Data'
    player2 = Player()
    player2.kind = 'computer'
    player2.name = 'R2D2'
    assert player1.play(player2) in {'Data wins', 'R2D2 wins', 'Draw'}
