-- все, что начинается с двух дефисов - это комментарий

CREATE TABLE IF NOT EXISTS Tracks (
	track_id SERIAL PRIMARY KEY,
	track_name VARCHAR(256) NOT NULL,
	duration INTERVAL NOT NULL,
	album INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Collection (
	id SERIAL PRIMARY KEY,
	name VARCHAR(256) NOT NULL,
	year date NOT NULL
);

CREATE TABLE IF NOT EXISTS TrackCollection (
	collection INTEGER REFERENCES Collection(id),
	track INTEGER REFERENCES Tracks(track_id),
	CONSTRAINT pk PRIMARY KEY (collection, track)
);

CREATE TABLE IF NOT EXISTS Albums (
	album_id SERIAL PRIMARY KEY REFERENCES Tracks(album),
	album_name VARCHAR(256) NOT NULL,
	performer INTEGER NOT NULL,
	year date NOT NULL
);

CREATE TABLE IF NOT EXISTS Performers (
	perf_id SERIAL PRIMARY KEY,
	perf_name VARCHAR(256) NOT NULL,
	genre INTEGER
);

CREATE TABLE IF NOT EXISTS AlbumPerformer (
	album INTEGER REFERENCES Albums(album_id),
	performer INTEGER REFERENCES Performers(perf_id),
	CONSTRAINT pk PRIMARY KEY (album, performer)
);

CREATE TABLE IF NOT EXISTS Genre (
	genre_id SERIAL PRIMARY KEY,
	genre_name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS perf_genre (
	performer INTEGER REFERENCES Performers(perf_id),
	genre INTEGER REFERENCES Genre(genre_id)
	CONSTRAINT pk PRIMARY KEY (performer, genre)
);
