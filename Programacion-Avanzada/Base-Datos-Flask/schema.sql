
CREATE TABLE departamentos (
	id INTEGER NOT NULL, 
	nombre VARCHAR(50) NOT NULL, 
	PRIMARY KEY (id)
)

;


CREATE TABLE usuarios (
	id INTEGER NOT NULL, 
	nombre VARCHAR(50) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	id_departamento INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	FOREIGN KEY(id_departamento) REFERENCES departamentos (id)
)

;

-- Insertar datos iniciales en departamentos
INSERT INTO departamentos (id, nombre) VALUES
(1, 'Ventas'),
(2, 'Finanzas'),
(3, 'Recursos humanos');
