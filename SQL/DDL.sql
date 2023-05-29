DROP SCHEMA IF EXISTS public CASCADE;

CREATE SCHEMA public;  -- Creamos el esquema publico

CREATE TABLE usuario (
	id_usuario SERIAL PRIMARY KEY,
	nombre VARCHAR(64) NOT NULL UNIQUE,
	contrasenia CHAR(128) NOT NULL
);

CREATE TABLE administrador (
	id_admin INT PRIMARY KEY REFERENCES usuario(id_usuario)
);

CREATE TABLE vendedor (
	id_vendedor INT PRIMARY KEY REFERENCES usuario(id_usuario)
);

CREATE TABLE categoria_inventario (
	id_categoria_inventario SERIAL PRIMARY KEY,
	nombre VARCHAR(128) UNIQUE NOT NULL
);

CREATE TABLE categoria_producto (
	id_categoria_producto SERIAL PRIMARY KEY,
	nombre VARCHAR(128) UNIQUE NOT NULL
);

CREATE TABLE inventario (
	id_inventario SERIAL PRIMARY KEY,
	nombre VARCHAR(128) UNIQUE NOT NULL,
	precio_adquisicion REAL NOT NULL,
	cantidad INT NOT NULL,
	id_categoria_inventario INT REFERENCES categoria_inventario(id_categoria_inventario) NOT NULL
);

CREATE TABLE producto (
	id_producto SERIAL PRIMARY KEY,
	nombre VARCHAR(128) UNIQUE NOT NULL,
	descripcion TEXT NOT NULL,
	precio REAL NOT NULL,
	disponible BOOLEAN NOT NULL,
	id_categoria_producto INT REFERENCES categoria_producto(id_categoria_producto) NOT NULL
);

CREATE TABLE producto_utiliza_inventario (
	id_producto INT REFERENCES producto(id_producto) NOT NULL,
	id_inventario INT REFERENCES inventario(id_inventario) NOT NULL
);

CREATE TABLE itinerario (
	id_itinerario SERIAL PRIMARY KEY,
	id_inventario INT REFERENCES inventario(id_inventario) NOT NULL,
	id_vendedor INT REFERENCES vendedor(id_vendedor) NOT NULL,
	cantidad INT NOT NULL,
	precio_total REAL NOT NULL,
	fecha_entrega DATE NOT NULL
);

CREATE TABLE orden (
    id_orden SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES usuario(id_usuario),
    estatus VARCHAR(20) NOT NULL, -- Change the data type to VARCHAR
    fecha DATE NOT NULL,
    total REAL NOT NULL
);

CREATE TABLE vendedor_atender_orden(
	id_vendedor INT REFERENCES vendedor(id_vendedor) NOT NULL,
	id_orden INT REFERENCES orden(id_orden) NOT NULL
);

CREATE TABLE pruductos_orden (
	id_producto INT REFERENCES producto(id_producto) NOT NULL,
	id_orden INT REFERENCES orden(id_orden) NOT NULL
);

CREATE TABLE reporte_ventas (
	id_reporte_ventas SERIAL PRIMARY KEY,
	id_vendedor INT REFERENCES vendedor(id_vendedor),
	fecha_inicio DATE NOT NULL,
	fecha_fin DATE NOT NULL,
	total REAL NOT NULL
);

CREATE TABLE productos_en_reporte (
	id_reporte_ventas INT REFERENCES reporte_ventas(id_reporte_ventas) NOT NULL,
	id_orden INT REFERENCES orden(id_orden) NOT NULL
);