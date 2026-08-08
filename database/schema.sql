CREATE TABLE IF NOT EXISTS "banks" (
        "bank_id"       INTEGER,
        "bank_name"     VARCHAR(128) NOT NULL,
        PRIMARY KEY("bank_id")
);

CREATE TABLE IF NOT EXISTS "entities" (
        "entity_id"     INTEGER,
        "entity_name"   VARCHAR(128) NOT NULL,
        PRIMARY KEY("entity_id")
);