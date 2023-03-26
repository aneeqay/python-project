from db.run_sql import run_sql
from models.treatment import Treatment
from models.booking import Booking
from models.treatmentinbooking import Treatinbook
import repos.treatments_repo as treatments_repo
import bookings_repo

def save(treatinbook):
    sql = "INSERT INTO treatments_bookings (bookings_id, treatments_id) VALUES (%s, %s) RETURNING id"
    values = [treatinbook.booking.id, treatinbook.treatment.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    treatinbook.id = id

def select(id):
    sql = "SELECT * FROM treatments_bookings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        treatment = treatments_repo.select(row['treatments_id'])
        booking = bookings_repo.select(row['bookings_id'])
        treatinbook = Treatinbook(booking, treatment, row['id'])
    return treatinbook

def update(treatinbook):
    sql = "UPDATE treatments_bookings SET (bookings_id, treatments_id) VALUES (%s, %s) WHERE id = %s"
    values = [treatinbook.booking.id, treatinbook.treatment.id, treatinbook.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM treatments_bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)