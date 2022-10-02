-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/AqyzFn
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "country" (
    "country_code" varchar   NOT NULL,
    "country_name" varchar   NOT NULL,
    "lat" float   NOT NULL,
    "lon" float   NOT NULL,
    CONSTRAINT "pk_country" PRIMARY KEY (
        "country_code"
     )
);

CREATE TABLE "item_element" (
    "item_element_id" integer   NOT NULL,
    "item_name" varchar   NOT NULL,
    "element_type" varchar   NOT NULL,
    CONSTRAINT "pk_item_element" PRIMARY KEY (
        "item_element_id"
     )
);

CREATE TABLE "amount" (
    "amount_id" serial   NOT NULL,
    "country_code" varchar   NOT NULL,
    "item_element_id" integer   NOT NULL,
    "year" integer   NOT NULL,
    CONSTRAINT "pk_amount" PRIMARY KEY (
        "amount_id"
     )
);

CREATE TABLE "year" (
    "year" integer   NOT NULL,
    "temperature" float   NOT NULL,
    "temperature_uncertainty" float   NOT NULL,
    CONSTRAINT "pk_year" PRIMARY KEY (
        "year"
     )
);

ALTER TABLE "amount" ADD CONSTRAINT "fk_amount_country_code" FOREIGN KEY("country_code")
REFERENCES "country" ("country_code");

ALTER TABLE "amount" ADD CONSTRAINT "fk_amount_item_element_id" FOREIGN KEY("item_element_id")
REFERENCES "item_element" ("item_element_id");

