# Orderflow API

API REST construida con **Django REST Framework** para la gestión de **Clientes** y **Pedidos**.

## 🚀 Endpoints principales

### Clientes
| Método | Endpoint | Descripción |
|---------|-----------|--------------|
| GET | /api/clients/ | Lista todos los clientes |
| POST | /api/clients/ | Crea un cliente |
| GET | /api/clients/{id}/ | Detalle de cliente |
| PUT/PATCH | /api/clients/{id}/ | Edita cliente |
| DELETE | /api/clients/{id}/ | Elimina cliente |

### Pedidos
| Método | Endpoint | Descripción |
|---------|-----------|--------------|
| GET | /api/orders/ | Lista todos los pedidos |
| POST | /api/orders/ | Crea un pedido |
| GET | /api/orders/{id}/ | Detalle de pedido |
| PUT/PATCH | /api/orders/{id}/ | Edita pedido |
| DELETE | /api/orders/{id}/ | Elimina pedido |
| GET | /api/orders/?search={texto} | Busca por cliente o estado |

## 🧩 Tecnologías usadas
- Python 3.11+
- Django 5
- Django REST Framework

## 🧠 Autor
Desarrollado por **Diego Alexis** — 2025.
