-- все, что начинается с двух дефисов - это комментарий

CREATE TABLE IF NOT EXISTS Albums (
	album_id SERIAL PRIMARY KEY,
	album_name VARCHAR(256) NOT NULL,
	year date NOT NULL
);

CREATE TABLE IF NOT EXISTS Tracks (
	track_id SERIAL PRIMARY KEY,
	track_name VARCHAR(256) NOT NULL,
	duration INTEGER NOT NULL,
	album_id INTEGER NOT NULL REFERENCES Albums(album_id)
);

CREATE TABLE IF NOT EXISTS Collection (
	id SERIAL PRIMARY KEY,
	name VARCHAR(256) NOT NULL,
	year date NOT NULL
);

CREATE TABLE IF NOT EXISTS TrackCollection (
	collection_id INTEGER REFERENCES Collection(id),
	track_id INTEGER REFERENCES Tracks(track_id),
	CONSTRAINT pk PRIMARY KEY (collection_id, track_id)
);

CREATE TABLE IF NOT EXISTS Performers (
	perf_id SERIAL PRIMARY KEY,
	perf_name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS AlbumPerformer (
	album INTEGER REFERENCES Albums(album_id),
	performer INTEGER REFERENCES Performers(perf_id),
	CONSTRAINT pk2 PRIMARY KEY (album, performer)
);

CREATE TABLE IF NOT EXISTS Genre (
	genre_id SERIAL PRIMARY KEY,
	genre_name VARCHAR(256) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS PerfGenre (
	perf_id INTEGER REFERENCES Performers(perf_id),
	genre_id INTEGER REFERENCES Genre(genre_id),
	CONSTRAINT pk3 PRIMARY KEY (perf_id, genre_id)
);
