# Paquetes
### 1. ¿Qué son los paquetes en Python?
Los paquetes permiten estructurar jerárquicamente los módulos que hemos definido.

Para inicializar un directorio dentro de nuestro sistema operativo y que Python lo reconozca como un paquete que contiene módulos que pueden importarse, debe crearse un fichero dentro del directorio con el nombre `__init__.py`.

El código de `__init__.py` se invocará cuando el paquete o un módulo del paquete sea imortando en el programa. Esto puede utilizarse para establecer código de inicialización de los paquetes o de los módulos.

Para importar un módulo que se encuentra en un paquete debe utilizarse la sintaxis:
```
import <nombre_paquete>.<nombre_modulo>

from <nombre_paquete>.<nombre_modulo> import <nombre(s)>
```
### 2. Importando todos los módulos de un paquete
Podríamos pensar que para importar todos los módulos de un paquete podríamos utilizar la sintaxis:
```
from <nombre_paquete> import *
```
Sin embargo, ¿qué es lo que sucede?

Python sigue la siguiente convención: si el archivo `__init__.py` en el directorio del paquete contiene una lista llamada `__all__`, se toma como una lista de módulos que deben ser importados cuando se encuentra la sentencia: 
```
from <nombre_paquete> import *.
```

# Dentro del fichero __init__.py del modulo
__all__ = [
    'mimodulo'
]
### 3. Subpaquetes
Los paquetes pueden contener un número arbitrario de paquetes anidados. La sintaxis que se utiliza para acceder a los modulos que se encuentran en los paquetes anidados es similar a la anterior pero añadiendo algunos `.` adicionales:
```
from <nombre_paquete>.<nombre_subpaquete>.<nombre_modulo> import <nombre(s)>
```


