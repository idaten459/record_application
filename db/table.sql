CREATE TABLE records (
  id serial PRIMARY KEY,
  user_id integer NOT NULL,
  date date NOT NULL,
  category varchar(255) NOT NULL,
  sets integer NOT NULL,
  reps integer NOT NULL,
  weight integer NOT NULL
);
