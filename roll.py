import random


class Roll:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def valid_choices():
        return {'rock', 'paper', 'scissors'}

    @classmethod
    def choices(cls):
        return [Roll(choice) for choice in cls.valid_choices()]

    @classmethod
    def random_choice(cls):
        return random.choice(cls.choices())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value in self.valid_choices():
            self._name = value
        else:
            raise ValueError(f'You must choose between {self.choices().join(", ")}.')

    def __gt__(self, other):
        return any([self.name == 'rock' and other.name == 'scissors',
                    self.name == 'paper' and other.name == 'rock',
                    self.name == 'scissors' and other.name == 'paper'])

    def __eq__(self, other):
        return self.name == other.name

    def play(self, other):
        return 'win' if self > other else 'draw' if self == other else 'lose'
