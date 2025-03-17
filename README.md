# 🚀 Proyecto FastAPI - Academy API

Este proyecto es una API REST construida con **FastAPI**, diseñada para ser modular, escalable y mantenible. Incluye autenticación con **JWT**, acceso a base de datos mediante **SQLAlchemy**, validación de datos con **Pydantic**, y sigue el patrón de diseño **Abstract Factory Method** para la creación de objetos desacoplados.

---

## ⚙️ Comandos para ejecutar el proyecto

1. **Clona el repositorio:**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <CARPETA_DEL_PROYECTO>
   ```

2. **Instala las dependencias del proyecto:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configura las variables de entorno:**

   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

   ```dotenv
   DB_ENGINE=mysql
   DB_NAME=academy
   DB_USER=XXXXXXXXXX
   DB_PASSWORD=XXXXXXXXXXX
   DB_HOST=XXXXXXXXX
   DB_PORT=XXXXXXXX
   SECRET_KEY=XXXXXXX
   ```

4. **Carga el script SQL con los datos iniciales:**

   Se incluye un script SQL para iniciar la base de datos con datos precargados. Puedes encontrarlo en la carpeta `/scripts`:

   ```bash
   mysql -u root -p academy < scripts/init_db.sql
   ```

5. **Levanta el servidor de desarrollo:**

   ```bash
   uvicorn app.main:app --reload
   ```

   La aplicación estará disponible en:

   ```
   http://127.0.0.1:8000
   ```

---

## 🛠️ Tecnologías utilizadas

- **FastAPI**: Framework para el desarrollo rápido de APIs.
- **SQLAlchemy**: ORM para la interacción con bases de datos.
- **Pydantic**: Manejo de validaciones y serialización de datos.
- **JWT**: Autenticación segura con JSON Web Tokens.
- **MySQL**: Base de datos relacional.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.

---

## 📐 Patrón de Diseño: Abstract Factory Method

Se ha implementado el **Abstract Factory Method** para desacoplar la creación de repositorios y servicios, facilitando la escalabilidad del proyecto.

Puedes aprender más sobre este patrón en la siguiente documentación:
👉 [Abstract Factory Method - Refactoring Guru](https://refactoring.guru/design-patterns/abstract-factory)

---

## 📂 Estructura del Proyecto

```
app/
│
├── main.py                          # Punto de entrada de la aplicación FastAPI
├── api/
│   └── v1/
│       └── endpoints/
│           └── users.py             # Rutas y controladores del módulo de usuarios
├── core/
│   └── factory.py                   # Implementación del patrón Abstract Factory
├── models/
│   └── user.py                      # Modelos SQLAlchemy para la base de datos
├── repositories/
│   ├── base.py                      # Repositorio base (interfaz)
│   ├── memory_user_repository.py    # Repositorio en memoria (implementación temporal)
│   └── sql_user_repository.py       # Repositorio con acceso a base de datos SQL
└── services/
    └── user_service.py              # Lógica de negocio del módulo de usuarios
```

---

## 📚 Documentación de la API

FastAPI genera automáticamente la documentación interactiva:

- Swagger UI:  
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- ReDoc:  
  👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## ✅ Requisitos previos

- Python 3.9+
- MySQL Server
- Pip

---

## 📝 Notas adicionales

- El proyecto incluye un archivo `scripts/init_db.sql` para cargar datos de prueba y empezar a utilizar la API de inmediato.
- Las credenciales de la base de datos y el `SECRET_KEY` se gestionan a través de variables de entorno declaradas en el archivo `.env`.
- Se recomienda **NO usar las credenciales de ejemplo en producción**.

---
