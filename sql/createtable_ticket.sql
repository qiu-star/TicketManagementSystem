-- Table: public.ticket

-- DROP TABLE public.ticket;

CREATE TABLE public.ticket
(
    tc_tcid character(9) COLLATE pg_catalog."default" NOT NULL,
    tc_date date NOT NULL,
    tc_trainnum character(9) COLLATE pg_catalog."default" NOT NULL,
    tc_aimsid character(9) COLLATE pg_catalog."default" NOT NULL,
    tc_price double precision NOT NULL,
    tc_seatnum smallint NOT NULL,
    tc_cid character(9) COLLATE pg_catalog."default" NOT NULL,
    tc_ifrefund boolean DEFAULT false,
    tc_custid character(18) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT ticket_pkey PRIMARY KEY (tc_tcid),
    CONSTRAINT tcfk_cid FOREIGN KEY (tc_cid)
        REFERENCES public.conductor (c_cid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT tcfk_sid FOREIGN KEY (tc_aimsid)
        REFERENCES public.station (s_sid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT tcfk_trainnum FOREIGN KEY (tc_trainnum)
        REFERENCES public.departuretime (dt_trainnum) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.ticket
    OWNER to postgres;

GRANT ALL ON TABLE public.ticket TO manager;

GRANT ALL ON TABLE public.ticket TO postgres;

GRANT INSERT, SELECT, UPDATE ON TABLE public.ticket TO conductor;

COMMENT ON TABLE public.ticket
    IS '车票表';

COMMENT ON COLUMN public.ticket.tc_aimsid
    IS '终点站';

COMMENT ON COLUMN public.ticket.tc_cid
    IS '售票员员工号';

COMMENT ON COLUMN public.ticket.tc_ifrefund
    IS '退票否';