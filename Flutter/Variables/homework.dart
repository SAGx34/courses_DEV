/*
Hay tres variables A,B y C. Escriba el codigo necesario para intercambiar
entre si sus valores del siguiente modo:
B toma el valor de A
C toma el valor de B
A toma el valor de C
*/

void main() {
  int valueA = 10, valueB = 20, valueC = 30;
  int tempValue = valueB;

  valueB = valueA;
  valueA = valueC;
  valueC = tempValue;
  print("VALORES: $valueA $valueB $valueC");
}
