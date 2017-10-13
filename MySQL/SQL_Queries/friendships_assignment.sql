select u.first_name, u.last_name, u2.first_name, u2.last_name
from users u
	left join friends f on f.user_id = u.id
    left join users u2 on u2.id = f.friend_id
order by u.first_name, u2.last_name
