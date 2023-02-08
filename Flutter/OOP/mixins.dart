abstract class Animals {}

abstract class Mamifero extends Animals {}

abstract class Ave extends Animals {}

abstract class Pez extends Animals {}

mixin Volador {
  void volar() {
    print("Vuela");
  }
}

mixin Nadador {
  void nadar() {
    print("Nada");
  }
}

abstract class Caminante {
  void caminar() {
    print("Camina");
  }
}

class Delfin extends Mamifero with Nadador {}

class Murcielago extends Mamifero with Caminante, Volador {}

class Gato extends Mamifero with Caminante {}

class Paloma extends Ave with Caminante, Volador {}

class Pato extends Ave with Caminante, Volador, Nadador {}
