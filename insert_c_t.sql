create or replace function insert_c_t()
returns trigger as
$$
declare
	tmp character(9);
begin
	select max(c_cid) into tmp from conductor;
	tmp = cast(tmp as integer) + 1;
	new.c_cid = cast(tmp as character(9));
	return new; 
end;
$$ language plpgsql;

create trigger insert_c before insert
on conductor
for each row execute procedure insert_c_t();