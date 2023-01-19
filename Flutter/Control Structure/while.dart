// Bucles con while y do while

import 'dart:io';

void main() {
  List<int> KDA = [4, 0, 1];
  List<String> enemyNames = ["John", "Michael", "Jim", "Will", "Patrick"];
  int i = 0;
  while (i < KDA.length) {
    print(KDA[i]);
    i++;
  }
  int selectedOption;
  do {
    print("Choose a option");
    selectedOption = int.parse(stdin.readLineSync()!);
    switch (selectedOption) {
      case 1:
        print("Option 1");
        break;
      case 2:
        print("Option 2");
        break;
      case 3:
        print("Exiting...");
        break;
      default:
        print("Invalid option");
    }
  } while (selectedOption != 3);
}
