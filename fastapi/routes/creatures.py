from fastapi import APIRouter

from db.database import db_creatures
from models.creature import Creature


router = APIRouter()


@router.post("/add_creature")
def add_creature(creature: Creature):
    cursor = db_creatures.cursor()

    query = """
        INSERT INTO creatures (name, mana_cost)
        VALUES (%s, %s)
    """

    cursor.execute(query, (creature.name, creature.mana_cost))
    db_creatures.commit()

    cursor.close()

    return {"message": "Creature created successfully"}