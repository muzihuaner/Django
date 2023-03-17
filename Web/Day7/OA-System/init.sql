create database unicom DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
use unicom;
create table admin(
    id int auto_increment primary key,
    username varchar(64) not null,
    password char(64) not null,
    mobile char(11) not null
)default charset=utf8;