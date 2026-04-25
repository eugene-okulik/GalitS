class Flower:
    def __init__(self, name, color, stem_length, freshness, price, lifetime):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.price = price
        self.lifetime = lifetime


class Rose(Flower):
    pass


class Tulip(Flower):
    pass


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(f.price for f in self.flowers)

    def average_lifetime(self):
        return sum(f.lifetime for f in self.flowers) / len(self.flowers)

    def sort_by(self, param):
        self.flowers.sort(key=lambda f: getattr(f, param))

    def find_by(self, param, value):
        return [f for f in self.flowers if getattr(f, param) == value]
