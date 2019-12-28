create or replace function insert_m_t()
returns trigger as
$$
declare
	tmp character(9);
begin
	select max(m_mid) into tmp from manager;
	tmp = cast(tmp as integer) + 1;
	new.m_mid = cast(tmp as character(9));
	return new; 
end;
$$ language plpgsql;

create trigger insert_m before insert
on manager
for each row execute procedure insert_m_t();