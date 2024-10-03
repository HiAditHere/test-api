from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI app instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http:localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/api/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Endpoint with a path parameter
@app.get("/api/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "message": f"User {user_id} details"}

# To run this, save as 'main.py' and use the following command in terminal:
# uvicorn main:app --reload
