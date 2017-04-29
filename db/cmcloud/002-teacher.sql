CREATE TABLE teacher(
    id SERIAL PRIMARY KEY,
    name VARCHAR(16) NOT NULL,
    mobile VARCHAR(16) NOT NULL,
    email VARCHAR(32),
    password VARCHAR(32) NOT NULL
);