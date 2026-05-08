import datetime
import json


def read_file(filename):
    file_data = open(filename, 'r')
    data = json.load(file_data)
    file_data.close()
    return data


class Flower:
    def __init__(self, filename):
        data = read_file(filename)
        self.lifetime = data.get('lifetime')
        self.privoz = datetime.datetime.strptime(
            data['privoz'],
            '%d/%m/%Y'
        ).date()
        self.color = data.get('color')
        self.freshness = (datetime.date.today() - self.privoz).days

    def __repr__(self):
        return f'{self.__class__.__name__}(color={self.color}, freshness={self.freshness} дней)'


class Roses(Flower):
    def __init__(self, filename):
        super().__init__(filename)


class Asters(Flower):
    def __init__(self, filename):
        super().__init__(filename)


class Gerberas(Flower):
    def __init__(self, filename):
        super().__init__(filename)


class Bouquet:
    def __init__(self, *flowers):
        self.flowers = list(flowers)

    def sort_by_freshness(self):
        return sorted(self.flowers, key=lambda x: x.freshness)

    def sort_by_color(self):
        return sorted(self.flowers, key=lambda x: x.color)

    def avg_freshness(self):
        return sum(x.freshness for x in self.flowers) / len(self.flowers)


rose = Roses('roses.txt')
aster = Asters('asters.txt')
gerbera = Gerberas('gerberas.txt')
bouquet = Bouquet(rose, aster, gerbera)

print(bouquet.avg_freshness())
print(bouquet.sort_by_freshness())
