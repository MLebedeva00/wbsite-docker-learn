import os
from flask import Flask
import psycopg

app = Flask(__name__)

# Адрес базы сайт берёт из переменной окружения DB_HOST — не зашивает в код
DB = f"host={os.environ['DB_HOST']} dbname=postgres user=postgres password=secret"

@app.route("/")
def home():
    with psycopg.connect(DB) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS visits (n int)")
        conn.execute("INSERT INTO visits (n) VALUES (1)")
        count = conn.execute("SELECT count(*) FROM visits").fetchone()[0]
    return f"Привет! Ты заглянул сюда {count}-й раз"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)