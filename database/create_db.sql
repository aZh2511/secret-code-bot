CREATE TABLE IF NOT EXISTS users
(
    chat_id   bigint            not null
        constraint users_pk
            primary key,
    username  text,
    full_name text,
    adding_date   timestamp,
    id        serial            not null
);

alter table users
    owner to postgres;

create unique index users_id_uindex
    on users (id);

create table if not exists code
(
    secret_code text,
    id        serial            not null
);

alter table code
    owner to postgres;

CREATE TABLE IF NOT EXISTS whitelist
(
    chat_id   bigint            not null
        constraint users_pk
            primary key,
    id        serial            not null
);

alter table whitelist
    owner to postgres;


CREATE TABLE IF NOT EXISTS texts
(
    message   text,
    button    text,
    id        serial            not null
);

alter table whitelist
    owner to postgres;
