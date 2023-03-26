from db.run_sql import run_sql
from models.treatment import Treatment

def save(treatment):
    sql = "INSERT INTO treatments (name, duration, description) VALUES (%s, %s, %s) RETURNING id"
    values = [treatment.name, treatment.duration, treatment.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    treatment.id = id

def select_all():
    treatments = []
    sql = "SELECT * FROM treatments"
    results = run_sql(sql)
    for row in results:
        treatment = Treatment(row['name'], row['duration'], row['description'], row['id'])
        treatments.append(treatment)
    return treatments

def select(id):
    sql = "SELECT * FROM treatments WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        treatment = Treatment(row['name'], row['duration'], row['description'], row['id'])
    return treatment