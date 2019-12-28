-- Table: public.manager

-- DROP TABLE public.manager;

CREATE TABLE public.manager
(
    m_mid character(9) COLLATE pg_catalog."default" NOT NULL,
    m_mname character varying COLLATE pg_catalog."default" NOT NULL,
    m_mpassword character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT manager_pkey PRIMARY KEY (m_mid),
    CONSTRAINT muq_manme UNIQUE (m_mname)

)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.manager
    OWNER to postgres;

GRANT ALL ON TABLE public.manager TO manager;

GRANT ALL ON TABLE public.manager TO postgres;

-- Trigger: insert_m

-- DROP TRIGGER insert_m ON public.manager;

CREATE TRIGGER insert_m
    BEFORE INSERT
    ON public.manager
    FOR EACH ROW
    EXECUTE PROCEDURE public.insert_m_t();