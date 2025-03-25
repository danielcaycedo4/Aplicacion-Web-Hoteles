-- Eliminar datos existentes
DELETE FROM habitaciones;
DELETE FROM hoteles;
DELETE FROM ciudades;

-- Insertar ciudades
INSERT INTO ciudades (id, nombre) VALUES 
(1, 'Cali'), 
(2, 'Cartagena'), 
(3, 'Bogotá');

-- Insertar hoteles
INSERT INTO hoteles (id, nombre, ciudad_id, direccion) VALUES 
(1, 'Hotel Cali', 1, 'Dirección Cali'),
(2, 'Hotel Cartagena', 2, 'Dirección Cartagena'),
(3, 'Hotel Bogotá', 3, 'Dirección Bogotá');

-- Insertar habitaciones para Cali
INSERT INTO habitaciones (hotel_id, tipo, cantidad, precio) VALUES
(1, 'premium', 20, 200.00),
(1, 'VIP', 2, 500.00);

-- Insertar habitaciones para Cartagena
INSERT INTO habitaciones (hotel_id, tipo, cantidad, precio) VALUES
(2, 'estándar', 10, 100.00),
(2, 'premium', 1, 200.00);

-- Insertar habitaciones para Bogotá
INSERT INTO habitaciones (hotel_id, tipo, cantidad, precio) VALUES
(3, 'estándar', 20, 100.00),
(3, 'premium', 20, 200.00),
(3, 'VIP', 2, 500.00);
