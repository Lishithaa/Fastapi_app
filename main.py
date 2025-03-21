from fastapi import FastAPI
from config.engine import engine
from models.models import Base
from routers import users

app = FastAPI()

# Create tables
Base.metadata.create_all(engine)

# Include all the Routers from each module
app.include_router(users.router)
