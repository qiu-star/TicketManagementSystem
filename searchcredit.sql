create or replace function searchcredit(credit character(18), out ddate date, out trainnum character(9),
										out aimsname character varying, out price double precision, out seatnum smallint)
returns setof record as $$
declare
	rec record;
begin
	for rec in select tc_date, tc_trainnum, s_sname, tc_price, tc_seatnum from ticket, station
				where tc_aimsid = s_sid and tc_custid = credit and tc_ifrefund = false loop
		ddate := rec.tc_date;
		trainnum := rec.tc_trainnum;
		aimsname := rec.s_sname;
		price := rec.tc_price;
		seatnum := rec.tc_seatnum;
		return next;
	end loop;
end;
$$ language plpgsql;
	