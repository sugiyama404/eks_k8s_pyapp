DROP TABLE IF EXISTS todos;

CREATE TABLE todos
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    content TEXT DEFAULT NULL
);

INSERT INTO todos (content) VALUES ("Nagaoka");
INSERT INTO todos (content) VALUES ("Tanaka");
