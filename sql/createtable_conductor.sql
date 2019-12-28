-- Table: public.conductor

-- DROP TABLE public.conductor;

CREATE TABLE public.conductor
(
    c_cid character(9) COLLATE pg_catalog."default" NOT NULL,
    c_cname character varying COLLATE pg_catalog."default" NOT NULL,
    c_cpassword character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT conductor_pkey PRIMARY KEY (c_cid),
    CONSTRAINT cuq_cname UNIQUE (c_cname)

)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.conductor
    OWNER to postgres;

GRANT SELECT ON TABLE public.conductor TO conductor;

GRANT ALL ON TABLE public.conductor TO manager;

GRANT ALL ON TABLE public.conductor TO postgres;

COMMENT ON TABLE public.conductor
    IS '售票员';

-- Trigger: insert_c

-- DROP TRIGGER insert_c ON public.conductor;

CREATE TRIGGER insert_c
    BEFORE INSERT
    ON public.conductor
    FOR EACH ROW
    EXECUTE PROCEDURE public.insert_c_t();