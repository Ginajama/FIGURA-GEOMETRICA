from FiguraGeometrica import FiguraGeometrica
from COLOR import Color

class RECTANGULO(FiguraGeometrica, Color):
    def __init__(self, alto=0, ancho=0, color=None):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self,color)

    def __str__(self):
        return f"Rectángulo -> {self.__dict__.__str__()}"

if __name__ == "__main__":
    r1 = RECTANGULO(alto=5,ancho=3, color="Rojo")
    print(r1)
    print(f'Area: {r1.area()}')
    print(f'Perimetro: {r1.perimetro()}')