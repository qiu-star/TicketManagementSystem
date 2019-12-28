-- Table: public.refund

-- DROP TABLE public.refund;

CREATE TABLE public.refund
(
    rf_tcid character(9) COLLATE pg_catalog."default" NOT NULL,
    rf_time date NOT NULL,
    rf_money double precision NOT NULL,
    CONSTRAINT rfpk PRIMARY KEY (rf_tcid, rf_time),
    CONSTRAINT rffk_tcid FOREIGN KEY (rf_tcid)
        REFERENCES public.ticket (tc_tcid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.refund
    OWNER to postgres;

GRANT INSERT ON TABLE public.refund TO conductor;

GRANT ALL ON TABLE public.refund TO manager;

GRANT ALL ON TABLE public.refund TO postgres;

COMMENT ON TABLE public.refund
    IS '退票表';

COMMENT ON COLUMN public.refund.rf_money
    IS '退回的钱';