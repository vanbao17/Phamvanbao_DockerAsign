create database Books;
create table base_menu (
	id_base_menu int primary key not null,
	title nvarchar(50) not null,
    content_type varchar(50) not null
);
create table detail_base_menu (
	id_detail_base_menu int  not null,
    id_base_menu int not null ,
    name nvarchar(50),
    orders int,
    description text,
    type int,
    status int,
    thumb text,
    content_detail_url text,
    primary key (id_detail_base_menu),
    FOREIGN KEY (id_base_menu) REFERENCES base_menu(id_base_menu)
);
create table books (
	id_book int not null,
    title nvarchar(200) not null,
    author nvarchar(100) not null,
    thumb text not null,
    content_type varchar(50) not null,
    liked int not null,
    price int not null,
    primary key (id_book)
);
create table detail_books(
	id_detail_book int not null,
    id_book int not null,
    description text not null,
    file_path text,
    updated_time varchar(100),
	foreign key (id_book) references books(id_book)
);
create table rate_of_books (
	content_id int not null,
    id_book int not null,
    created_time varchar(100) not null,
    name nvarchar(50) not null,
    content text not null,
    rate int,
    primary key (content_id),
    foreign key (id_book) references books(id_book)
)