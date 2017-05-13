CREATE TABLE homework (
    id SERIAL PRIMARY KEY,
    teacher_id INT NOT NULL REFERENCES teacher,
    class_id INT NOT NULL REFERENCES class,
    content VARCHAR(256) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX homework_teacher_id ON homework(teacher_id);

CREATE TABLE homework_answer (
    id SERIAL PRIMARY KEY,
    student_id INT NOT NULL REFERENCES student,
    homework_id INT NOT NULL REFERENCES homework,
    answer VARCHAR(256) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX homework_answer_student_id ON homework_answer(student_id);
