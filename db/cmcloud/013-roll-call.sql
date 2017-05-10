CREATE TABLE roll_call (
    id SERIAL PRIMARY KEY,
    class_id INT NOT NULL REFERENCES class,
    on_student_ids INT[] NOT NULL DEFAULT '{}',
    off_student_ids INT[] NOT NULL DEFAULT '{}',
    leave_student_ids INT[] NOT NULL DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX roll_call_class_id_idx ON roll_call(class_id);
