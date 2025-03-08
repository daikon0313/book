# def greeting(name, login_cnt):
#     return f"こんにちは、{name}さん！({login_cnt}回目のログイン)"

# def greeting_hint(name:str, login_cnt:int) -> str:
#     return f"こんにちは、{name}さん！({login_cnt}回目のログイン)"

# print(greeting_hint("dai", 10))

import sqlite3

DATABASE = "./database.db"

def insert_user(name:str, user_id:int):
    con = sqlite3.connect(DATABASE)
    con.execute(
        "INSERT INTO users VALUES(?,?)",
        [name, name]
    )
    con.commit()
    con.close()