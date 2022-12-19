DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_id INTEGER NULL,
    parent_id INTEGER NULL
);

DROP TABLE IF EXISTS images;
CREATE TABLE images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    path TEXT NOT nULL,
    category_id INTEGER NULL
);

INSERT INTO groups (id, name) VALUES (1, "Разное");
INSERT INTO groups (id, name) VALUES (2, "Инфографика");
INSERT INTO groups (id, name) VALUES (3, "История");
INSERT INTO groups (id, name) VALUES (4, "Карты");

INSERT INTO categories (id, name, group_id) VALUES (1, "Разное 1.1", 1);
INSERT INTO categories (id, name, group_id, parent_id) VALUES (2, "Разное 2", 1, 1);
INSERT INTO categories (id, name, group_id, parent_id) VALUES (3, "Разное 3", 1, 2);
INSERT INTO categories (id, name, group_id) VALUES (4, "Разное 1.2", 1);
INSERT INTO categories (id, name, group_id) VALUES (5, "Разное 4", 1);
INSERT INTO categories (id, name, group_id) VALUES (6, "Разное 5", 2);
INSERT INTO categories (id, name, group_id) VALUES (7, "Разное 6", 3);

INSERT INTO images (id, name, path, category_id) VALUES (1, "image_1", "./static/uploads/image_1.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (2, "image_2", "./static/uploads/image_2.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (3, "image_3", "./static/uploads/image_3.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (4, "image_4", "./static/uploads/image_4.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (5, "image_5", "./static/uploads/image_5.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (6, "image_6", "./static/uploads/image_6.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (7, "image_7", "./static/uploads/image_7.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (8, "image_8", "./static/uploads/image_8.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (9, "image_9", "./static/uploads/image_9.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (10, "image_10", "./static/uploads/image_10.png", 1);

INSERT INTO images (id, name, path, category_id) VALUES (11, "image_11", "./static/uploads/image_11.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (12, "image_12", "./static/uploads/image_12.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (13, "image_13", "./static/uploads/image_13.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (14, "image_14", "./static/uploads/image_14.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (15, "image_15", "./static/uploads/image_15.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (16, "image_16", "./static/uploads/image_16.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (17, "image_17", "./static/uploads/image_17.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (18, "image_18", "./static/uploads/image_18.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (19, "image_19", "./static/uploads/image_19.png", 1);
INSERT INTO images (id, name, path, category_id) VALUES (20, "image_20", "./static/uploads/image_20.png", 1);

