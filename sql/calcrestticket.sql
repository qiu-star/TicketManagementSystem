-- FUNCTION: public.calcrestticket(character)

-- DROP FUNCTION public.calcrestticket(character);

CREATE OR REPLACE FUNCTION public.calcrestticket(
	trainnum character)
    RETURNS smallint
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE 
AS $BODY$
declare
	sumticket smallint;
	sold smallint;
begin
	select t_seatnum into sumticket from train, departuretime where dt_trainnum = trainnum and dt_tid = t_tid;
	select count(*) into sold from ticket where tc_trainnum = trainnum;
	return cast((sumticket - sold) as smallint);
end;
$BODY$;

ALTER FUNCTION public.calcrestticket(character)
    OWNER TO postgres;