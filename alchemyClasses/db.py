from alchemyClasses import db


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False, unique=True)
    contrasenia = db.Column(db.String(128), nullable=False)
    direccion = db.Column(db.VARCHAR(256), nullable=True)

    def __init__(self, nombre, contrasenia):
        self.id_usuario = Usuario.query.order_by(Usuario.id_usuario.desc()).first().id_usuario + 1 # Puede arreglarse desde la bd
        self.nombre = nombre
        self.contrasenia = contrasenia


class Administrador(db.Model):
    __tablename__ = 'administrador'
    id_admin = db.Column(db.Integer, primary_key=True)

    def __init__(self, id_admin):
        self.id_admin = id_admin


class Vendedor(db.Model):
    __tablename__ = 'vendedor'
    id_vendedor = db.Column(db.Integer, primary_key=True)

    def __init__(self, id_vendedor):
        self.id_vendedor = id_vendedor


class CategoriaInventario(db.Model):
    __tablename__ = 'categoria_inventario'
    id_categoria_inventario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False, unique=True)

    def __init__(self, nombre):
        self.nombre = nombre


class CategoriaProducto(db.Model):
    __tablename__ = 'categoria_producto'
    id_categoria_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False, unique=True)

    def __init__(self, nombre):
        self.nombre = nombre


class Inventario(db.Model):
    __tablename__ = 'inventario'
    id_inventario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False, unique=True)
    precio_adquisicion = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    id_categoria_inventario = db.Column(db.Integer, db.ForeignKey('categoria_inventario.id_categoria_inventario'),
                                        nullable=False)

    def __init__(self, nombre, precio_adquisicion, cantidad, id_categoria_inventario):
        self.nombre = nombre
        self.precio_adquisicion = precio_adquisicion
        self.cantidad = cantidad
        self.id_categoria_inventario = id_categoria_inventario


class Producto(db.Model):
    __tablename__ = 'producto'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False, unique=True)
    descripcion = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    disponible = db.Column(db.Boolean, nullable=False)
    id_categoria_producto = db.Column(db.Integer, db.ForeignKey('categoria_producto.id_categoria_producto'),
                                      nullable=False)

    def __init__(self, nombre, descripcion, precio, disponible, id_categoria_producto):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.disponible = disponible
        self.id_categoria_producto = id_categoria_producto


class ProductoUtilizaInventario(db.Model):
    __tablename__ = 'producto_utiliza_inventario'
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id_producto'), primary_key=True)
    id_inventario = db.Column(db.Integer, db.ForeignKey('inventario.id_inventario'), primary_key=True)

    def __init__(self, id_producto, id_inventario):
        self.id_producto = id_producto
        self.id_inventario = id_inventario


class Itinerario(db.Model):
    __tablename__ = 'itinerario'
    id_itinerario = db.Column(db.Integer, primary_key=True)
    id_inventario = db.Column(db.Integer, db.ForeignKey('inventario.id_inventario'), nullable=False)
    id_vendedor = db.Column(db.Integer, db.ForeignKey('vendedor.id_vendedor'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_total = db.Column(db.Float, nullable=False)
    fecha_entrega = db.Column(db.Date, nullable=False)

    def __init__(self, id_inventario, id_vendedor, cantidad, precio_total, fecha_entrega):
        self.id_inventario = id_inventario
        self.id_vendedor = id_vendedor
        self.cantidad = cantidad
        self.precio_total = precio_total
        self.fecha_entrega = fecha_entrega


class Orden(db.Model):
    __tablename__ = 'orden'
    id_orden = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    estatus = db.Column(db.String(20), nullable=False)  # Change the data type to String
    fecha = db.Column(db.Date, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __init__(self, id_usuario, estatus, fecha, total):
        self.id_usuario = id_usuario
        self.estatus = estatus
        self.fecha = fecha
        self.total = total
        

class VendedorAtenderOrden(db.Model):
    __tablename__ = 'vendedor_atender_orden'
    id_vendedor = db.Column(db.Integer, db.ForeignKey('vendedor.id_vendedor'), primary_key=True)
    id_orden = db.Column(db.Integer, db.ForeignKey('orden.id_orden'), primary_key=True)

    def __init__(self, id_vendedor, id_orden):
        self.id_vendedor = id_vendedor
        self.id_orden = id_orden


class ProductoOrden(db.Model):
    __tablename__ = 'producto_orden'
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id_producto'), primary_key=True)
    id_orden = db.Column(db.Integer, db.ForeignKey('orden.id_orden'), primary_key=True)

    def __init__(self, id_producto, id_orden):
        self.id_producto = id_producto
        self.id_orden = id_orden


class ReporteVentas(db.Model):
    __tablename__ = 'reporte_ventas'
    id_reporte_ventas = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __init__(self, fecha_inicio, fecha_fin, total):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.total = total



class ProductosEnReporte(db.Model):
    __tablename__ = 'productos_en_reporte'
    id_reporte_ventas = db.Column(db.Integer, db.ForeignKey('reporte_ventas.id_reporte_ventas'), primary_key=True)
    id_orden = db.Column(db.Integer, db.ForeignKey('orden.id_orden'), primary_key=True)

    def __init__(self, id_reporte_ventas, id_orden):
        self.id_reporte_ventas = id_reporte_ventas
        self.id_orden = id_orden
