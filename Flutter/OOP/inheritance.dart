abstract class PolygonShape {
  String name;
  double area;
  double perimeter;

  PolygonShape(this.name, this.area, this.perimeter);

  void hello() {
    print(this.name);
  }
}

class Square extends PolygonShape {
  double side;
  Square(this.side) : super("Cuadrado", 0.0, 0.0);
  double calculatedArea() {
    this.area = this.side * this.side;
    return this.area;
  }

  double calculatePerimeter() {
    this.perimeter = this.side + this.side + this.side + this.side;
    return this.perimeter;
  }
}
