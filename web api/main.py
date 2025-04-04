from fastapi import FastAPI, HTTPException
from models import User
from database import users_db

app = FastAPI()

@app.get("/")
def home():
    return {"message": "🚀 Welcome to the User API!"}

# Get all users
@app.get("/users")
def get_users():
    return list(users_db.values())

# Get user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# Create new user
@app.post("/users", status_code=201)
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.id] = user
    return {"message": "User created successfully", "user": user}

# Update user
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = updated_user
    return {"message": "User updated", "user": updated_user}

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted successfully"}
