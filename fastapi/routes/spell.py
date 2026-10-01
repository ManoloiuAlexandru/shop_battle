from fastapi import APIRouter

from db.database import db_spell
from models.spell import Spell

router = APIRouter()


@router.post("/add_spell")
def add_spell(spell: Spell):
    cursor = db_spell.cursor()

    query = """
        INSERT INTO spells (name, mana_cost)
        VALUES (%s, %s)
    """

    cursor.execute(query, (spell.name, spell.mana_cost))
    db_spell.commit()

    cursor.close()

    return {"message": "Spell created successfully"}