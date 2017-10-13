select c.name, l.language, l.percentage
from world.countries c
	inner join world.languages l on l.country_id = c.id
    where language = 'slovene'
    order by l.percentage desc;
    
select c.name, count(cit.name) as cities
from world.cities cit
	inner join countries c on c.id = cit.country_id 
group by country_code
order by cities desc;

select name, population 
from world.cities
where country_code = 'MEX'
and cities.population > 500000
order by population desc;


select c.name, l.language, l.percentage from languages l
	inner join countries c on c.id = l.country_id
where percentage > 89
order by percentage desc;

select name, surface_area, population
from countries
where surface_area < 501
and population > 100000;

select name, government_form, capital, life_expectancy
from countries
where government_form = 'Constitutional Monarchy'
and capital > 200
and life_expectancy > 75;

select c.name, cit.name, cit.district, cit.population
from countries c
	inner join cities cit on cit.country_id = c.id
where cit.district = 'Buenos Aires'
and cit.population > 500000
order by cit.population desc;

select region, count(name) as country_count
from countries
	group by region
    order by country_count desc

