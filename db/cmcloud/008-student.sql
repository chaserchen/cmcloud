CREATE TABLE student(
    id SERIAL PRIMARY KEY,
    name VARCHAR(16) NOT NULL,
    mobile VARCHAR(16) NOT NULL,
    email VARCHAR(32),
    class_id INT NOT NULL REFERENCES class,
    password VARCHAR(32) NOT NULL
);