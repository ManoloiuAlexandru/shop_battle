from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    mana_cost: int