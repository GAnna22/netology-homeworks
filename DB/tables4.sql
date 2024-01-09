-- 1
select track_name, duration
from tracks
where duration = (select MAX(duration) from tracks);

-- 2
select track_name
from tracks
where duration >= 210;

-- 3
select name 
from collection 
where (extract(year from collection.year) >= 2018) and 
(extract(year from collection.year) <= 2020);

-- 4
select perf_name 
from performers 
where length(perf_name) - length(replace(perf_name, ' ', '')) = 0;

-- 5
select track_name
from tracks 
where track_name ilike '%my%' or track_name ilike '%мой%';