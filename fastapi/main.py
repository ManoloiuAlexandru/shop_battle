from fastapi import FastAPI

from routes.creatures import router as creatures_router
from routes.spell import router as spell_router

app = FastAPI()


app.include_router(creatures_router)
app.include_router(spell_router)

@app.get("/")
def home():
    return {"message": "FastAPI is running"}