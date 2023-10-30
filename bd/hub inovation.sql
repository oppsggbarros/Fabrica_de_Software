create database hub_innovation char set utf8mb4 collate utf8mb4_unicode_ci;
use hub_innovation;
drop database hub;


create table palestra(
palestra_id int primary key auto_increment,
palestra_tema varchar(150) not null,
palestra_desc text,
palestrante_linkedin varchar(200),
palestrante_instagram varchar(200),
palestrante varchar(50) not null,
sala varchar(5) not null,
profile_image_url varchar(300),
vagas int
);

insert into palestra(palestra_tema, palestra_desc, palestrante_linkedin, palestrante_instagram, palestrante, sala, profile_image_url, vagas) values 
("Modelagem 3D","Modelagem 3D de Personagens", "Gabriel.linkedin", "Gabriel.instagram", "Gabriel", "310", "https@@######@", 20),
("IA", "Introdução À inteligencia artificial","Nerevaldo.linkedin", "Nerevaldo.instagram", "Nerevaldo", "306", "https@@######@", 20),
("C#", "Programação em C#", "Faz o L", "Faz o L2", "Lula", "307", "https@@######@", 20);

create table usuario(
user_id int primary key auto_increment,
nome varchar(50) not null,
usuario_palestra_id int not null,
constraint foreign key (usuario_palestra_id) references palestra(palestra_id),
cpf varchar(12) not null,
email varchar(30) not null,
genero varchar(1) not null,
nasc date not null,
permission bool not null
);

delimiter $

create trigger Tgr_Usuario_Insert after insert on usuario
for each row
begin
update palestra set vagas = vagas - 1
where new.usuario_palestra_id = palestra_id;
end$

create trigger Tgr_Usuario_Del after delete on usuario
for each row
begin
update palestra set vagas = vagas + 1
where old.usuario_palestra_id = palestra_id;
end$

delimiter ; 

select * from palestra;  

set sql_safe_updates = 0;







