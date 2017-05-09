DELETE FROM teacher;
ALTER TABLE teacher DROP CONSTRAINT teacher_mobile_key;
ALTER TABLE teacher ADD COLUMN number VARCHAR(16) NOT NULL UNIQUE;

INSERT INTO teacher(name, number, mobile, password, is_super) values ('邓晨迪', '20170101', '18879331009', '1fd0e96081a7de6116d12a442b0187ff', TRUE); -- 密码默认为手机号的md5加密后的值
