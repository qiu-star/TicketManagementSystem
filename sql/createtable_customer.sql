-- Table: public.customer

-- DROP TABLE public.customer;

CREATE TABLE public.customer
(
    cust_custid character(18) COLLATE pg_catalog."default" NOT NULL,
    cust_custname character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT customer_pkey PRIMARY KEY (cust_custid)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.customer
    OWNER to postgres;

GRANT INSERT, SELECT ON TABLE public.customer TO conductor;

GRANT ALL ON TABLE public.customer TO manager;

GRANT ALL ON TABLE public.customer TO postgres;

COMMENT ON TABLE public.customer
    IS '顾客';

COMMENT ON COLUMN public.customer.cust_custid
    IS '身份证号';