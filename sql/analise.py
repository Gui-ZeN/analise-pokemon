import sqlite3
import pandas as pd
import os

# Caminho do banco
db_path = 'C:/Users/Pichau/Desktop/analise_pkmn/data/pokemon.db'

# Pasta para salvar os CSVs (crie se não existir)
output_folder = 'C:/Users/Pichau/Desktop/analise_pkmn/reports/csvs'
os.makedirs(output_folder, exist_ok=True)

# Conectar ao banco
conn = sqlite3.connect(db_path)

queries = {
    "pokemon_por_geracao": """
        SELECT generation, COUNT(*) as total
        FROM pokemon
        GROUP BY generation
        ORDER BY generation;
    """,
    "top_10_maiores_ataques": """
        SELECT name, attack
        FROM pokemon
        ORDER BY attack DESC
        LIMIT 10;
    """,
    "quantidade_por_tipo": """
        SELECT type_1, COUNT(*) as quantidade
        FROM pokemon
        GROUP BY type_1
        ORDER BY quantidade DESC;
    """,
    "media_defesa_por_tipo": """
        SELECT type_1, ROUND(AVG(defense), 2) as media_defesa
        FROM pokemon
        GROUP BY type_1
        ORDER BY media_defesa DESC;
    """,
    "total_lendarios_por_tipo": """
        SELECT type_1, COUNT(*) as qtd_lendarios
        FROM pokemon
        WHERE legendary = 1
        GROUP BY type_1
        ORDER BY qtd_lendarios DESC;
    """,
    "base_com_lendarios": """
    SELECT name, type_1, generation, legendary
    FROM pokemon;
    """,

}

for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    csv_path = os.path.join(output_folder, f"{name}.csv")
    df.to_csv(csv_path, index=False)
    print(f"Exportado: {csv_path}")

conn.close()
