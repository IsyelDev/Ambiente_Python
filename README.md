# Guía para trabajar con entornos en Conda y Jupyter Notebook

Este es un proceso paso a paso para crear, gestionar entornos en Conda, e instalar Jupyter Notebook.

# Proyecto con Anaconda
Este es un proyecto que utiliza Anaconda para la creación de entornos y la instalación de dependencias necesarias.
## Requisitos previos
- Tener [Anaconda](https://www.anaconda.com/products/distribution) instalado en tu sistema.

![Descripción de la imagen 1](https://github.com/IsyelDev/Ambiente_Python/blob/main/Captura%20de%20pantalla%202025-01-16%20205543.png)

![Descripción de la imagen 2](https://github.com/IsyelDev/Ambiente_Python/blob/main/segundo.png)


## Pasos a seguir

### 1. **Abrir Anaconda**
   - Inicia **Anaconda Navigator** desde el menú de inicio (Windows) o desde la terminal (Linux/macOS).

### 2. **Verificar la lista de ambientes con `conda env list`**
   - Abre la terminal o Anaconda Prompt y escribe el siguiente comando para ver todos los entornos de Conda disponibles:
   ```bash
   conda env list
   ```

### 3. **Crear un nuevo `entorno`**
   - Para crear un entorno llamado pegasus_fantasy con Python 3.13, ejecuta el siguiente comando (aunque puede que 3.13 no esté disponible, intenta con una versión más estable si es necesario):
 ```bash
conda create --name pegasus_fantasy python=3.13  
```
## Si Python 3.13 no está disponible, puedes probar con Python 3.10:
 ```bash
conda create --name pegasus_fantasy python=3.10
```
### 4. Eliminar un entorno
Si deseas eliminar el entorno pegasus_fantasy que creaste, utiliza el siguiente comando:
```bash
conda remove --name pegasus_fantasy --all
```
### 5. Activar el entorno y abrir Anaconda Navigator
Para activar el entorno, utiliza el siguiente comando:
```bash
conda activate pegasus_fantasy
```
# Luego, abre Anaconda Navigator y ve a la pestaña Home.
### 6. Instalar Jupyter Notebook desde Anaconda Navigator
Dentro de Anaconda Navigator, en la pestaña Home, busca la opción Jupyter Notebook en la lista de aplicaciones.
Haz clic en Install si aún no está instalado y luego en Launch para abrir Jupyter Notebook.
### 7. Instalar dependencias en Jupyter Notebook
Dentro de Jupyter Notebook, si necesitas instalar dependencias, puedes usar el siguiente comando en una celda:
```bash
!pip install nombre_paquete
```
#### Nota: Aunque este comando puede funcionar, es preferible usar Conda desde la terminal del entorno, ya que conda gestiona mejor las dependencias.
### 8. Uso de conda y pip
Se recomienda usar conda para instalar paquetes siempre que sea posible, ya que conda maneja mejor las dependencias.
Si necesitas usar pip, asegúrate de que el entorno en el que estás instalando es el correcto y que Jupyter tiene acceso a los paquetes.
Resumen de Comandos
Crear un entorno:

```bash
conda create --name pegasus_fantasy python=3.x
```
Verificar entornos:
```bash
conda env list
```
Eliminar un entorno:

```bash
conda remove --name pegasus_fantasy --all
```
#### Instalar Jupyter: Desde la pestaña Home de Anaconda Navigator, haz clic en Install y luego en Launch.

Instalar dependencias en Jupyter:

```bash
!pip install nombre_paquete
```


# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
