create or replace function sellticket(num smallint, trainnum character(9), s_date character varying,
									 aimsname character varying, price double precision, cname character varying,
									 custid character(18))
returns void as
$$
declare
	idcnt integer;
	i smallint;
	aimsid character(9);
	cid character(9);
	seatnum smallint;
begin
	i = 0;
	select s_sid into aimsid from station where s_sname = aimsname;
	select c_cid into cid from conductor where c_cname = cname;
	lock ticket;
	select count(*) into idcnt from ticket;
	idcnt = idcnt + 1;
	while i < num loop
		select max(tc_seatnum) into seatnum from ticket where tc_trainnum = trainnum;
		if seatnum = null
		then 
			seatnum = 0;
		end if;
		seatnum = seatnum + 1;
		insert into ticket(tc_tcid, tc_date, tc_trainnum,tc_aimsid, tc_price, tc_seatnum, tc_cid, tc_custid)
						  values(cast(idcnt as character(9)), cast(s_date as date), trainnum, aimsid,
								price, seatnum, cid, custid);
		i = i + 1;
		end loop;
end;
$$ language plpgsql;