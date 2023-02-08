import 'setterGetters.dart';

void main() {
  User Jumbo = User("Jumbito", "Mimbo");

  Jumbo.password = "Mimbotex";
  print(Jumbo.username);
  print(Jumbo.password);
}
