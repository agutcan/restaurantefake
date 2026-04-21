# Codigo & Sabor

Aplicacion de gestion para restaurante con frontend multipagina y backend API. El proyecto usa FastAPI, PostgreSQL y Docker Compose para ejecutar todo en local con un solo comando.

## Caracteristicas

- Menu digital conectado a base de datos.
- Creacion de pedidos por cantidades.
- Control de pagos (efectivo y tarjeta).
- Tablero de pedidos con estados por color.
- Interfaz responsive en espanol.

## Stack tecnico

- Backend: Python 3.12, FastAPI, SQLAlchemy, Uvicorn.
- Base de datos: PostgreSQL 16.
- Frontend: HTML, CSS, JavaScript vanilla y Bootstrap local.
- Infraestructura: Dockerfile + docker compose.

## Estructura principal

```text
restauranteFake/
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── services.py
├── assets/
│   └── bootstrap.min.css
├── app.js
├── styles.css
├── index.html
├── pedidos.html
├── pagos.html
├── pedidos-estado.html
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Ejecucion local

1. Construir y levantar servicios:

```bash
docker compose up -d --build
```

2. URLs principales:

- Aplicacion: http://localhost:8001
- Salud API: http://localhost:8001/health
- Swagger: http://localhost:8001/docs

3. Ver logs:

```bash
docker compose logs -f api
```

4. Parar servicios:

```bash
docker compose down
```

## Flujo de la aplicacion

1. index.html
   - Muestra portada y menu desde GET /dishes.
2. pedidos.html
   - Permite seleccionar platos y crear pedido con POST /orders.
3. pagos.html
   - Carga pedido con GET /orders/{order_id} y registra pago con POST /orders/{order_id}/payments.
4. pedidos-estado.html
   - Lista todos los pedidos con GET /orders y refresca cada 15 segundos.

## Endpoints

- GET /health
- GET /dishes
- POST /orders
- GET /orders
- GET /orders/{order_id}
- POST /orders/{order_id}/payments

## Variables de entorno (compose)

- POSTGRES_DB=restaurante
- POSTGRES_USER=app_user
- POSTGRES_PASSWORD=app_pass
- DATABASE_URL=postgresql+psycopg2://app_user:app_pass@db:5432/restaurante

## Notas de desarrollo

- El frontend se sirve como estatico desde FastAPI.
- Si cambias HTML, CSS o JS con Docker, reconstruye: docker compose up -d --build.
- Si abres archivos por file://, app.js usa http://localhost:8001 como fallback de API_BASE.