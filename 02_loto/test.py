from loto import Player, Card, Game

def test_player():
    player = Player("Alex")
    assert player.name == "Alex"


def test_gen_bag():
    player = Player("Alex")
    card = Card(player)
    assert len(card._card) == 15


def test_gen_valid_values():
    bag = Game.gen_bag()
    for elem in bag:
        assert 0 < elem < 91


def test_remove_n():
    player = Player("Alex")
    card = Card(player)
    card_dublicate = card._card[:]
    card._check(card._card[-1])
    assert card._card == card_dublicate[:-1]
