from db.run_sql import run_sql
from models.booking import Booking
import repos.treatments_repo as treatments_repo

def save(booking):
    sql = "INSERT INTO bookings (date, time, treatments_id) VALUES (%s, %s, %s) RETURNING id"
    values = [booking.date, booking.time, booking.treatment.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        treatment = treatments_repo.select(row['treatments_id'])
        booking = Booking(row['date'], row['time'], treatment, row['id'])
        bookings.append(booking)
    return bookings

def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        treatment = treatments_repo.select(row['treatments_id'])
        booking = Booking(row['date'], row['time'], treatment, row['id'])
    return booking

def update(booking):
    sql = "UPDATE bookings SET (date, time, treatments_id) VALUES (%s, %s) WHERE id = %s"
    values = [booking.date, booking.time, booking.treatment.id, booking.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM booking WHERE id = %s"
    values = [id]
    run_sql(sql, values)
