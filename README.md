# paises-flask-2687386

# COMANDOS DE PYTHON (EN CONSOLA)
- Inicial:
- - Debemos tener instalado el python y el pip, el modo a seguir será primero tener descargado el proyecto de GitHub descargado en nuestro ordenador, lo descargaremos desde la consola usando los comandos básicos de git (git clone o git init) 
- - Debemos usar "pip install flask" el cual nos servirá para instalar todas las dependencias del proyecto.
- - Tenemos que crear un disco virtual con el comando "pip install virtualenv" en la ruta donde tenemos el proyecto de Git, despues usaremos "python -m env (nombre del entorno, generalmente nombrado env)" el cual ya creará la maquina virtual.
- - Para poder activar la máquina virtual debemos hacer uso del comando ".\venv(nombre del entorno virtual)\Scripts\activate"
- - Luego, para almacenar las dependencias que instalamos, usaremos el comando "pip freeze > requirements.txt" el cual nos creará un archivo de texto en donde nos mostrará las dependencias instaladas