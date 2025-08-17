import duckdb
from palmerpenguins import penguins

con = duckdb.connect('my-db_python.duckdb')
df = penguins.load_penguins()
con.execute('CREATE TABLE penguins AS SELECT * FROM df')
con.close()
