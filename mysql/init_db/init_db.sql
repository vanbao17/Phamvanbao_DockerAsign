CREATE DATABASE IF NOT EXISTS BooksWaka;
USE BooksWaka;

CREATE TABLE IF NOT EXISTS base_menu (
    id_base_menu INT PRIMARY KEY NOT NULL,
    title VARCHAR(50) NOT NULL,
    content_type VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS detail_base_menu (
    id_detail_base_menu INT NOT NULL,
    id_base_menu INT NOT NULL,
    name VARCHAR(50),
    orders INT,
    description TEXT,
    type INT,
    status INT,
    thumb TEXT,
    content_detail_url TEXT,
    PRIMARY KEY (id_detail_base_menu),
    FOREIGN KEY (id_base_menu) REFERENCES base_menu(id_base_menu)
);

CREATE TABLE IF NOT EXISTS books (
    id_book INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(200) NOT NULL,
    thumb TEXT NOT NULL,
    content_type VARCHAR(50) NOT NULL,
    liked INT NOT NULL,
    price INT NOT NULL,
    PRIMARY KEY (id_book)
) ;

CREATE TABLE IF NOT EXISTS detail_books (
    id_detail_book INT NOT NULL,
    id_book INT NOT NULL,
    description TEXT NOT NULL,
    file_path TEXT,
    updated_time VARCHAR(100),
    FOREIGN KEY (id_book) REFERENCES books(id_book)
);

CREATE TABLE IF NOT EXISTS rate_of_books (
    content_id INT NOT NULL,
    id_book INT NOT NULL,
    created_time VARCHAR(100) NOT NULL,
    name VARCHAR(50) NOT NULL,
    content TEXT NOT NULL
)

