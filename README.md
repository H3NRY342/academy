---

# 🚀 Proyecto FastAPI - Academy API

Este proyecto es una API REST construida con **FastAPI**, diseñada para ser modular, escalable y mantenible. Incluye autenticación con **JWT**, acceso a base de datos mediante **SQLAlchemy**, validación de datos con **Pydantic**, y sigue el patrón de diseño **Abstract Factory Method** para la creación de objetos desacoplados.

---

## ⚙️ Pasos para ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_PROYECTO>
```

---

### 2. Crear y activar un entorno virtual (recomendado)

#### En **Linux / MacOS**:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### En **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar las dependencias

Una vez activado el entorno virtual, instala los paquetes necesarios:

```bash
pip install -r requirements.txt
```

---

### 4. Configurar las variables de entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```dotenv
DB_ENGINE=mysql
DB_NAME=academy
DB_USER=xxxxxxxxxxx
DB_PASSWORD=xxxxxxxxxxx
DB_HOST=xxxxxxxxxxx
DB_PORT=xxxxxxxxxxx
SECRET_KEY=xxxxxxxxxxx
```

---

### 5. Inicializar la base de datos con datos precargados

El proyecto incluye un script SQL para poblar la base de datos con información inicial.

Ejecuta el script en tu servidor MySQL:

```bash
mysql -u root -p academy < scripts/init_db.sql
```

---

### 6. Ejecutar el servidor de desarrollo

Inicia el servidor FastAPI utilizando **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

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

Este proyecto implementa el **Abstract Factory Method** para desacoplar la lógica de creación de objetos, permitiendo una mayor flexibilidad y escalabilidad.

Puedes leer más sobre este patrón aquí:  
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
scripts/
└── init_db.sql                      # Script para cargar datos iniciales
```

---

## 📚 Documentación de la API

FastAPI genera automáticamente la documentación de la API. Puedes acceder a ella una vez el servidor esté corriendo:

- Swagger UI:  
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- ReDoc:  
  👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## ✅ Requisitos previos

- Python 3.10+
- MySQL 
- Pip

---

## 📝 Notas adicionales

- Las credenciales proporcionadas son solo para entornos de desarrollo. **No uses estas credenciales en producción**.
- Recuerda activar el entorno virtual cada vez que trabajes en el proyecto.

---
