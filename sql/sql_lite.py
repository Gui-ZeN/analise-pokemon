import pandas as pd
import sqlite3

df = pd.read_csv('c:/Users/Pichau/Desktop/analise_pkmn/data/pokemon_tratado.csv')


conn = sqlite3.connect('C:/Users/Pichau/Desktop/analise_pkmn/data/pokemon.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type_1 TEXT,
    type_2 TEXT,
    total INTEGER,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    sp_atk INTEGER,
    sp_def INTEGER,
    speed INTEGER,
    generation INTEGER,
    legendary INTEGER
);
""")

df.to_sql('pokemon', conn, if_exists='replace', index=False)

cursor.execute("SELECT COUNT(*) FROM pokemon;")
total = cursor.fetchone()[0]
print(f"Dados inseridos com sucesso! Total de registros: {total}")

conn.close()