import 'Dog.dart';

void main() {
  Dog dog1 =
      new Dog(name: "Jumbo", race: "American Standford", age: 4, height: 28.5);
  Dog dog2 = new Dog(name: "Linda", race: "Fake Tekker", age: 12, height: 32.7);
  print(dog1.name);
  print(dog2.name);

  dog1.bark();
  dog2.eat();
}
