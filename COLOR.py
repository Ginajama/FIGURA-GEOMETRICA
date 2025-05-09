class Color:
    def __init__(self, nombre):
        self._Color = nombre

    def __str__(self):
        return f'Color: {self.__dict__.__str__()}'

    @property
    def nombre(self):
        return self._Color

    @nombre.setter
    def nombre(self, nombre):
        self._Color = nombre

if __name__ == '__main__':
    c1 = Color('Rojo')
    print(c1)