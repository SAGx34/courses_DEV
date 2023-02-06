// Funcion para contar palabras de un texto

void main() {
  String content =
      "Hola mundo, hoy es martes, mañana es nochebuena, pasado mañana es navidad. Hoy es vispera de nochebuena y mañana vispera de navidad.";
  print(wordsCounter(content, "es"));
}

String wordsCounter(String text, String query) {
  Map<String, int> counterMap = {};
  List<String> wordList = text.split(" ");
  for (String word in wordList) {
    word = normalize(word);
    if (counterMap.containsKey(word)) {
      counterMap[word] = counterMap[word]! + 1;
    } else {
      counterMap[word] = 1;
    }
  }

  query = normalize(query);
  return "La palabra $query se repite: ${counterMap[query] ?? 0} veces";
}

String normalize(String word) {
  return word.toLowerCase().replaceAll(RegExp("[,.]"), " ");
}
