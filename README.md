# 🚀 FastAPI Customer & Invoice API

API REST construida con **FastAPI** para la gestión de clientes, transacciones e invoices (facturas), diseñada como práctica de desarrollo backend profesional en Python.

Este proyecto simula un sistema de gestión donde actualmente los datos se almacenan en memoria y posteriormente se integrará persistencia con SQLite.

---

## 🧠 Objetivo del Proyecto

Desarrollar una API backend moderna aplicando:

* FastAPI
* Pydantic (validación de datos)
* Arquitectura modular
* Buenas prácticas para portafolio backend

---

## 📂 Estructura del Proyecto

```
fastapi-project/
│
├── main.py          # Endpoints de la API
├── models.py        # Modelos Pydantic (Customer, Transaction, Invoice)
├── db.py            # Lógica de base de datos (en desarrollo)
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación del proyecto
```

---

## ⚙️ Tecnologías Utilizadas

* Python 3.10+
* FastAPI
* Pydantic
* Uvicorn
* ZoneInfo (manejo de zonas horarias)

---

## 📦 Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/fastapi-project.git
cd fastapi-project
```

### 2. Crear entorno virtual (WSL recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor

```bash
uvicorn main:app --reload
```

Servidor disponible en:

```
http://127.0.0.1:8000
```

Documentación automática:

```
http://127.0.0.1:8000/docs
```

---

## 🌎 Endpoints Disponibles

### 🔹 Root

```
GET /
```

Retorna un mensaje de bienvenida.

### 🔹 Obtener hora por país

```
GET /time/{iso_code}
```

Ejemplo:

```
/time/CO
/time/MX
```

---

### 👤 Clientes

#### Crear cliente

```
POST /customers
```

#### Listar clientes

```
GET /customers
```

Los clientes se almacenan actualmente en memoria (lista simulando base de datos).

---

### 💳 Transacciones

```
POST /transactions
```

Permite registrar transacciones asociadas a invoices.

---

### 🧾 Facturas (Invoices)

```
POST /invoices
```

Incluye:

* Cliente
* Lista de transacciones
* Total de la factura

---

## 🏗️ Estado del Proyecto

🔹 Versión actual: MVP (datos en memoria)  
🔹 Próximo paso: Persistencia con SQLite  

### 🗺️ Roadmap del Proyecto

#### 🔹 Backend
- [ ] Implementar base de datos SQLite
- [ ] CRUD completo con persistencia
- [ ] Validaciones avanzadas
- [ ] Autenticación con JWT

#### 🎨 Frontend
- [ ] Desarrollo de interfaz web (HTML, CSS, JavaScript)
- [ ] Conexión del frontend con la API backend
- [ ] Dashboard interactivo para gestión de datos

#### ☁️ Producción & DevOps
- [ ] Dockerización del proyecto
- [ ] Despliegue en la nube (Render / Railway / AWS)
- [ ] Configuración de variables de entorno
- [ ] Documentación de la API


---

## 👨‍💻 Autor

**Edwin Granada**  
Ingeniero Físico | Backend Developer  
Enfoque: Python, APIs, Automatización y Data

---

## 📌 Notas Técnicas

* Uso de Pydantic para validación de esquemas
* Arquitectura modular separando modelos y lógica
* API preparada para futura integración con base de datos
* Desarrollo ejecutado en entorno WSL (Linux)
