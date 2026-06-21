import pymysql


class Database:
    def __init__(self, db_name, db_password, db_user, db_port, db_host):
        self.db_name = db_name
        self.db_password = db_password
        self.db_user = db_user
        self.db_port = db_port
        self.db_host = db_host

    def connect(self):
        return pymysql.Connection(
            database=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            cursorclass=pymysql.cursors.DictCursor
        )

    def execute(self, sql: str, params: tuple = (), commit=False, fetchone=False, fetchall=False) -> dict | list:
        database = self.connect()
        cursor = database.cursor()

        cursor.execute(sql, params)
        data = None

        if fetchone:
            data = cursor.fetchone()

        elif fetchall:
            data = cursor.fetchall()

        if commit:
            database.commit()

        return data

    def clear_categories(self):
        sql = """
            DELETE FROM categories
        """
        self.execute(sql, commit=True)

    def clear_products(self):
        sql = """
            DELETE FROM products
        """
        self.execute(sql, commit=True)

    def seed_categories(self) -> None:
        self.clear_categories()
        sql = """
            INSERT INTO categories (name)
            VALUES ("🌯 Lavashlar"),
                   ("🍔 Burgerlar"),
                   ("🌮 Shourmalar"),
                   ("🥂 Ichimliklar"),
                   ("🍧 Desertlar")
        """
        self.execute(sql, commit=True)
        print("5 ta kategoriya yaratildi: Lavashlar, Burgerlar, Shourmalar, Ichimliklar, Desertlar")

    def seed_products(self) -> None:
        self.clear_products()
        sql = """
            INSERT INTO products (name, category_id, price,  description, image_path)
            VALUES ("Lavash mini", 66, 25000.00, "Compact and delicious lavash prepared with fresh ingredients and wrapped in soft baked bread. Filled with tender meat, crisp vegetables, and flavorful sauces, it offers a satisfying meal that is perfect for a quick lunch, snack, or light dinner.", "media/products/lavash_mini.jpg"),
                   ("Lavash standart", 66, 28000.00, "A balanced lavash option featuring a generous portion of juicy meat, fresh vegetables, and signature sauces wrapped in warm, soft lavash bread. Ideal for everyday dining, it delivers rich flavor, satisfying texture, and excellent value in every bite.", "media/products/lavash_standart.jpg"),
                   ("Lavash big", 66, 32000.00, "The largest mini-series lavash designed for hearty appetites. Packed with extra meat, fresh vegetables, and flavorful sauces inside freshly baked lavash bread, it provides a filling and satisfying experience that is perfect for lunch, dinner, or sharing.", "media/products/lavash_big.jpg")
        """
        self.execute(sql, commit=True)
        print("3 ta maxsulot qo'shildi: Lavash (min), Lavash (standart), Lavash (big)")

    def create_users_table(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS users(
                id INT PRIMARY KEY AUTO_INCREMENT,
                telegram_id INT NOT NULL UNIQUE,
                fullname VARCHAR(100)
            )
        """
        self.execute(sql)

    def create_categories_table(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS categories(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL UNIQUE
            )
        """
        self.execute(sql, commit=True)
        # self.seed_categories()

    def create_products_table(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS products(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL UNIQUE,
                category_id INT NOT NULL,
                price DECIMAL(12, 2) NOT NULL,
                description VARCHAR(255) NOT NULL,
                image_path VARCHAR(255) NOT NULL
            )
        """
        self.execute(sql, commit=True)
        self.seed_products()

    def add_user(self, telegram_id: int, fullname: str = "") -> None:
        sql = """
            INSERT INTO users (telegram_id, fullname)
            VALUES (%s, %s)
        """
        self.execute(sql, (telegram_id, fullname), commit=True)

    def get_categories(self) -> list[dict]:
        sql = """
            SELECT * FROM categories
        """
        return self.execute(sql, fetchall=True)

    def get_category_product(self, category_id: int) -> list[dict]:
        sql = """
            SELECT * FROM products WHERE category_id = %s
        """
        return self.execute(sql, (category_id,), fetchall=True)

    def get_product(self, product_id: int) -> dict:
        sql = """
            SELECT * FROM products WHERE id = %s
        """
        return self.execute(sql, (product_id,), fetchone=True)
