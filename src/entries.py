import random
import sqlite3
from os.path import dirname, abspath
from datetime import date

dir_path = dirname(dirname(__file__))
DB_FILENAME = dir_path + '/' + 'entries.db'


def find_random_entry():
    conn = sqlite3.connect(DB_FILENAME)

    c = conn.cursor()
    c.execute("SELECT id from entries")
    ids = list(map(lambda x: x[0], c.fetchall()))

    random_id = random.choice(ids)
    c.execute("""
    SELECT id, entry
    FROM entries
    WHERE id = ?
    """, (random_id,)
    )
    t = c.fetchone()
    entry_dict = tuple_to_dict(t)

    c = conn.cursor()
    conn.close()
    return entry_dict


def tuple_to_dict(entry):
    return {
        'id': entry[0],
        'entry': entry[1]
    }


def add_entry(entry):
    conn = sqlite3.connect(DB_FILENAME)
    today = date.today().strftime("%m-%d-%Y")

    c = conn.cursor()
    c.execute("""
      INSERT INTO entries
      (entry, created_at, updated_at)
      VALUES
      (?,?,?)
    """,
              (entry, today, today))

    conn.commit()
    conn.close()


def print_entry(e):
    print('\n')
    print('   %s   ' % (e["entry"]))
    print('\n')


def count():
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) from entries")
    count = c.fetchone()[0]
    conn.close()
    return count
