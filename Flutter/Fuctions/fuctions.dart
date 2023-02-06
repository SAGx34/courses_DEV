import '../Variables/const_final.dart';

void main() {
  int sumar = sum(5, 10);
  int restar = resta(10, 5);
  print(sumar);
  print(restar);
}

int sum(int a, int b) {
  return a + b;
}

int resta(int a, int b) {
  return a - b;
}
