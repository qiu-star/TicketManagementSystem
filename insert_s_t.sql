create or replace function insert_s_t()
returns trigger as
$$
declare
	tmp character(9);
begin
	select max(s_sid) into tmp from station;
	tmp = cast(tmp as integer) + 1;
	new.s_sid = cast(tmp as character(9));
	return new; 
end;
$$ language plpgsql;

create trigger insert_s before insert
on station
for each row execute procedure insert_s_t();