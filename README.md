# 🍽️ Restaurante Digital - Sistema de Gestión

Un sistema completo de gestión digital de restaurantes con backend API RESTful y frontend web responsivo. Construido con **Python + FastAPI**, **PostgreSQL**, **Docker** y **JavaScript vanilla**.

## 📋 Características

✅ **Menú digital** - Visualización de platos disponibles
✅ **Sistema de pedidos** - Creación y gestión de órdenes
✅ **Procesamiento de pagos** - Soporte para efectivo y tarjeta
✅ **Cálculo automático** - Subtotal, total e cambio
✅ **Interfaz 100% en español** - UI completamente localizada
✅ **Responsivo** - Funciona en desktop, tablet y móvil
✅ **Docker Ready** - Deploy con un comando

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────┐
│       Frontend (JavaScript)         │
│  • index.html (Portal)              │
│  • menu.html (Menú)                 │
│  • pedidos.html (Órdenes)           │
│  • pagos.html (Pagos)               │
│  • app.js (Cliente compartido)      │
│  • styles.css (Estilos)             │
└──────────────┬──────────────────────┘
               │
         HTTP/REST (JSON)
               │
┌──────────────▼──────────────────────┐
│    Backend API (FastAPI)            │
│  • GET /dishes                      │
│  • POST /orders                     │
│  • GET /orders/{id}                 │
│  • POST /orders/{id}/payments       │
│  • GET /health                      │
└──────────────┬──────────────────────┘
               │
      SQLAlchemy ORM
               │
┌──────────────▼──────────────────────┐
│     PostgreSQL Database             │
│  • Platos (Dishes)                  │
│  • Órdenes (Orders)                 │
│  • Ítems de orden (OrderItems)      │
│  • Pagos (Payments)                 │
└─────────────────────────────────────┘
```

---

## 🛠️ Tecnologías

**Backend:**
- Python 3.12
- FastAPI (API web)
- SQLAlchemy (ORM)
- Uvicorn (ASGI server)
- PostgreSQL 16 (Base de datos)

**Frontend:**
- HTML5 + CSS3
- JavaScript ES6+ (vanilla, sin frameworks)
- Fetch API (comunicación con backend)

**DevOps:**
- Docker & Docker Compose
- AWS EC2 (para producción)

---

## 📁 Estructura de Archivos

```
restauranteFake/
├── app/                          # Backend FastAPI
│   ├── main.py                  # Aplicación principal y endpoints
│   ├── database.py              # Configuración de SQLAlchemy
│   ├── models.py                # Modelos ORM (Dish, Order, etc)
│   ├── schemas.py               # Esquemas Pydantic (validación)
│   └── services.py              # Lógica de negocio
│
├── Frontend (raíz)
│   ├── index.html               # Portal principal (menú de acceso)
│   ├── menu.html                # Página de visualización de menú
│   ├── pedidos.html             # Página de creación de órdenes
│   ├── pagos.html               # Página de procesamiento de pagos
│   ├── app.js                   # Cliente compartido (funciones API)
│   └── styles.css               # Estilos globales
│
├── docker-compose.yml           # Orquestación de servicios
├── Dockerfile                   # Imagen de la aplicación
├── requirements.txt             # Dependencias de Python
└── README.md                    # Este archivo
```

---

## 🚀 Uso Local

### Requisitos
- Python 3.12+
- Docker y Docker Compose
- Git

### Instalación y ejecución

1. **Clonar o descargar el proyecto:**
```bash
git clone <repo-url>
cd restauranteFake
```

2. **Iniciar con Docker Compose:**
```bash
docker-compose up -d
```

El sistema estará disponible en:
- **Frontend:** http://localhost
- **API:** http://localhost/health
- **Swagger docs:** http://localhost:8000/docs (si se accede directo a puerto 8000)

3. **Ver logs:**
```bash
docker-compose logs -f api
```

4. **Detener:**
```bash
docker-compose down
```

5. **Eliminar datos persistentes (Postgres):**
```bash
docker-compose down -v
```

---

## 🌐 Despliegue en AWS EC2

### 1. Preparar instancia EC2

```bash
# Conectar a la instancia
ssh -i "tu-clave.pem" ubuntu@tu-dns-ec2

