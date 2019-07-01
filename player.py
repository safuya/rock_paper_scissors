from roll import Roll


class Player:
    VALID_KINDS = {'human', 'computer'}

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        if value in self.VALID_KINDS:
            self._kind = value
        else:
            raise ValueError(f'The kind must be one of {", ".join(self.VALID_KINDS)}.')

    def make_choice(self):
        if self.kind == 'computer':
            return Roll.random_choice()
        else:
            return Roll(input('Select rock, paper or scissors. '))

    def play(self, other):
        result = self.make_choice().play(other.make_choice())
        return f'{self.name} wins' if result == 'win' \
               else 'Draw' if result == 'draw' \
               else f'{other.name} wins'
