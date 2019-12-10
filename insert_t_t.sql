create or replace function insert_t_t()
returns trigger as
$$
declare
	tmp character(9);
begin
	select max(t_tid) into tmp from train;
	tmp = cast(tmp as integer) + 1;
	new.t_tid = cast(tmp as character(9));
	return new; 
end;
$$ language plpgsql;

create trigger insert_t before insert
on train
for each row execute procedure insert_t_t();