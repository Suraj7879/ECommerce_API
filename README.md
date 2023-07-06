# ECommerce API

This repository contains the code for the ECommerce API, which is a backend server for managing orders and products. It is built using Python, FastAPI, and MongoDB.

## Prerequisites

1. FastAPI
2. Motor (MongoDB driver for asyncio)

Use the [pip](https://pip.pypa.io/en/stable/) package manager for installing this project

```bash
pip install fastapi
pip install motor
```

## Installation

1. Clone the repository:

```python
git clone https://github.com/your-repo-url.git
```

2. Install the dependencies:

```python
pip install -r requirements.txt
```

3. Set up MongoDB:

## Usage

1. To start the API server, run the following command:

```bash
uvicorn main:app --reload
```

2. The API will be available at http://localhost:8000
3. Access the Builtin API documentation of FastAPI at http://localhost:8000/docs in your web browser.

## API Endpoints

### Get all products

- **Endpoint:** `/products/`
- **Method:** GET
- **Description:** Retrieves all products from the database.
- **Response:** JSON response containing a list of products.

### Place an order

- **Endpoint:** `/order/`
- **Method:** POST
- **Description:** Places a new order.
- **Request body:** JSON object representing the order details.
- **Response:** JSON response indicating the success of the order placement.

#### **Request body should contain**

    ```
    {
        "items": [
            {
                "product": "Product 1",
                "quantity": 2
            },
            {
                "product": "Product 2",
                "quantity": 1
            }
        ],
        "amount": 1000,
        "address": {
            "city": "Maihar",
            "country": "India",
            "zipCode": 485771
        }
    }
    ```

### Get all orders

- **Endpoint:** `/orders/`
- **Method:** GET
- **Description:** Retrieves a paginated list of all orders.
- **Query parameters:**
  - `page` (optional): Page number (default: 1)
  - `page_size` (optional): Number of orders per page (default: 10)
- **Response:** JSON response containing the paginated list of orders.

### Get an order by ID

- **Endpoint:** `/orders/{id}`
- **Method:** GET
- **Description:** Retrieves an order by its ID.
- **Path parameter:** `id` - The ID of the order.
- **Response:** JSON response containing the order details.

### Update a product

- **Endpoint:** `/product/{id}`
- **Method:** PUT
- **Description:** Updates a product by its ID.
- **Path parameter:** `id` - The ID of the product.
- **Request body:** JSON object representing the updated fields of the product.
- **Response:** JSON response indicating the success of the product update.

### Insert multiple products

- **Endpoint:** `/products/`
- **Method:** POST
- **Description:** Inserts multiple products into the database.
- **Request body:** JSON array of product objects.
- **Response:** JSON response indicating the success of the product insertion.

#### **Request body should contain**

    ```
    [
        {
            "name": "Macbook Air M1",
            "price": 90000,
            "quantity": 20
        },
        {
            "name": "Aurdino",
            "price": 900,
            "quantity": 200
        },
        {
            "name": "Raspberry Pie",
            "price": 700,
            "quantity": 50
        },
        {
            "name": "Sony A95K OLED",
            "price": 100000,
            "quantity": 120
        },
        {
            "name": "Apple Mini",
            "price": 35000,
            "quantity": 12
        }
    ]

    ```
