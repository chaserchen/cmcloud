CREATE TABLE student(
    id SERIAL PRIMARY KEY,
    number VARCHAR(16) NOT NULL,
    name VARCHAR(16) NOT NULL,
    mobile VARCHAR(16) NOT NULL,
    email VARCHAR(32),
    class_id INT NOT NULL REFERENCES class,
    password VARCHAR(32) NOT NULL
);