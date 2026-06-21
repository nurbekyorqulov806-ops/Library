import sqlite3

# 1. Bazaga ulanish
# check_same_thread=False bu botlar uchun juda muhim, 
# aks holda boshqa qismlar bazaga kira olmay qolishi mumkin.
conn = sqlite3.connect("books.db", check_same_thread=False)
cursor = conn.cursor()

# 2. Jadvalni yaratish (Agar bo'lmasa)
def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS favorites (
        user_id INTEGER,
        book_key TEXT,
        title TEXT
    )
    """)
    conn.commit()

# 3. Jadvalni yaratish funksiyasini chaqiramiz
create_tables()