-- все, что начинается с двух дефисов - это комментарий

INSERT INTO Performers(perf_name)
VALUES
	('Elton John'),
	('Celine Dion'),
	('Freddie Mercury'),
	('Sting');

INSERT INTO Albums
VALUES 
	(1, 'Ice On Fire', to_date(1985::text, 'YYYY')),
	(2, 'You are The Inspiration', to_date(2008::text, 'YYYY')),
	(3, 'Messenger Of The Gods', to_date(2016::text, 'YYYY')),
	(4, 'Night Call', to_date(2022::text, 'YYYY')),
	(5, '...Nothing Like The Sun', to_date(1987::text, 'YYYY'));


INSERT INTO Tracks
VALUES 
	(1, 'Shoot Down The Moon', 295, 1),
	(2, 'Its a sin', 284, 4),
	(3, 'Because You Loved Me (Live)', 148, 2),
	(4, 'In My Defence', 234, 3),
	(5, 'Fragile', 234, 5),
	(6, 'Englishman In New York', 234, 5);

INSERT INTO Genre
VALUES 
	(1, 'pop'),
	(2, 'rock'),
	(3, 'soul');

INSERT INTO PerfGenre
VALUES 
	(1, 1),
	(1, 2),
	(2, 3),
	(3, 2),
	(4, 1);

INSERT INTO AlbumPerformer
VALUES
	(1, 1),
	(4, 1),
	(2, 2),
	(3, 3),
	(5, 4);

INSERT INTO Collection
VALUES 
	(1, 'Old collection', to_date(2018::text, 'YYYY')),
	(2, 'My first collection', to_date(2020::text, 'YYYY')),
	(3, 'My second collection', to_date(2022::text, 'YYYY')),
	(4, 'My third collection', to_date(2023::text, 'YYYY'));

INSERT INTO TrackCollection
VALUES 
	(1, 1),
	(1, 5),
	(1, 6),
	(2, 2),
	(2, 3),
	(3, 4),
	(4, 2);
