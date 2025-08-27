from fastapi import FastAPI
from routes import route

app = FastAPI()

# include the router from route.py
app.include_router(route.router)
