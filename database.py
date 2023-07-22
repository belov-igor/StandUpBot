# -*- coding: utf-8 -*-
import sqlite3 as sq

db = sq.connect('db.db')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id INTEGER, "
                "tg_name TEXT, "
                "user_name TEXT, "
                "cart_id TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name TEXT, "
                "desc TEXT, "
                "price TEXT, "
                "photo TEXT, "
                "brand_TEXT)")
    db.commit()


async def cmd_start_db(user_id):
    user = cur.execute(f"SELECT * FROM accounts WHERE tg_id == {user_id}").fetchone()
    if not user:
        cur.execute(f"INSERT INTO accounts (tg_id) VALUES ({user_id})")
        db.commit()