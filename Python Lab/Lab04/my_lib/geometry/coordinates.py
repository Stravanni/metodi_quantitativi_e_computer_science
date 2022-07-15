class Coordinate:
    def __init__(self, a, b):
        if type(a)!= int:
            raise ValueError('x must be int')
        elif type(b)!= int:
            raise ValueError('y must be int')
        else:
            self._x = a
            self._y = b
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y