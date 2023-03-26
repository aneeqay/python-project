DROP TABLE IF EXISTS treatments_bookings;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS treatments;

CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    duration TIME,
    description TEXT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date DATE,
    time TIME
);

CREATE TABLE treatments_bookings (
    id SERIAL PRIMARY KEY,
    treatments_id INT NOT NULL REFERENCES treatments(id) ON DELETE CASCADE,
    bookings_id INT NOT NULL REFERENCES bookings(id) ON DELETE CASCADE
)