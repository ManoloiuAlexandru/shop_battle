import os
import mysql.connector


db_creatures = mysql.connector.connect(
    host=os.getenv("DB_creature_HOST"),
    port=int(os.getenv("DB_creature_PORT")),
    database=os.getenv("DB_creature_NAME"),
    user=os.getenv("DB_creature_USER"),
    password=os.getenv("DB_creature_PASSWORD")
)

db_spell = mysql.connector.connect(
    host=os.getenv("DB_spell_HOST"),
    port=int(os.getenv("DB_spell_PORT")),
    database=os.getenv("DB_spell_NAME"),
    user=os.getenv("DB_spell_USER"),
    password=os.getenv("DB_spell_PASSWORD")
)

db_defence = mysql.connector.connect(
    host=os.getenv("DB_defence_HOST"),
    port=int(os.getenv("DB_defence_PORT")),
    database=os.getenv("DB_defence_NAME"),
    user=os.getenv("DB_defence_USER"),
    password=os.getenv("DB_defence_PASSWORD")
)