import sys
import sqlite3
import os

def init(db):
    # create tables
    db.execute("create table if not exists User(username varchar(30) not null, email varchar(30) not null unique, password varchar(30) not null);")
    db.execute("create table if not exists Tickets(train varchar(30) not null, _from varchar(30) not null, _to varchar(30) not null, date varchar(30) not null, ticketid varchar(30) unique, username varchar(30));")
    db.commit()
    TRAINS = ["FALAKNUMA EXP", "EAST COST EXP", "SHALIMAR EXP", "SHATABDI EXP"]
    FROM = ["HYD", "DEL", "KOL"]
    TO = ["MMB", "AHM"]
    DATES = [f"{x+16}-4-2021" for x in range(1,4)]
    tid = 1000
    for t in TRAINS:
        for f in FROM:
            for _t in TO:
                for d in DATES:
                    command = f"insert into Tickets values('{t}', '{f}', '{_t}', '{d}', '{tid}', NULL);" 
                    # print(command)
                    db.execute(command)
                    tid += 1
                    db.commit()


def main():
    # Create database connection
    for name in [8001, 8002, 8003]:
        # Remove pre-existing database file
        try:
            os.remove(f'{name}.db')
        except OSError:
            pass
        db = sqlite3.connect(f'{name}.db')
        db.row_factory = sqlite3.Row
        init(db)
        db.close()
        print(f"Initialized {name}.db")

if __name__ == "__main__":
    main()
