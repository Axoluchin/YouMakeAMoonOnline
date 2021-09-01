import sqlite3 as sq

DataDir = 'DataBase/Moons.db'

def Nlunas():
  base = sq.connect(DataDir)
  cursor = base.execute("SELECT count(*) from Lunas")
  result = cursor.fetchall();
  base.close()
  return result[0][0]

def last_luna():
  base = sq.connect(DataDir)
  cursor = base.execute("SELECT Texto from Lunas ORDER BY ID DESC LIMIT 1")
  result = cursor.fetchall();
  base.close()
  return result[0][0]

def guarda_luna(texto,luna):
    if texto == last_luna():
      return
    base = sq.connect(DataDir)
    base.execute(f"INSERT INTO Lunas(Texto, TypeMoon) VALUES('{texto}',{luna})");
    base.commit()
    base.close()
    
def ultimas_lunas():
    base = sq.connect(DataDir)
    cursor = base.execute("SELECT Texto, TypeMoon from Lunas ORDER BY ID DESC LIMIT 10")
    result = cursor.fetchall();
    base.close()
    
    return result