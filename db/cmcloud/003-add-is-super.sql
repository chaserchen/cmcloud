ALTER TABLE teacher ADD COLUMN is_super BOOLEAN NOT NULL DEFAULT FALSE;
CREATE INDEX teacher_mobile_idx ON teacher(mobile);

INSERT INTO teacher(name, mobile, password) values ('邓晨迪', '18879331009', '1fd0e96081a7de6116d12a442b0187ff', TRUE); -- 密码默认为手机号的md5加密后的值