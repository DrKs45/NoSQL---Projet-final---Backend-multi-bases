import sys
import os
from sqlalchemy import text

# Cette ligne permet de s'assurer que Python trouve le dossier 'app'
sys.path.append(os.getcwd())

try:
    from app.db.postgres import engine
    print("✅ Importation des modules réussie.")
except ImportError as e:
    print(f"❌ Erreur d'importation : {e}")
    sys.exit(1)

def test_postgres_connection():
    print("🐘 Tentative de connexion à PostgreSQL...")
    try:
        # On tente d'ouvrir une connexion et d'exécuter une requête simple
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 'Connexion opérationnelle !'"))
            for row in result:
                print(f"🚀 SQL dit : {row[0]}")
        print("\n✨ Félicitations ! La liaison entre Python et PostgreSQL est parfaite.")
    except Exception as e:
        print(f"\n❌ Échec de la connexion.")
        print(f"Détails de l'erreur : {e}")
        print("\n💡 Vérifie que :")
        print("1. Tes conteneurs Docker sont lancés (docker ps)")
        print("2. Les identifiants dans app/core/config.py sont corrects")

if __name__ == "__main__":
    test_postgres_connection()