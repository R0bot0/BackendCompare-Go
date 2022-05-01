# BDDCovidNews

## Setup environment

### Create a virtual environment

Create a virtualenv with `python3 -m virtualenv env`.
If you don't have virtualenv, install it.

Then, activate the enviroment with

| Linux                     | Windows 10               |
| ------------------------- | ------------------------ |
| `source env/bin/activate` | `.\env\Scripts\activate` |

### Load local configuration

Copy the `.env.example` and rename it to `.env`.
In said file, you can specify variables unique to your environment.

### Load requirements from file

Just run
`python -m pip install -r requirements.txt`

## Cómo crear una APP con un CRUD en Django

1. Se crean los modelos
2. Se crean los serializadores que responden al modelo
3. Se crea el viewset (conjunto de vistas) base
4. Se agrega el viewset al router
5. Se agrega el router a urls.py de la app
6. Se agrega la ruta en urls.py del proyecto.
7. Test
