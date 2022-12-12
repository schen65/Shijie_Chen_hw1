import numpy as np
import psycopg2
psycopg2.__version__
import pandas as pd


database = {'user':'postgres',
            'pass':'book',
            'name':'postgres',
            'host': 'localhost',
            'port':'5432'}


pgConnectString = f"""host={database['host']}
                      port={database['port']}
                      dbname={database['name']}
                      user={database['user']}
                      password={database['pass']}"""



pgConnection = psycopg2.connect(pgConnectString)
query ='select * from a;'
result = pd.read_sql_query(query,pgConnection)
pgConnection.close()
result