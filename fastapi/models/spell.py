from pydantic import BaseModel

class Spell(BaseModel):
    name: str
    mana_cost: int