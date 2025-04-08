CREATE TABLE IF NOT EXISTS "items"
(
    id       integer        not null
        constraint items_pk
            primary key autoincrement,
    name     TEXT           not null,
    price    REAL default 0 not null,
    is_offer INT  default 0
);