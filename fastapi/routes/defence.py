from fastapi import APIRouter

from db.database import db_creatures
from models.defence import Defence


router = APIRouter()


@router.post("/add_defence")
def add_defence(defence: Defence):
    cursor = db_creatures.cursor()

    query = """
        INSERT INTO defences (name, mana_cost)
        VALUES (%s, %s)
    """

    cursor.execute(query, (defence.name, defence.mana_cost))
    db_creatures.commit()

    cursor.close()

    return {"message": "Defence created successfully"}