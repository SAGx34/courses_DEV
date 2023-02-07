class Dog {
  String name;
  String race;
  int age;
  double height;

  Dog(
      {required this.name,
      required this.race,
      required this.age,
      required this.height});

  void eat() {
    print("$name esta comiendo");
  }

  void bark() {
    print("$name esta ladrando");
  }
}
