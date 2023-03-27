DROP TABLE IF EXISTS treatments_bookings;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS treatments;

CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    duration INT,
    description TEXT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date DATE,
    time TIME
);

CREATE TABLE treatments_bookings (
    id SERIAL PRIMARY KEY,
    bookings_id INT NOT NULL REFERENCES bookings(id) ON DELETE CASCADE,
    treatments_id INT NOT NULL REFERENCES treatments(id) ON DELETE CASCADE
);

INSERT INTO treatments (id, name, duration, description) VALUES (1, 'BASIC B*TCH', 30, 'For the simple folks out there. A general tidy up and colour.'); 
INSERT INTO treatments (id, name, duration, description) VALUES (2, 'BOUJEE', 40, 'For the classy folks out there. BASIC B*TCH plus simple nail art.');
INSERT INTO treatments (id, name, duration, description) VALUES (3, 'EXTRA AF', 50, 'For those who like to take it up a notch. No request is too crazy.'); 