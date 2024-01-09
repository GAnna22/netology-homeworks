-- 1
select count(perf_id) 
from perfgenre 
group by genre_id;

-- 2
select count(track_id) 
from tracks t
join albums a on t.album_id = a.album_id
where (extract(year from a.year) >= 2018) 
	and (extract(year from a.year) <= 2022);

-- 3
select avg(duration) avg_duration
from tracks t
join albums a on t.album_id = a.album_id
group by a.album_id;

-- 4
select perf_name
from performers p 
join albumperformer a on p.perf_id = a.performer 
join albums a2 on a2.album_id = a.album
where extract(year from a2.year) != 2020;

-- 5
select c.name  
from collection c 
join trackcollection t on c.id = t.collection_id 
join tracks t2 on t.track_id = t2.track_id 
join albums a on a.album_id = t2.album_id 
join albumperformer a2 on a2.album = a.album_id 
join performers p on p.perf_id = a2.performer
where p.perf_name = 'Elton John';
