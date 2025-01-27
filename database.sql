-- Active: 1737981361472@@127.0.0.1@5433
CREATE TABLE mahasiswa (
    id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    npm VARCHAR(10) NOT NULL,
    major VARCHAR(50) NOT NULL,
    faculty VARCHAR(50) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    year_in INT NOT NULL,
    PRIMARY KEY (id)
);

SELECT * FROM mahasiswa;