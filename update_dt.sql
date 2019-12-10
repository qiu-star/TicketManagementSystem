create or replace function update_dt_t()
returns trigger as
$$
declare
	v_msg character varying;
begin
	if new.dt_tid is not null and new.dt_tid not in (select t_tid from train) then
		v_msg = 't_tid不符合外键约束';
		raise notice '%', v_msg;
		return null;
	end if;
	if new.dt_aimsid is not null and new.dt_aimsid not in(select s_sid from station) then
		v_msg = 's_sid不符合外键约束';
		raise notice '%', v_msg;
		return null;
	end if;
	v_msg = '修改成功';
	raise notice '%', v_msg;
	return new;
end;
$$ language plpgsql;

create trigger update_dt before update
on departuretime
for each row execute procedure update_dt_t();