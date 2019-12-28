-- View: public.c_tc

-- DROP VIEW public.c_tc;

CREATE OR REPLACE VIEW public.c_tc
 AS
 SELECT conductor.c_cid,
    conductor.c_cname,
    count(*) AS count
   FROM conductor,
    ticket
  WHERE ticket.tc_cid = conductor.c_cid AND ticket.tc_ifrefund = false
  GROUP BY conductor.c_cid, conductor.c_cname;

ALTER TABLE public.c_tc
    OWNER TO postgres;

GRANT ALL ON TABLE public.c_tc TO postgres;
GRANT SELECT ON TABLE public.c_tc TO manager;