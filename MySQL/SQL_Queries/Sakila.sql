#Query number 1
select c.first_name, c.last_name, c.email, a.address, a.city_id, ct.city, a.postal_code
from customer c
	inner join address a on a.address_id = c.address_id
    inner join city ct on ct.city_id = a.city_id
    where a.city_id = 312;
    
#Query number 2
select title, description, release_year, rating, special_features, ca.name
from film f
inner join film_category fc on fc.film_id = f.film_id
inner join category ca on ca.category_id = fc.category_id
where ca.name = 'Comedy';

#Query number 3
select a.actor_id, a.first_name, a.last_name, f.film_id, f.title, f.description, f.release_year
from actor a
	inner join film_actor fa on fa.actor_id = a.actor_id
    inner join film f on f.film_id = fa.film_id
where a.actor_id = 5;

#Query number 4
select c.first_name, c.last_name, c.email, a.address, ct.city, a.postal_code
from customer c
	inner join address a on a.address_id = c.address_id
    inner join city ct on ct.city_id = a.city_id
where store_id = 1
and ct.city_id in(1,42,312,459);

#Query number 5
select f.title, f.description, f.release_year, f.rating, f.special_features
from film f
	inner join film_actor fa on fa.film_id = f.film_id
where rating = 'G'
and special_features like '%behind the scenes%'
and fa.actor_id = 15;

#Query number 6
select f.film_id, f.title, a.actor_id, a.first_name, a.last_name
from film f
	inner join film_actor fa on fa.film_id = f.film_id
    inner join actor a on a.actor_id = fa.actor_id
where f.film_id = 369;

#Query number 7
select f.film_id, f.title, f.description,f.release_year, f.rating, f.special_features, c.name, f.rental_rate
from film f
	inner join film_category fc on fc.film_id = f.film_id
    inner join category c on c.category_id = fc.category_id
where rental_rate = 2.99
and c.name = 'Drama';

#Query number 8
select a.actor_id, concat(a.first_name, ' ', a.last_name), f.film_id, f.title, f.description, f.release_year, f.rating, f.special_features, c.name as genre
from actor a
	inner join film_actor fa on fa.actor_id = a.actor_id
	inner join film f on f.film_id = fa.film_id
    inner join film_category fc on fc.film_id = f.film_id
    inner join category c on c.category_id = fc.category_id
where a.first_name = 'Sandra'
and a.last_name = 'Kilmer'
and c.name = 'Action'



