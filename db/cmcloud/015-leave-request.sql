CREATE TABLE leave_request (
    id SERIAL PRIMARY KEY,
    student_id INT NOT NULL REFERENCES student,
    teacher_id INT REFERENCES teacher,
    reason VARCHAR(256) NOT NULL,
    teacher_memo VARCHAR(256),
    status SMALLINT NOT NULL DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP WITH TIME ZONE
);
CREATE INDEX leave_request_student_id_idx ON leave_request(student_id);
