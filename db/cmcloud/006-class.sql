CREATE TABLE class(
    id SERIAL PRIMARY KEY,
    code VARCHAR(16) NOT NULL,
    name VARCHAR(16) NOT NULL
);
INSERT INTO class (code, name) values ('20170101', '软件一班');