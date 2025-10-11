from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

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

# ----- Model for Validation -----
class Item(BaseModel):
    Name: str
    Price: str
    Description: str


# ----- Routes -----

@app.get("/")
def root():
    return {"message": "Hello World"}


# ---- Team Members ----
@app.get("/Home/")
def get_member():
    return {"Team Members": members}


# ---- Inventory ----

# Static Introductory Endpoint
@app.get("/inventory")
def get_inventory():
    return {"Inventory": inventory}


# Get Item by ID
@app.get("/get_inventory/{item_id}")
def get_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    return inventory[item_id]


# Create New Item
@app.post("/create_inventory/", status_code=201)
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists")
    inventory[item_id] = item.dict()
    return {"message": "Item created successfully", "item": inventory[item_id]}


# Update Existing Item
@app.put("/update_inventory/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    inventory[item_id] = item.dict()
    return {"message": "Item updated successfully", "item": inventory[item_id]}
