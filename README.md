# Motor-RPG-Python-POO
Sistema de combate e inventario en consola demostrando los pilares de la Programación Orientada a Objetos.
Este proyecto es un motor de lógica por consola desarrollado en Python. Su objetivo principal es demostrar la aplicación practica y estructurada de los 4 pilares fundamentales de la Programación Orientada a Objetos (POO)
## Arquitectura y Conceptos Técnicos Aplicados
- **Clases y Objetos (`__init__`, `self`):** Creación de moldes independientes para entidades del juego, asegurando el encapsulamiento de atributos (Vida, Ataque, Defensa).
- **Herencia (`super()`):** Implementación de la clase `Mago` que hereda las estadísticas base de la clase padre `Personaje`, aplicando el principio DRY (Don't Repeat Yourself).
- **Polimorfismo (Sobrescritura de métodos):** Alteración del método `atacar()` en la clase `Mago` para que implemente un sistema de daño mágico que ignora la defensa rival y consume recursos (Maná), a diferencia del ataque físico estándar.
- **Composición (Objetos dentro de Objetos):** Diseño de un sistema modular donde la clase `Personaje` inicializa y almacena en su interior una instancia de la clase `Inventario`, la cual a su vez administra listas de objetos tipo `Pocion`.

## Tecnologías
- Python 3 (POO, Estructuras de Datos, Control de Flujo, F-Strings).
