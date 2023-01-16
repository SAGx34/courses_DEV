/*
* Carlos Sag Vinos
* Tipos de datos mapa o objetos literales
*/

void main() {
  Map<String, dynamic> Trainer = {"age": 27, "name": "Norder", "ID": 010995};
  print(Trainer["age"]);
  print(Trainer["name"]);
  print(Trainer["ID"]);

  Map<String, dynamic> pokemon = {
    "ID": 1,
    "name": "Bulbasur",
    "type": ["Plant", "Poison"],
    "caught": true,
    "stats": {"level": 5, "hp": 30, "attack": 15, "def": 25}
  };
  print(pokemon);
}
