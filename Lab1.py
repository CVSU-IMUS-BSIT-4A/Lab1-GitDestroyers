<<<<<<< HEAD
from fastapi import FastAPI, HTTPException, Response
=======
from fastapi import FastAPI, HTTPException
>>>>>>> 7acbb1257bbaa09f48f2d7793ae4ab0617b3c496
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(title="Inventory Management API", version="2.0")

# Data Models
class CreateInventoryItem(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    category: str

class UpdateInventoryItem(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category: Optional[str] = None


<<<<<<< HEAD
=======
# Enhanced inventory database
>>>>>>> 7acbb1257bbaa09f48f2d7793ae4ab0617b3c496
inventory_db = [
    {"id": 1, "name": "Intel i5 11th Gen", "description": "Intel i5 11th Gen is a processor that is used in laptops and desktops.", "price": 10000.00, "quantity": 5, "category": "Processors"},
    {"id": 2, "name": "AMD Ryzen 5 5600G", "description": "AMD Ryzen 5 5600G is a processor that is used in laptops and desktops.", "price": 10000.00, "quantity": 8, "category": "Processors"},
    {"id": 3, "name": "AMD Ryzen 7 5800H", "description": "AMD Ryzen 7 5800H is a processor that is used in laptops and desktops.", "price": 10000.00, "quantity": 3, "category": "Processors"},
    {"id": 4, "name": "NVIDIA RTX 4060", "description": "High-performance graphics card for gaming and content creation", "price": 15000.00, "quantity": 6, "category": "Graphics Cards"},
    {"id": 5, "name": "Samsung 1TB SSD", "description": "Fast NVMe SSD for improved system performance", "price": 5000.00, "quantity": 12, "category": "Storage"}
]

<<<<<<< HEAD
=======
# Team Members - Updated List
>>>>>>> 7acbb1257bbaa09f48f2d7793ae4ab0617b3c496
team_members = [
    {"name": "Destine April D. Fortaliza", "role": "Developer", "student_id": "BSIT-4A"},
    {"name": "Percy S. Bunag", "role": "Developer", "student_id": "BSIT-4A"},
    {"name": "Francis C. Factor", "role": "Developer", "student_id": "BSIT-4A"},
    {"name": "John Mark C. Cruz", "role": "Developer", "student_id": "BSIT-4A"},
    {"name": "Adriane Aguilon", "role": "Developer", "student_id": "BSIT-4A"},
    {"name": "John Michael Irenea", "role": "Developer", "student_id": "BSIT-4A"}
]



# New Activity 2 endpoints
@app.get("/Home/")
async def home():
    return {
        "message": "Welcome to Inventory Management API - Activity v2",
        "team": "GitDestroyers",
        "members": team_members,
        "version": "2.0"
    }

@app.get("/inventory")
async def get_static_inventory():
    return {
        "message": "Welcome to our inventory system!",
        "total_items": len(inventory_db),
        "categories": list(set(item["category"] for item in inventory_db)),
        "sample_items": inventory_db[:3]
    }

@app.get("/get_inventory/")
async def get_all_inventory():
    return {
        "status": "success",
        "total_items": len(inventory_db),
        "items": inventory_db
    }

@app.get("/get_inventory/{item_id}")
async def get_inventory_item(item_id: int):
    for item in inventory_db:
        if item["id"] == item_id:
            return {"status": "success", "item": item}
<<<<<<< HEAD
    return Response(status_code=404)
=======
    raise HTTPException(status_code=404, detail="Item not found")
>>>>>>> 7acbb1257bbaa09f48f2d7793ae4ab0617b3c496

@app.post("/create_inventory/")
async def create_inventory_item(item: CreateInventoryItem):
    # Check if ID already exists
    for existing_item in inventory_db:
        if existing_item["id"] == item.id:
<<<<<<< HEAD
            return Response(status_code=400)
=======
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
>>>>>>> 7acbb1257bbaa09f48f2d7793ae4ab0617b3c496
    
    # Check if name already exists
    for existing_item in inventory_db:
        if existing_item["name"].lower() == item.name.lower():
<<<<<<< HEAD
            return Response(status_code=400)
=======
            raise HTTPException(status_code=400, detail="Item with this name already exists")
>>>>>>> 7acbb1257bbaa09f48f2d7793ae4ab0617b3c496
    
    new_item = {
        "id": item.id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "quantity": item.quantity,
        "category": item.category
    }
    inventory_db.append(new_item)
    
    return {
        "status": "success",
        "message": "Item created successfully",
        "item": new_item
    }

@app.put("/update_inventory/{item_id}")
async def update_inventory_item(item_id: int, item_update: UpdateInventoryItem):
    item_index = None
    for i, item in enumerate(inventory_db):
        if item["id"] == item_id:
            item_index = i
            break
    
    if item_index is None:
<<<<<<< HEAD
        return Response(status_code=404)
=======
        raise HTTPException(status_code=404, detail="Item not found")
>>>>>>> 7acbb1257bbaa09f48f2d7793ae4ab0617b3c496
    
    if item_update.name is not None:
        for existing_item in inventory_db:
            if existing_item["id"] != item_id and existing_item["name"].lower() == item_update.name.lower():
<<<<<<< HEAD
                return Response(status_code=400)
=======
                raise HTTPException(status_code=400, detail="Item with this name already exists")
>>>>>>> 7acbb1257bbaa09f48f2d7793ae4ab0617b3c496
    
    current_item = inventory_db[item_index]
    
    if item_update.name is not None:
        current_item["name"] = item_update.name
    if item_update.description is not None:
        current_item["description"] = item_update.description
    if item_update.price is not None:
        current_item["price"] = item_update.price
    if item_update.quantity is not None:
        current_item["quantity"] = item_update.quantity
    if item_update.category is not None:
        current_item["category"] = item_update.category
    
    return {
        "status": "success",
        "message": "Item updated successfully",
        "item": current_item
    }

<<<<<<< HEAD
@app.delete("/items/{item_id}")
async def delete_inventory_item(item_id: int):
    item_index = None
    for i, item in enumerate(inventory_db):
        if item["id"] == item_id:
            item_index = i
            break
    
    if item_index is None:
        return Response(status_code=404)
    
    # Remove the item from the database
    inventory_db.pop(item_index)
    
    # Return 204 No Content with empty body
    return Response(status_code=204)

=======
>>>>>>> 7acbb1257bbaa09f48f2d7793ae4ab0617b3c496
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
