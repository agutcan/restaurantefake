# Guia de Presentacion Oral (15-20 minutos)

## Proyecto
Transformacion Digital de un Restaurante - Caso Codigo & Sabor

Esta guia esta preparada para explicar de forma clara:
- El problema de negocio del restaurante
- La propuesta de transformacion digital
- La aplicacion construida (frontend + backend + base de datos)
- El despliegue en AWS con Docker y EC2
- Los resultados esperados y siguientes pasos

## 1. Introduccion (0:00 - 2:00)

Guion sugerido:

Buenos dias/tardes. Hoy voy a presentar el caso Transformacion Digital de un Restaurante, aplicado al restaurante Codigo & Sabor.

La idea principal fue pasar de una operacion tradicional, con procesos manuales, a una solucion digital real y funcional. Para ello construimos una aplicacion web completa con base de datos y la desplegamos en la nube usando AWS EC2 y Docker.

El objetivo fue mejorar tres puntos criticos: velocidad de atencion, reduccion de errores y control de pagos.

## 2. Contexto y Problema (2:00 - 4:00)

Guion sugerido:

El restaurante parte de un modelo tradicional:
- Pedidos presenciales manuales
- Cobro en efectivo o tarjeta fisica
- Sin sistema digital integrado

Segun la presentacion, aparecen 4 desafios principales:
1. Errores en pedidos por mala comunicacion entre sala y cocina.
2. Lentitud operativa, sobre todo en horas punta.
3. Control financiero limitado por falta de digitalizacion.
4. Experiencia anticuada para un publico joven y tecnologico.

Este es el problema que queremos resolver.

## 3. Propuesta de Transformacion (4:00 - 6:30)

Guion sugerido:

La propuesta se plantea como una implementacion progresiva, para modernizar sin frenar la operacion diaria.

Fases planteadas:
1. Digitalizacion del menu
2. Automatizacion de pedidos
3. Control de pagos
4. Simulacion de escenarios y formacion
5. Mejora de experiencia y base para escalar

La filosofia es usar tecnologia sencilla pero efectiva: empezar por un MVP funcional que aporte valor inmediato y sirva como base para crecer.

## 4. Solucion Tecnica Implementada (6:30 - 10:00)

Guion sugerido:

Para convertir esa propuesta en algo real, desarrollamos una web app full stack con esta arquitectura:

Frontend:
- HTML, CSS y JavaScript
- Cuatro pantallas: portal, menu, pedidos y pagos

Backend:
- Python con FastAPI
- API REST para consultar platos, crear pedidos y procesar pagos

Base de datos:
- PostgreSQL para guardar platos, ordenes, items de orden y pagos

Infraestructura:
- Docker para empaquetar servicios
- Docker Compose para levantar API y BD juntas

Puntos tecnicos clave:
- API-first, separando frontend y backend
- Validaciones y calculos en backend para evitar errores
- Estados traducidos en frontend para experiencia en espanol
- URL API dinamica para funcionar tanto en local como en produccion

## 5. Demo de Funcionalidades (10:00 - 13:00)

Guion sugerido:

Flujo de uso que se puede mostrar en vivo:

1. Menu digital
- Se cargan platos desde la API con nombre, categoria, descripcion y precio.

2. Creacion de pedidos
- El usuario selecciona cantidades y crea una orden.
- Se genera un ID de pedido para seguimiento.

3. Procesamiento de pagos
- Se introduce ID del pedido, metodo de pago y monto.
- El sistema valida el pago y calcula cambio en efectivo.

Resultados visibles:
- Menos errores manuales
- Mas velocidad en operacion
- Proceso trazable de principio a fin

## 6. Despliegue en AWS (13:00 - 16:00)

Guion sugerido:

Despues del desarrollo local, desplegamos en AWS EC2:

1. Instalamos Docker y Docker Compose en la instancia.
2. Subimos el proyecto al servidor.
3. Levantamos servicios con docker compose up.
4. Abrimos puerto HTTP en Security Group.
5. Publicamos la app mediante DNS publico de EC2.

Esto demuestra que la solucion no solo funciona en el ordenador de desarrollo, sino tambien en un entorno real accesible por internet.

## 7. Resultados y Beneficios (16:00 - 18:30)

Guion sugerido:

Beneficios obtenidos/alineados con la presentacion:
1. Reduccion de errores en pedidos
2. Ahorro de tiempo en toma de pedidos y cobro
3. Mejor experiencia de cliente
4. Mejor control financiero y trazabilidad
5. Base escalable para nuevas funcionalidades

Ademas, la presentacion proyecta impacto positivo en eficiencia e ingresos gracias a la digitalizacion progresiva.

## 8. Cierre y Futuro (18:30 - 20:00)

Guion sugerido:

Como conclusion, este proyecto valida una transformacion digital completa y real:
- Se identifica un problema de negocio
- Se disena una solucion progresiva
- Se implementa una aplicacion funcional
- Se despliega en la nube

Proximos pasos naturales:
1. App movil para pedidos online
2. Programa de fidelizacion
3. Analitica de datos para optimizar menu y operacion

Cierre sugerido:
La digitalizacion no reemplaza al equipo humano, lo potencia para ofrecer un servicio mas rapido, preciso y moderno.

## Resumen ultra corto para abrir la defensa (30 segundos)

Hemos desarrollado una aplicacion full stack para digitalizar menu, pedidos y pagos de un restaurante, con base de datos PostgreSQL y despliegue publico en AWS EC2 usando Docker. El resultado es una operacion mas rapida, menos errores y una base escalable para futuras mejoras.

## Checklist para presentar con confianza

- Tener abierta la URL publica de la app
- Tener preparada una mini demo: menu -> pedido -> pago
- Explicar arquitectura en 3 capas: frontend, backend, base de datos
- Explicar despliegue en AWS en 4 pasos
- Cerrar con beneficios y siguientes pasos
