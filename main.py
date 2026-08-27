from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Hola profe, pongame 5")

class Producto(BaseModel):
    id: int
    nombre: str
    categoria: str
    precio: float
    stock: int

inventario = {}

@app.post("/productos/", status_code=201)
def crear_producto(producto: Producto):
    inventario[producto.id] = producto
    return producto

@app.get("/productos/")
def listar_productos(categoria: str = None):
    if categoria:
        return [p for p in inventario.values() if p.categoria == categoria]
    return list(inventario.values())

@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    if producto_id not in inventario:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return inventario[producto_id]

@app.put("/productos/{producto_id}")
def actualizar_producto(producto_id: int, producto: Producto):
    if producto_id not in inventario:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    inventario[producto_id] = producto
    return producto

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):
    if producto_id not in inventario:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    del inventario[producto_id]
    return {"mensaje": "Producto eliminado"}