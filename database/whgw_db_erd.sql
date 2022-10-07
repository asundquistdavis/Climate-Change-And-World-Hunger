-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/AqyzFn
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.
CREATE TABLE "amount" (
    "amount_id" serial   NOT NULL,
    "amount" integer   NOT NULL,
    "country_code" varchar   NOT NULL,
    "category_id" integer   NOT NULL,
    "type" varchar   NOT NULL,
    "year" integer   NOT NULL,
    CONSTRAINT "pk_amount" PRIMARY KEY (
        "amount_id"
     )
);

CREATE TABLE "year" (
    "year" integer   NOT NULL,
    "temperature" float  NOT NULL,
    "temperature_unc" float   NOT NULL,
    CONSTRAINT "pk_year" PRIMARY KEY (
        "year"
     )
);