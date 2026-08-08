CREATE TABLE IF NOT EXISTS "banks" (
        "bank_id"       INTEGER,
        "bank_name"     VARCHAR(128) NOT NULL,
        PRIMARY KEY("bank_id")
);

CREATE TABLE IF NOT EXISTS "entities" (
        "entity_id"     VARCHAR(128),
        "entity_name"   VARCHAR(128) NOT NULL,
        PRIMARY KEY("entity_id")
);

CREATE TABLE IF NOT EXISTS "accounts" (
        "account_id"    INTEGER AUTO_INCREMENT,
        "entity_id"     VARCHAR(128) NOT NULL,
        "bank_id"       INTEGER NOT NULL,
        "account_number" VARCHAR(128) NOT NULL,
        PRIMARY KEY("account_id"),
        FOREIGN KEY("entity_id") REFERENCES "entities"("entity_id"),
        FOREIGN KEY("bank_id") REFERENCES "banks"("bank_id"),
        UNIQUE("bank_id", "account_number")
);