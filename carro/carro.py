class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            #si no hay carro, lo crea vacio
            carro = self.session["carro"] = {}
        #else:
            #si hay carro, mantiene los items ya almacenados del carro que ya habia
        self.carro = carro

    def agregar(self, producto):
        #si no encuentra el ID del producto en las claves del diccionario (el carro es un diccionario con claves y valores)
        if(str(producto.id) not in self.carro.keys()):
            #pues lo añade al carro
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
            # la imagen no es serializable en un JSON, daria fallo
            #   "imagen": producto.imagen
            }
        #si ya esta el articulo en el carro, aumentamos la cantidad en 1
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break

        self.guardar_carro()

    def guardar_carro(self):
        #el carro debe ser el mismo de la sesion y indicamos que se ha modificado la Sesion
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key == str(producto.id):
                    #si solo habia 1 item de ese producto, elimina el producto del carro
                    value["cantidad"] = value["cantidad"] - 1
                    value["precio"] = float(value["precio"]) - producto.precio
                    if value["cantidad"] < 1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        #el carro (diccionario) lo pasa a vacio
        self.session["carro"] = {}
        self.session.modified = True
