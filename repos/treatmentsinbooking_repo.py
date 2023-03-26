from db.run_sql import run_sql

def save(booking, treatment):
    sql = 

    def save(booking):
    sql = "INSERT INTO treatments_bookings (treatments_id, bookings_id) VALUES (%s, %s, %s) RETURNING id"
    values = [booking.name, booking.duration, booking.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id