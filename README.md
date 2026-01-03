# Flask Notes

Una aplicación de notas simple construida con Flask y Bootstrap.

## 🚀 Demo

**Deploy:** [https://flask-blog-production.up.railway.app/](https://flask-blog-production.up.railway.app/)

## 📋 Características

- Registro y autenticación de usuarios
- Crear, editar y eliminar notas
- Ver notas de todos los usuarios
- Base de datos SQLite
- Interfaz con Bootstrap

## 🛠️ Tecnologías

- Python 3
- Flask 3.1.2
- SQLite3
- Bootstrap
- Gunicorn

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Kenkyoo/flask-notes.git
cd flask-notes
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Inicializa la base de datos:
```bash
flask --app flaskr init-db
```

4. Ejecuta la aplicación:
```bash
flask --app flaskr run
```

La aplicación estará disponible en `http://127.0.0.1:5000`

## 📁 Estructura
```
flaskr/
├── __init__.py      # Configuración de la app
├── auth.py          # Autenticación
├── notes.py          # Rutas del blog
├── db.py            # Base de datos
├── schema.sql       # Estructura de la BD
└── templates/       # Plantillas HTML
```

## 🔑 Funcionalidades

- **Registro/Login:** Autenticación de usuarios
- **Crear Nota:** Usuarios pueden crear notas
- **Editar/Eliminar:** Solo el autor puede modificar sus notas
- **Ver Notas:** Todos pueden ver las notas publicadas

## 📄 Licencia

MIT

## 👤 Autor

[Kenkyoo](https://github.com/Kenkyoo)
