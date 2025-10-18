
## Lab1-Bunag.py Documentation

### Overview
`Lab1-Bunag.py` is a FastAPI-based Inventory Management System that provides a RESTful API for managing inventory items. The application includes CRUD operations for inventory management and team member information.

### Features
- **Inventory Management**: Full CRUD operations for inventory items
- **Team Information**: Display team member details
- **RESTful API**: Proper HTTP semantics with appropriate status codes
- **Data Validation**: Pydantic models for request validation
- **Error Handling**: Comprehensive error handling with proper HTTP status codes

### Team Members
The application includes information about the development team:
1. Bunag, Percy S.
2. Irenea, John Michael A.
3. Dela Cruz, John Mark C.
4. Aguilon, Adriane G.
5. Fortaliza, Destine April D.
6. Factor, Francis C.

### API Endpoints

#### Meta Endpoints
- `GET /` - Root endpoint returning a "Hello World" message
- `GET /Home/` - Returns team member information

#### Inventory Endpoints
- `GET /inventory` - Retrieves all inventory items
- `GET /get_inventory/{item_id}` - Retrieves a specific inventory item by ID
- `POST /create_inventory/` - Creates a new inventory item
- `PUT /update_inventory/{item_id}` - Updates an existing inventory item
- `DELETE /items/{item_id}` - Deletes an inventory item

### Data Models

#### Item Model
```python
class Item(BaseModel):
    Name: str
    Price: str
    Description: str
```

### Sample Inventory Data
The application comes pre-populated with sample processor inventory:
1. **Intel i5 11th Gen** - ₱10,000
2. **AMD Ryzen 5 5600G** - ₱10,000
3. **AMD Ryzen 7 5800H** - ₱10,000

### Installation and Usage

#### Prerequisites
- Python 3.7+
- FastAPI
- Pydantic

#### Running the Application
```bash
# Install dependencies
pip install fastapi uvicorn

# Run the application
uvicorn Lab1-Bunag:app --reload
```

#### Accessing the API
- **API Documentation**: http://localhost:8000/docs (Swagger UI)
- **Alternative Documentation**: http://localhost:8000/redoc (ReDoc)

### API Examples

#### Get All Inventory Items
```bash
curl -X GET "http://localhost:8000/inventory"
```

#### Create New Item
```bash
curl -X POST "http://localhost:8000/create_inventory/?item_id=4" \
     -H "Content-Type: application/json" \
     -d '{
       "Name": "Intel i7 12th Gen",
       "Price": "15000",
       "Description": "High-performance processor for gaming and productivity"
     }'
```

#### Update Existing Item
```bash
curl -X PUT "http://localhost:8000/update_inventory/1" \
     -H "Content-Type: application/json" \
     -d '{
       "Name": "Intel i5 11th Gen (Updated)",
       "Price": "12000",
       "Description": "Updated description for Intel i5 11th Gen processor"
     }'
```

#### Delete Item
```bash
curl -X DELETE "http://localhost:8000/items/1"
```

### Error Handling
The API includes comprehensive error handling:
- **404 Not Found**: When requesting non-existent items
- **400 Bad Request**: When attempting to create items with existing IDs
- **204 No Content**: Successful deletion responses

### Technical Details
- **Framework**: FastAPI
- **Data Validation**: Pydantic
- **Storage**: In-memory dictionaries (for demonstration purposes)
- **HTTP Status Codes**: Proper RESTful semantics
- **API Documentation**: Auto-generated Swagger/OpenAPI documentation

