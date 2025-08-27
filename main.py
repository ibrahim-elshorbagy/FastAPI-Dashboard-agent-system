from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import route

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# include the router from route.py
app.include_router(route.router)
