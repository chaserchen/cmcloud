CREATE TABLE notification (
    id SERIAL PRIMARY KEY,
    teacher_id INT NOT NULL REFERENCES teacher,
    class_id INT REFERENCES class,
    type SMALLINT NOT NULL,
    content VARCHAR(256) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX notification_class_id_idx ON notification(class_id);