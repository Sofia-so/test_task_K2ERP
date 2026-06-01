import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    dbname="test_task_k2erp",
    user="postgres",
    password="769011",
    options="-c client_encoding=UTF8"
)

print("Підключення успішне")
conn.close()