create or replace function refundticket(tcid character(9), money double precision)
returns void as $$
declare
	ddate date;
begin
	select current_date into ddate;
	lock ticket;
	update ticket set tc_ifrefund = true where tc_tcid = tcid;
	insert into refund(rf_tcid, rf_time, rf_money)
		values(tcid, ddate, money);
end;
$$ language plpgsql;