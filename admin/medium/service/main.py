from flask import Flask, request
from hashlib import sha1  # so insecure
import sqlite3
import os
from contextlib import contextmanager
from html import escape


app = Flask(__name__)

SALT = "so salty, so cute:3 CTF Code 2021"
STARTING_STRING = '''
do you know that md5 of "oren_ctf" is cfe721641130ac5151d3c55fd8121ece?
'''

FLAG = "oren_ctf_DUHK!"

DB_PATH=os.environ.get('DB_PATH', 'user_agents.db')

@contextmanager
def db_connection():
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor\
            .execute(
             'CREATE TABLE IF NOT EXISTS agents'
             ' (user_agent TEXT UNIQUE, amount INTEGER)'
        )
        yield cursor
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.commit()
        conn.close()


def add_user_agent(user_agent):
    with db_connection() as cursor:
        cursor.execute(
            'INSERT INTO agents VALUES (?, ?)', (user_agent, 1))


def check_user_agents(user_agent):
    with db_connection() as cursor:
        cursor.execute(
            'SELECT * FROM agents WHERE user_agent=?', (user_agent,))
        row = cursor.fetchone()
        if row is not None:
            user_agent = row
            cursor.execute(
                'UPDATE agents SET amount = (?) WHERE user_agent = (?)',
                (user_agent[1] + 1, user_agent[0])
            )
            return True
        return False


def get_top_100_user_agents():
    with db_connection() as cursor:
        cursor.execute(
            'SELECT user_agent, amount from agents order by amount desc limit 100'
        )
        all_rows = cursor.fetchall()
        return all_rows



@app.route("/")
def root_router():
    return "Srly?! I hate guests, get out!", "200 go to root plus {}"\
        .format(sha1(STARTING_STRING.encode()).hexdigest())


@app.route("/easterEggs/top100userAgents")
def easter_egg():
    table = "<tr><th>Pos</th><th>UserAgent</th><th>Amount</th></tr>"
    for i, useragent in enumerate(get_top_100_user_agents()):
        table += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(i, escape(useragent[0]), useragent[1])
    return "<html><body><center><table border=\"1\">{}</table></center></body</html>".format(table)


@app.route("/<some_hash>")
def task_router(some_hash):
    user_agent = str(request.user_agent)

    # fix little and big user agents
    if user_agent == "" or len(user_agent) > 512:
        user_agent = "0orTooBig"
    # fix all browsers, lol
    if "Mozilla" in user_agent or "Opera" in user_agent:
        return "Your browser is banned!", "403 Browser is banned"

    # fix snakes
    if "python" in user_agent.lower():
        return "S-s-s-sssnakeee is here", "403 Python is banned also!"

    # fix old user agents
    if check_user_agents(user_agent):
        return "Your have been banned!", "403 Browser is Banned"
    else:
        add_user_agent(user_agent)

    # ok, flag
    if some_hash == "cf926ebbfe5088c164bc88b84233d4589d18e1f9":
        return "Find the flag, (or me, lol)",\
               '200 {}'.format(FLAG)
    return "Yep! You're on the right way!", "200 goto root plus {}"\
        .format(sha1((some_hash + SALT).encode()).hexdigest())


if __name__ == '__main__':
    app.run("0.0.0.0", port=8080)