# Actualizar paquetes
sudo apt update && sudo apt upgrade -y

# Instalar Docker
sudo apt install -y docker.io

# Instalar Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Agregar usuario a grupo docker
sudo usermod -aG docker ubuntu
newgrp docker
```

### 2. Descargar el proyecto en EC2

```bash
# Opción A: Desde GitHub
git clone <repo-url>
cd restauranteFake

# Opción B: Desde máquina local con SCP
scp -i "tu-clave.pem" -r ./* ubuntu@tu-dns-ec2:~/restaurante/
```

### 3. Configurar Security Group en AWS

En la consola de AWS:
1. EC2 → Security Groups
2. Selecciona tu security group
3. Edita **Inbound Rules**
4. Agrega:
   - Type: HTTP, Port: 80, Source: 0.0.0.0/0
   - Type: HTTPS, Port: 443, Source: 0.0.0.0/0 (opcional)

### 4. Iniciar la aplicación

```bash
cd ~/restaurante
docker-compose up -d
docker-compose logs -f api
```

La app estará disponible en: `http://tu-dns-ec2.compute-1.amazonaws.com`

---

## 📡 Endpoints API

### GET /health
Verifica que la API esté operativa.

**Response:**
```json
{
  "status": "ok"
}
```

### GET /dishes
Obtiene lista de platos disponibles.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Hamburguesa Código",
    "category": "Plato Principal",
    "description": "La mejor hamburguesa con ingredientes de calidad",
    "price": "12.99",
    "is_active": true
  }
]
```

### POST /orders
Crea una nueva orden.

**Request:**
```json
{
  "items": [
    {
      "dish_id": 1,
      "quantity": 2
    },
    {
      "dish_id": 3,
      "quantity": 1
    }
  ]
}
```

**Response:**
```json
{
  "id": 42,
  "items": [
    {
      "dish_id": 1,
      "dish_name": "Hamburguesa Código",
      "quantity": 2,
      "price": "12.99",
      "subtotal": "25.98"
    }
  ],
  "subtotal": "25.98",
  "total": "25.98",
  "status": "pending"
}
```

### GET /orders/{order_id}
Obtiene una orden específica.

### POST /orders/{order_id}/payments
Procesa el pago de una orden.

**Request:**
```json
{
  "amount_paid": "30.00",
  "method": "cash"
}
```

**Response:**
```json
{
  "id": 1,
  "order_id": 42,
  "amount_paid": "30.00",
  "change": "4.02",
  "method": "cash",
  "status": "approved",
  "created_at": "2026-04-20T16:45:30"
}
```

---

## 💾 Modelos de Base de Datos

### Dishes (Platos)
Tabla con información de platos disponibles.

### Orders (Órdenes)
Tabla con órdenes creadas por clientes.

### OrderItems (Ítems de orden)
Tabla de relación que conecta órdenes con platos y sus cantidades.

### Payments (Pagos)
Tabla con información de pagos realizados.

---

## 🎨 Frontend - Flujo de Usuario

### 1. **index.html** - Portal Principal
Página de entrada con tres opciones:
- 🍽️ Ver Menú
- 📝 Crear Pedido
- 💳 Procesar Pago

### 2. **menu.html** - Visualización del Menú
- Carga automática de platos desde API `/dishes`
- Muestra nombre, categoría, descripción y precio
- Diseño responsivo con grid CSS

### 3. **pedidos.html** - Creación de Órdenes
- Selecciona cantidad de cada plato
- Calcula subtotal en tiempo real
- Envía orden a API `/orders`
- Muestra ID de orden y estado (traducido a español)

### 4. **pagos.html** - Procesamiento de Pagos
- Ingresa ID de orden
- Selecciona método de pago (Efectivo/Tarjeta)
- Ingresa monto pagado
- Calcula cambio automáticamente
- Muestra estado del pago en español

---

## 🌍 Localización

Todos los textos de la UI están en **español** con acentos correctos. Además, los estados internos del API se traducen automáticamente:

**En app.js:**
```javascript
// Traducción de estados de orden
pending → Pendiente
paid → Pagado

// Traducción de estados de pago
approved → Aprobado

// Traducción de métodos de pago
cash → Efectivo
card → Tarjeta
```

Esto permite mantener la API en inglés (buena práctica) mientras el usuario ve todo en español.

---

## ⚙️ Configuración

### Variables de Entorno (docker-compose.yml)

```yaml
DATABASE_URL: postgresql+psycopg2://app_user:app_pass@db:5432/restaurante
```

Para cambiar la contraseña de la base de datos, edita el `docker-compose.yml` en ambos servicios (`db` y `api`).

---

## 🔧 Troubleshooting

### "Not Found" al acceder a la web
**Solución:** Verifica que el Dockerfile copia los archivos HTML, CSS y JS:
```dockerfile
COPY *.html ./
COPY *.css ./
COPY *.js ./
```

### API devuelve 404 para `/dishes`
**Solución:** El mounting de `StaticFiles` debe estar **al final** de `main.py`, después de todos los endpoints.

### Conexión rechazada a PostgreSQL
**Solución:** Verifica que el servicio `db` está sano:
```bash
docker-compose logs db
docker-compose ps
```

### Puerto 80 en uso
**Solución:** Cambia el puerto en `docker-compose.yml`:
```yaml
ports:
  - "8080:8000"  # Usa http://localhost:8080
```

### API Base URL incorrecta
El `app.js` usa automáticamente el dominio del servidor:
```javascript
const API_BASE = `${window.location.protocol}//${window.location.host}`;
```

Funciona tanto en local (`localhost`) como en producción (tu DNS de EC2).

---

## 📊 Ejemplo de Uso Completo

```bash
# 1. Consultar menú
curl http://localhost/dishes

# 2. Crear orden (IDs de platos: 1, 2, 3, 4)
curl -X POST http://localhost/orders \
  -H "Content-Type: application/json" \
  -d '{
    "items": [
      {"dish_id": 1, "quantity": 2},
      {"dish_id": 3, "quantity": 1}
    ]
  }'

# Respuesta: {"id": 1, "total": "25.98", "status": "pending", ...}

# 3. Procesar pago
curl -X POST http://localhost/orders/1/payments \
  -H "Content-Type: application/json" \
  -d '{
    "amount_paid": "30.00",
    "method": "cash"
  }'

# Respuesta: {"status": "approved", "change": "4.02", ...}
```

---

## 🎓 Cómo se Creó Este Proyecto

Este proyecto fue desarrollado como un sistema completo de gestión digital de restaurantes, combinando:

1. **Backend robusto** con FastAPI, SQLAlchemy y PostgreSQL
2. **Frontend responsivo** con HTML, CSS y JavaScript vanilla (sin dependencias externas)
3. **Localización completa** con interfaz 100% en español
4. **Infraestructura moderna** con Docker para desarrollo y producción
5. **Despliegue en la nube** listo para AWS EC2

### Decisiones técnicas clave:

- **API-first design:** Backend expone todo como REST, frontend es consumidor puro
- **CORS habilitado:** Permite requests desde cualquier origen
- **Traducción client-side:** Mantiene DB y API en inglés, UI en español para buenas prácticas
- **Archivos estáticos servidos por FastAPI:** Una única imagen Docker que sirve todo
- **Base de datos persistente:** Volumen Docker para PostgreSQL evita pérdida de datos
- **API_BASE dinámica:** El frontend detecta automáticamente el servidor (local o producción)

### Flujo de desarrollo:

1. Se creó el modelo de datos (Dish, Order, OrderItem, Payment)
2. Se implementaron endpoints REST con lógica de negocio
3. Se creó frontend con 4 páginas HTML (portal, menú, pedidos, pagos)
4. Se tradujo toda la UI al español incluyendo estados internos
5. Se configuró Docker para ambiente aislado
6. Se preparó para despliegue en AWS EC2

---

## 📝 Licencia

Este proyecto es de código abierto. Siéntete libre de usarlo y modificarlo.

---

## 👨‍💻 Soporte

Para reportar bugs o sugerir mejoras, abre un issue en el repositorio.

**¡Buen provecho!** 🍴
