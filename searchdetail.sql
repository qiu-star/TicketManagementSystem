create or replace function searchdetail(sname character varying,
 										smonth smallint, sdate smallint, 
										out trainnum text, out aimname text, 
										out traintype text, out dtime text, 
										out checkentrance text)
returns setof record as $$
declare
	asid character(9);
	rec record;
begin
	select s_sid into asid from station where s_sname = sname;
	for rec in select dt_tid, dt_aimsid, dt_trainnum, dt_departuretime, dt_ticketentrance from departuretime
				where dt_month = smonth and dt_date = sdate loop
		if asid in (select r_sid from route where r_trainnum = rec.dt_trainnum)
		then
			trainnum := rec.dt_trainnum;
			aimname := (select s_sname from station where s_sid = rec.dt_aimsid);
			traintype := (select t_ttype from train where t_tid = rec.dt_tid);
			dtime := rec.dt_departuretime;
			checkentrance := rec.dt_ticketentrance;
		end if;
		return next;
	end loop;
end;
$$ language plpgsql;