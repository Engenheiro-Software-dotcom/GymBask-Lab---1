from app.core.database import engine
from sqlalchemy import text

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Conexão OK:", result.scalar())
except Exception as e:
    print("Erro na conexão:", e)