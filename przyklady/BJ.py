import karty, gry

class BJ_Card(karty.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            else:
                v = None
            return  v

class BJ_Deck(karty.Deck):
  def populate(self):
    for suit in BJ_Card.SUITS:
      for rank in BJ_Card.RANKS:
        self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(karty.Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep = rep + "(" +str(self.total) + ")"
            return  rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

    t = 0
    for card in self.cards:
        t = t + card.value

    contains_ace = False
    for card in self.cards:
        if card.value == BJ_Card.ACE_VALUE:
            contains_ace = True

    if contains_ace and t <= 11:
        t += 10
    return t

    def is_busted(self):
        return self.total > 21