from sqlalchemy import create_engine

username = 'postgres'
password = '769011'
host = 'localhost'
port = '5432'
database = 'test_task_k2erp'
postgresql_url = f'postgresql://postgres:769011@localhost:5432/test_task_k2erp'
engine_postgresql = create_engine(postgresql_url, echo=True)