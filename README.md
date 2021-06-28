# arc-publisher

Permite crea, categorizar y publicar notas en Arc Publishing a través de la API Draft

Prerequisitos:
- node 10.20
- python 3.6

Instalación:
- Clonar el proyecto
- De preferencia crear un virtualenv para Python usando la versión 3.6 del lenguaje
    virtualenv arc-publisher --python=python3
  Activamos el virtualenv
- Instalamos las dependencias de nodejs
    npm i
- Instalamos las dependencias de python
    pip install -r requirements.txt
- Activamos el servidor wsgi de Flask para probar las funciones definidas
    sls wsgi serve
- Listo
