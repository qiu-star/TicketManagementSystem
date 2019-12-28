-- Table: public.train

-- DROP TABLE public.train;

CREATE TABLE public.train
(
    t_tid character(9) COLLATE pg_catalog."default" NOT NULL,
    t_ttype character(8) COLLATE pg_catalog."default" NOT NULL DEFAULT '空调硬座'::bpchar,
    t_seatnum smallint NOT NULL DEFAULT 0,
    CONSTRAINT car_pkey PRIMARY KEY (t_tid)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.train
    OWNER to postgres;

GRANT SELECT ON TABLE public.train TO conductor;

GRANT ALL ON TABLE public.train TO manager;

GRANT ALL ON TABLE public.train TO postgres;

COMMENT ON TABLE public.train
    IS '车辆表';

COMMENT ON COLUMN public.train.t_tid
    IS '车辆编号';

COMMENT ON COLUMN public.train.t_ttype
    IS '车型';

-- Index: tix

-- DROP INDEX public.tix;

CREATE INDEX tix
    ON public.train USING hash
    (t_tid COLLATE pg_catalog."default")
    TABLESPACE pg_default;

-- Trigger: insert_t

-- DROP TRIGGER insert_t ON public.train;

CREATE TRIGGER insert_t
    BEFORE INSERT
    ON public.train
    FOR EACH ROW
    EXECUTE PROCEDURE public.insert_t_t();