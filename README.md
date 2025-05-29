# Railway Management System (Python)

A Flask-based Railway Management System API that handles train schedules, bookings, and user authentication

## 🛠 Tech Stack
- Python 3.8+
- Flask (Web Framework)
- PostgreSQL (Database)
- SQLAlchemy (ORM)
- JWT (Authentication)
- Marshmallow (Validation)

## 📦 Setup

1. Clone the Github repository:
```bash
git clone https://github.com/Morning0Star/Railway_Management_System.git
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory with the following variables:
```
DATABASE_URL=postgresql+psycopg://username:password@host:port/database
JWT_SECRET=your_jwt_secret
ADMIN_API_KEY=your_admin_api_key
PORT=5000
DEBUG=True
TZ=UTC
```

## 🚀 Run Server
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## ✅ API Endpoints

### Authentication
- POST `/api/v1/auth/register` - Register a new user
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123"
  }
  ```
- POST `/api/v1/auth/login` - Login user
  ```json
  {
    "email": "john@example.com",
    "password": "password123"
  }
  ```

### Trains (Admin)
- POST `/api/v1/trains` - Create a new train (Requires Admin API Key)
  ```json
  {
    "id": "T1",
    "name": "Express 1",
    "source": "Mumbai",
    "destination": "Delhi",
    "totalSeats": 100
  }
  ```
- GET `/api/v1/trains` - Get all trains
- GET `/api/v1/trains/<train_id>` - Get train by ID

### Bookings (Requires JWT)
- POST `/api/v1/bookings` - Create a new booking
  ```json
  {
    "trainId": "T1"
  }
  ```
- GET `/api/v1/bookings` - Get all bookings for the authenticated user
- GET `/api/v1/bookings/<booking_id>` - Get booking by ID
- DELETE `/api/v1/bookings/<booking_id>` - Cancel a booking

## 📌 Notes
- Uses SQLAlchemy for database operations with connection pooling
- Implements JWT-based authentication
- Uses row-level locking to prevent race conditions when booking seats
- Follows MVC pattern with clear separation of concerns:
  - Routes: Handle HTTP requests
  - Controllers: Contain business logic
  - Services: Handle database operations
  - Models: Define database schema
  - Middleware: Handle cross-cutting concerns

## 🔒 Security Features
- JWT-based authentication
- Admin API key protection for train management
- Password hashing
- Input validation using Marshmallow
- SQL injection prevention through SQLAlchemy
- Connection pooling for database stability

## 🧪 Testing
Use Postman or any API testing tool to test the endpoints. Remember to:
1. Register a user
2. Login to get JWT token
3. Use the token in Authorization header for protected routes
4. Use Admin API key for train management routes 