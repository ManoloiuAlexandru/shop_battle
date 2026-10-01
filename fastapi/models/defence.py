from pydantic import BaseModel

class Defence(BaseModel):
    name: str
    mana_cost: int