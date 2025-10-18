from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(
    title="Inventory API",
    description="Simple inventory with CRUD and proper HTTP semantics.",
    version="1.0.0",
)

# ----- Data Storage -----
inventory = {
    1: {
        "Name": "Intel i5 11th Gen",
        "Price": "10000",
        "Description": "Intel i5 11th Gen is a processor that is used in laptops and desktops.",
    },
    2: {
        "Name": "AMD Ryzen 5 5600G",
        "Price": "10000",
        "Description": "AMD Ryzen 5 5600G is a processor that is used in laptops and desktops.",
    },
    3: {
        "Name": "AMD Ryzen 7 5800H",
        "Price": "10000",
        "Description": "AMD Ryzen 7 5800H is a processor that is used in laptops and desktops.",
    },
}

members = {
    1: {"Name": "Bunag, Percy S."},
    2: {"Name": "Irenea, John Michael A."},
    3: {"Name": "Dela Cruz, John Mark C."},
    4: {"Name": "Aguilon, Adriane G."},
    5: {"Name": "Fortaliza, Destine April D."},
    6: {"Name": "Factor, Francis C."},
}


class Item(BaseModel):
    Name: str
    Price: str
    Description: str


# ----- Routes -----

@app.get("/", tags=["Meta"])
def root():
    return {"message": "Hello World"}


# ---- Team Members ----
@app.get("/Home/", tags=["Meta"])
def get_member():
    return {"Team Members": members}


# ---- Inventory ----

# Static Introductory Endpoint
@app.get("/inventory", tags=["Inventory"])
def get_inventory():
    return {"Inventory": inventory}


# Get Item by ID
@app.get("/get_inventory/{item_id}", tags=["Inventory"])
def get_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    return inventory[item_id]


# Create New Item
@app.post("/create_inventory/", status_code=201, tags=["Inventory"])
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists")
    inventory[item_id] = item.dict()
    return {"message": "Item created successfully", "item": inventory[item_id]}


# Update Existing Item
@app.put("/update_inventory/{item_id}", tags=["Inventory"])
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    inventory[item_id] = item.dict()
    return {"message": "Item updated successfully", "item": inventory[item_id]}

@app.delete("/items/{item_id}", tags=["Inventory"])
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    del inventory[item_id]

    return Response(status_code=status.HTTP_204_NO_CONTENT)