# Gestión de Inventario(Examen)

Este proyecto es una API sencilla desarrollada con **FastAPI** para la gestión de un inventario de productos. Es un examen. 

## ¿Qué contiene el código?
El código establece un sistema básico CRUD (Crear, Leer, Actualizar y Eliminar) que almacena los productos temporalmente en memoria (utilizando un diccionario). Usa `pydantic` para definir y validar la estructura de los datos del producto (ID, nombre, categoría, precio y stock).

## Endpoints Disponibles

- **`POST /productos/`**: Crea un nuevo producto.
- **`GET /productos/`**: Obtiene la lista completa de productos. Permite filtrar por categoría pasando un parámetro en la URL (ej. `/productos/?categoria=electronica`).
- **`GET /productos/{producto_id}`**: Obtiene un producto específico a través de su ID.
- **`PUT /productos/{producto_id}`**: Actualiza todos los datos de un producto existente.
- **`DELETE /productos/{producto_id}`**: Elimina un producto del inventario.

## Cómo levantar el proyecto

### 1. Preparar el entorno
Se recomienda utilizar un entorno virtual para instalar las dependencias:
```bash
python -m venv venv
```

Activar el entorno virtual (en Windows):
```bash
.\venv\Scripts\activate
```

### 2. Instalar dependencias
Necesitas instalar `fastapi` y `uvicorn` (servidor web):
```bash
pip install fastapi uvicorn
```

### 3. Ejecutar la aplicación
Levanta el servidor con recarga automática:
```bash
uvicorn main:app --reload
```
Una vez que el servidor inicie, la API estará disponible en `http://127.0.0.1:8000`. 

Puedes probar y visualizar la documentación interactiva (Swagger UI) ingresando a:
`http://127.0.0.1:8000/docs`
