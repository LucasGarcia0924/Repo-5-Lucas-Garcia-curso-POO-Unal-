# Reto 5 POO
Para el quinto reto se pide convertir el programa "Shape" en un paquete de dos métodos distintos.
***
## Logo del grupo
![Logo](https://github.com/NotName-K/POO-R2/blob/main/Screenshot%202025-09-23%20110719.png?raw=true)

## Módulo único
*** 
En este método simplemente se pone el archivo dentro de un paquete "paquete_unico", y se ingresa el archivo Shape junto al __init__ con este, por fuera la función main().
```
paquete_unico/
├── paquete/
│   ├── __init__.py
│   └── Shape.py
└── main.py
```
## Módulos separados
*** 
En este método se hace lo contrario al anterior, dentro del paquete ira el __init__ pero también un módulo por cada clase que originalmente se encontraba en un archivo, pero que de igual forma es llamada por la función main fuera del paquete.
```
paquete_separado/
├── paquete/
│   ├── __init__.py
│   ├── Shape.py
│   ├── Point.py
│   ├── Line.py
│   ├── Triangle.py
│   ├── Scalene.py
│   ├── Isosceles.py
│   ├── Equilateral.py
│   ├── TriRectangle.py
│   ├── Rectangle.py
│   └── Square.py
└── main.py
```
Ambos paquetes se pueden consultar para probar el código. : )
