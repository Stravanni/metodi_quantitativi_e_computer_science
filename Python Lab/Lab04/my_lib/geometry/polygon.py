from  my_lib.geometry.coordinates import Coordinate

class General_Polygon:
    def __init__(self, num_edges):
        self._num_edges=num_edges
        self._name=""

    def get_area(self):
        pass

    def get_name(self):
        return self._name

class Triangle(General_Polygon):
    def __init__(self, a: Coordinate, b: Coordinate, c: Coordinate):
        super().__init__(3)
        self._a = a
        self._b = b
        self._c = c
        self._name="triangle"
    
    def get_area(self):
        x1, y1, x2, y2, x3, y3 = self._a.x, self._a.y, self._b.x, self._b.y, self._c.x, self._c.y
        return abs(0.5 * (((x2-x1)*(y3-y1))-((x3-x1)*(y2-y1))))