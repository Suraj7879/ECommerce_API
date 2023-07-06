import motor.motor_asyncio
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional
from bson.timestamp import Timestamp
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException, Query


app = FastAPI()

uri = "mongodb+srv://cosmocloud:<password>@cosmocloud.rnm5qgo.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = motor.motor_asyncio.AsyncIOMotorClient(uri)

db = client["cosmocloud"]
orderCollection = db["orders"]
productCollection = db["products"]


class Address(BaseModel):
    city: str
    country: str
    zipCode: int

class Items(BaseModel):
    product: str
    quantity: Optional[int]

class Order(BaseModel):
    items: List[Items]
    amount: int
    address: Address
    

@app.get('/products/')
async def all_products():
    documents = productCollection.find()
    document_list = await documents.to_list(length=None)
    return JSONResponse(content=jsonable_encoder(document_list))


@app.post('/order/')
async def order(order: Order):
    try:
        order = order.dict()
        order["timestamp"] = int(datetime.now(timezone.utc).timestamp()) #storing it as epoch seconds, UTC
        result = await orderCollection.insert_one(order)
        print(result)
    except Exception as e:
        print(e)
    
    return {"message": "Your order has been successfully placed"}


@app.get('/orders/')
async def all_orders(page: int = Query(1, gt=0), page_size: int = Query(10, gt=0)):
    skip = (page - 1) * page_size
    total_orders = await orderCollection.count_documents({})

    if skip >= total_orders:
        raise HTTPException(status_code=404, detail="Page not found")

    cursor = orderCollection.find().skip(skip).limit(page_size)
    orders = []
    async for order in cursor:
        order['_id'] = str(order['_id'])
        orders.append(order)

    return {
        "page": page,
        "page_size": page_size,
        "total_orders": total_orders,
        "orders": orders
    }


@app.get('/orders/{id}')
async def order(id: str):
    order = await orderCollection.find_one({"_id": ObjectId(id)})
    if order:
        order['_id'] = str(order['_id'])
        return order
    else:
        return {"message": "Student not found"}


@app.put('/product/{id}')
async def update_product(id: str, updated_fields: dict):
    await productCollection.update_one({"_id": ObjectId(id)}, {"$set": updated_fields})
    return {"message": "Student updated"}


@app.post('/products/')
async def insert_documents(products: list): 
    result = productCollection.insert_many(products)
    print(result)
    return {"message": "success"}
