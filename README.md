base de datos:

https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/

Instalación de proyecto

Necesario entorno virtual

python -m venv venv

Entran al entorno y instalan el requierments.txt que está en la carpeta requierments

pip install -r base.txt

después instalan la dependencia local para hacer la carpeta un modulo propio.

pip install -e .

(ejecutan ese comando en la ruta donde se encuentre el archivo pyproject.toml