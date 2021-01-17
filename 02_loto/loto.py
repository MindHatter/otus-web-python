import argparse
import random


class Player:
    def __init__(self, name):
        self.name = name


class Card:
    def __init__(self, owner):
        self._card = self._gen_card()
        self.owner = owner
        print(f"{self.owner}'s card {self._card}")

    def _gen_card(self):
        bag = Game.gen_bag()
        return bag[:15]

    def _check(self, n):
        try:
            self._card.remove(n)
            print(f"{self.owner.name} found {n} in his card.")
        except:
            pass

    def __repr__(self):
        return f"{self.owner.name}'s card"

    def __str__(self):
        return f"{self.owner.name}'s card"


class Game:
    def __init__(self, cards):
        self.cards = cards
        self.bag = self.gen_bag()
        self.winners = []
        self.step = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.winners:
            if len(self.winners) > 1:
                print(f"{', '.join([str(w) for w in self.winners])} win")
            else:
                print(f"{self.winners[0]} wins")
            raise StopIteration

        keg = random.choice(self.bag)
        self.bag.remove(keg)
        print(f"Step: {self.step} / Keg: {keg}")

        for card in self.cards:
            card._check(keg)
            if not card._card:
                self.winners.append(card)
        self.step += 1

    @staticmethod
    def gen_bag():
        bag = list(range(1, 91))
        random.shuffle(bag)
        return bag

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number',
                        help='players number',
                        default=1,
                        type=int)
    args = parser.parse_args()

    cards = [Card(Player(f"J_{i}_hn")) for i in range(args.number)]
    game = Game(cards)
    for step in game:
        pass
