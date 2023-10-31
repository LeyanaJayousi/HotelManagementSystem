import sqlite3
def create_db():
    con=sqlite3.connect(database= r'htl.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS hotel(htlid INTEGER PRIMARY KEY AUTOINCREMENT, name text, category text, area text, website text, board text)")
    con.commit()

    
create_db()    

