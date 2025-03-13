# E-Commerce Database Management System

## Project Overview
This is a full-stack **E-Commerce Management System** that allows **customers** to browse products, place orders, and write reviews, while **admins** can manage users, products, and orders. The system includes:
- **Flask API (Backend)**: Handles database operations and business logic.
- **PostgreSQL Database**: Stores user, product, and order data.
- **Streamlit Apps (Admin & Customer)**: Provides user-friendly interfaces for customers and admins.

---

## Features
###  **Customer Functionality**
- Browse available products
- Add items to the cart
- Place an order
- Submit product reviews

###  **Admin Functionality**
- Manage users (add, delete, view)
- Manage products (add, delete, view)
- View and update orders
- Monitor customer reviews and logs

---

##  Tech Stack
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: Streamlit
- **ORM**: SQLAlchemy
- **Deployment**: Render, ElephantSQL, Streamlit Cloud

---

##  Local Setup Guide
### ** Clone the Repository**
```bash
git clone https://github.com/MeilinP/E-Commerce-Database-Management.git
cd E-Commerce-Database-Management
```

### ** Create a Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### ** Configure the Database**
- Install PostgreSQL and create a database:
```sql
CREATE DATABASE ecommerce_db;
```
- Update `config.py` with your database URL:
```python
DATABASE_URL = "postgresql://username:password@localhost:5432/ecommerce_db"
```

### ** Run Database Migrations**
```bash
python -m flask db upgrade
```

### ** Start the Flask API**
```bash
flask run
```
- The API will be available at: `http://127.0.0.1:5000`

### ** Start the Customer & Admin Dashboards**
```bash
streamlit run customer_app.py
```
```bash
streamlit run admin.py
```
- Customer App: `http://localhost:8501`
- Admin Dashboard: `http://localhost:8502`

---


## API Endpoints
| **Method** | **Endpoint** | **Description** |
|------------|-------------|-----------------|
| `GET` | `/users` | Get all users |
| `POST` | `/users` | Add a new user |
| `GET` | `/products` | Get all products |
| `POST` | `/products` | Add a new product |
| `POST` | `/orders` | Place an order |
| `GET` | `/orders` | Get all orders |
| `POST` | `/reviews` | Submit a review |

---
