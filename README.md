# FastAPI User Management API

A simple FastAPI application for updating and deleting user records in an in-memory database.

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

2. Start the server:
   ```bash
   uvicorn testing:app --reload
   ```

3. API will be available at:
   ```
   http://localhost:8000
   ```

## 📚 Endpoints

- **Update User**
  - `PUT /user_db/data/v1/update/{user_id}`
  - Request body: JSON with `name` (str) and `age` (int)

- **Delete User**
  - `DELETE /user_db/data/v1/update/{user_id}`

## 📝 Example

Update user:
```bash
curl -X PUT "http://localhost:8000/user_db/data/v1/update/1" -H "Content-Type: application/json" -d '{"name": "newname", "age": 25}'
```

Delete user:
```bash
curl -X
