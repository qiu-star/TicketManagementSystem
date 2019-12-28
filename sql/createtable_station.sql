-- Table: public.station

-- DROP TABLE public.station;

CREATE TABLE public.station
(
    s_sid character(9) COLLATE pg_catalog."default" NOT NULL,
    s_sname character varying COLLATE pg_catalog."default" NOT NULL,
    s_slongitude double precision,
    s_slatitude double precision,
    CONSTRAINT station_pkey PRIMARY KEY (s_sid)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.station
    OWNER to postgres;

GRANT SELECT ON TABLE public.station TO conductor;

GRANT ALL ON TABLE public.station TO manager;

GRANT ALL ON TABLE public.station TO postgres;

COMMENT ON TABLE public.station
    IS '站点';

COMMENT ON COLUMN public.station.s_slongitude
    IS '站点经度';

COMMENT ON COLUMN public.station.s_slatitude
    IS '纬度';

-- Index: six

-- DROP INDEX public.six;

CREATE INDEX six
    ON public.station USING hash
    (s_sid COLLATE pg_catalog."default")
    TABLESPACE pg_default;

-- Trigger: insert_s

-- DROP TRIGGER insert_s ON public.station;

CREATE TRIGGER insert_s
    BEFORE INSERT
    ON public.station
    FOR EACH ROW
    EXECUTE PROCEDURE public.insert_s_t();