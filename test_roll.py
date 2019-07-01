from roll import Roll
import pytest


@pytest.fixture
def rock():
    return Roll(name='rock')


@pytest.fixture
def paper():
    return Roll(name='paper')


@pytest.fixture
def scissors():
    return Roll(name='scissors')


def test_roll_has_name(rock):
    assert rock.name == 'rock'


def test_rock_beats_scissors(rock, scissors):
    assert rock.play(scissors) == 'win'


def test_paper_beats_rock(rock, paper):
    assert paper.play(rock) == 'win'


def test_scissors_beats_paper(paper):
    scissors = Roll(name='scissors')
    assert scissors.play(paper) == 'win'


def test_rock_draws_with_other_rock(rock):
    another_rock = Roll(name='rock')
    assert rock.play(another_rock) == 'draw'


def test_paper_loses_to_scissors(paper):
    scissors = Roll(name='scissors')
    assert paper.play(scissors) == 'lose'


def test_randomly_choose_roll():
    assert Roll.random_choice() in [Roll('rock'), Roll('paper'), Roll('scissors')]
