# Restaurante Digital (Python + PostgreSQL + Docker)

Backend minimo para gestionar:
- Menu digital (platos)
- Automatizacion de pedidos
- Control de pagos

## Requisitos
- Docker Desktop
- Docker Compose

## Levantar proyecto

```bash
docker compose up --build
```

API disponible en:
- http://localhost:8001
- Documentacion Swagger: http://localhost:8001/docs

## Endpoints

### 1) Ver platos

```http
GET /dishes
```

### 2) Crear pedido

```http
POST /orders
Content-Type: application/json

{
  "items": [
    { "dish_id": 1, "quantity": 2 },
    { "dish_id": 3, "quantity": 1 }
  ]
}
```

### 3) Ver pedido

```http
GET /orders/{order_id}
```

### 4) Pagar pedido

```http
POST /orders/{order_id}/payments
Content-Type: application/json

{
  "method": "cash",
  "amount_paid": 35.00
}
```

- `method`: `cash` o `card`
- Si el pago es en efectivo y sobra dinero, devuelve cambio.

## Apagar servicios

```bash
docker compose down
```

Si quieres borrar tambien los datos persistidos de Postgres:

```bash
docker compose down -v
```
# restaurantefake
