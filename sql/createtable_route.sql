-- Table: public.route

-- DROP TABLE public.route;

CREATE TABLE public.route
(
    r_trainnum character(9) COLLATE pg_catalog."default" NOT NULL,
    r_sid character(9) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT rpk PRIMARY KEY (r_trainnum, r_sid),
    CONSTRAINT rfk_sid FOREIGN KEY (r_sid)
        REFERENCES public.station (s_sid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID,
    CONSTRAINT rfk_trainnum FOREIGN KEY (r_trainnum)
        REFERENCES public.departuretime (dt_trainnum) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.route
    OWNER to postgres;

GRANT SELECT ON TABLE public.route TO conductor;

GRANT ALL ON TABLE public.route TO manager;

GRANT ALL ON TABLE public.route TO postgres;

COMMENT ON TABLE public.route
    IS '途径表';