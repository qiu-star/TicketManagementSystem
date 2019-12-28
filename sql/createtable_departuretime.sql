-- Table: public.departuretime

-- DROP TABLE public.departuretime;

CREATE TABLE public.departuretime
(
    dt_tid character(9) COLLATE pg_catalog."default" NOT NULL,
    dt_aimsid character(9) COLLATE pg_catalog."default" NOT NULL,
    dt_trainnum character(9) COLLATE pg_catalog."default" NOT NULL,
    dt_departuretime time(6) without time zone NOT NULL,
    dt_ticketentrance smallint NOT NULL,
    dt_month smallint NOT NULL,
    dt_date smallint NOT NULL,
    dt_cost double precision NOT NULL,
    CONSTRAINT leavefor_pkey PRIMARY KEY (dt_trainnum),
    CONSTRAINT lffk_carid FOREIGN KEY (dt_tid)
        REFERENCES public.train (t_tid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT lffk_sid FOREIGN KEY (dt_aimsid)
        REFERENCES public.station (s_sid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.departuretime
    OWNER to postgres;

GRANT SELECT ON TABLE public.departuretime TO conductor;

GRANT ALL ON TABLE public.departuretime TO manager;

GRANT ALL ON TABLE public.departuretime TO postgres;

COMMENT ON TABLE public.departuretime
    IS '发车时刻表';

COMMENT ON COLUMN public.departuretime.dt_trainnum
    IS '车次';

COMMENT ON COLUMN public.departuretime.dt_ticketentrance
    IS '检票口';

-- Index: dtix

-- DROP INDEX public.dtix;

CREATE INDEX dtix
    ON public.departuretime USING hash
    (dt_trainnum COLLATE pg_catalog."default")
    TABLESPACE pg_default;

-- Trigger: update_dt

-- DROP TRIGGER update_dt ON public.departuretime;

CREATE TRIGGER update_dt
    BEFORE UPDATE 
    ON public.departuretime
    FOR EACH ROW
    EXECUTE PROCEDURE public.update_dt_t();