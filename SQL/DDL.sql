CREATE TABLE public.usuario (
	id_usuario int4 NOT NULL,
	nombre bpchar(64) NOT NULL,
	contrasenia bpchar(128) NOT NULL,
	direccion varchar NULL,
	CONSTRAINT usuario_pk PRIMARY KEY (id_usuario),
	CONSTRAINT usuario_un UNIQUE (nombre)
);