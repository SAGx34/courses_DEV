//Bucles for y sus derivados

void main() {
  List<int> KDA = [4, 0, 1];
  List<String> enemyNames = ["John", "Michael", "Jim", "Will", "Patrick"];

  for (int i = 0; i < KDA.length; i++) {
    print(KDA[i]);
  }

  for (String enemyNames in enemyNames) {
    print(enemyNames);
  }

  for (int i = 1; i <= 10; i++) {
    print(5 * i);
  }

  enemyNames.forEach((enemyNames) {
    print(enemyNames);
  });
}
