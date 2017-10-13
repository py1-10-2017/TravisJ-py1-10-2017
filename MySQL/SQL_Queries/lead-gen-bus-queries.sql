#Total revenue for march of 2012
select sum(amount) as total_billed
from billing
where charged_datetime between '2012-03-01' and '2012-03-31';

#Total revenue for client=2
select c.client_id, sum(amount) as revenue_collected
from billing b
	inner join clients c on c.client_id = b.client_id
where c.client_id = 2;

#All sites owned by client 10
select domain_name as website, c.client_id
from sites s
	inner join clients c on c.client_id = s.client_id
where c.client_id = 10;

# What query would you run to get total # of sites created each month for client=1 ? What about for client=20?
select c.client_id, count(site_id) as number_of_websites, monthname(s.created_datetime) as month_created, year(s.created_datetime) as year_created
from sites s
	inner join clients c on c.client_id = s.client_id
#where c.client_id = 1
where c.client_id = 20
group by month_created, year_created
order by year_created;

#What query would you run to get the total # of leads we have generated for each of our sites between January
#1st 2011 to February 15th 2011?
select domain_name as website, count(l.leads_id) as leads, concat(monthname(l.registered_datetime),' ', day(l.registered_datetime), ', ', year(l.registered_datetime)) as date_generated
from sites s
	left join leads l on l.site_id = s.site_id
where l.registered_datetime between '2011-01-01' and '2011-02-15'
group by website;

#What query would you run to get a list of client name and the total # of leads we have generated for each of our
#client between January 1st 2011 to December 31st 2011?
select concat(c.first_name, ' ', c.last_name) as client_name, count(l.leads_id) as number_of_leads
from clients c
	inner join sites s on s.client_id = c.client_id
	inner join leads l on l.site_id = s.site_id
where l.registered_datetime between '2011-01-01' and '2011-12-31'
group by c.client_id;

#What query would you run to get a list of client name and the total # of leads we have generated for each client
#each month between month 1 - 6 of Year 2011?
select concat(c.first_name, ' ', c.last_name) as client_name, count(l.leads_id) as number_of_leads, monthname(l.registered_datetime) as month_generated
from clients c
	inner join sites s on s.client_id = c.client_id
	inner join leads l on l.site_id = s.site_id
where l.registered_datetime between '2011-01-01' and '2011-06-30'
group by month_generated, client_name
order by l.registered_datetime;


#8 part 1
select concat(c.first_name, ' ', c.last_name) as client_name, s.domain_name as website, count(l.leads_id) as number_of_leads, concat(monthname(l.registered_datetime),' ', day(l.registered_datetime), ', ', year(l.registered_datetime)) as date_generated
from clients c
	inner join sites s on s.client_id = c.client_id
	inner join leads l on l.site_id = s.site_id
where l.registered_datetime between '2011-01-01' and '2011-12-31'
group by website, client_name
order by c.client_id, s.site_id;

#8 part 2
select concat(c.first_name, ' ', c.last_name) as client_name, s.domain_name as website, count(l.leads_id) as number_of_leads, concat(monthname(l.registered_datetime),' ', day(l.registered_datetime), ', ', year(l.registered_datetime)) as date_generated
from clients c
	inner join sites s on s.client_id = c.client_id
	inner join leads l on l.site_id = s.site_id
group by website, client_name
order by c.client_id, s.site_id;

#9
select concat(c.first_name, ' ', c.last_name) as client_name, sum(amount), monthname(charged_datetime) as month_charge, year(charged_datetime) as year_charge
from billing b
	inner join clients c on c.client_id = b.client_id
group by month_charge, year_charge, c.client_id
order by c.client_id, charged_datetime;

#10
select concat(c.first_name, ' ', c.last_name) as client_name,
group_concat(s.domain_name separator ' / ') as websites
from clients c
	left join sites s on s.client_id = c.client_id
group by c.client_id











