-- все, что начинается с двух дефисов - это комментарий

CREATE TABLE IF NOT EXISTS Employee (
	empl_id SERIAL PRIMARY KEY,
	empl_name VARCHAR(256) NOT NULL,
	department VARCHAR(256) NOT NULL,
	boss INTEGER REFERENCES Employee(empl_id)
);

