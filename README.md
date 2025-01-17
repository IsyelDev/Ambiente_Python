# Proyecto con Anaconda
Este es un proyecto que utiliza Anaconda para la creación de entornos y la instalación de dependencias necesarias.
## Requisitos previos
- Tener [Anaconda](https://www.anaconda.com/products/distribution) instalado en tu sistema.
## Crear un nuevo entorno
Para crear un nuevo entorno en Anaconda, utiliza el siguiente comando en tu terminal:
`conda create --name nombre_del_entorno python=3.x`
Reemplaza `nombre_del_entorno` con el nombre que desees para tu entorno y `3.x` con la versión de Python que prefieras.
## Activar el entorno
Una vez que el entorno esté creado, puedes activarlo con el siguiente comando:
`conda activate nombre_del_entorno`
## Instalar dependencias
Para instalar las dependencias necesarias para este proyecto, puedes usar un archivo `requirements.txt` o instalar los paquetes manualmente. Aquí hay un ejemplo de cómo hacerlo.
### Opción 1: Instalación manual de dependencias
Instala los paquetes uno por uno usando `conda` o `pip`. Ejemplo:
`conda install numpy pandas matplotlib`
Si alguna de las dependencias no está disponible en el repositorio de `conda`, puedes usar `pip`:
`pip install nombre_paquete`
### Opción 2: Usando un archivo `environment.yml`
Si tienes un archivo `environment.yml` que contiene todas las dependencias, puedes crear un entorno directamente desde ese archivo. El archivo `environment.yml` tiene el siguiente formato:
```yaml
name: nombre_del_entorno
channels:
  - defaults
dependencies:
  - python=3.x
  - numpy
  - pandas
  - matplotlib
  - pip
  - pip:
      - nombre_paquete_extra
