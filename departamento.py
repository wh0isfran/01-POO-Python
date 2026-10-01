class Departamento:
    def __init__(self, id_departamento:int, nombre:str, piso:int):
            self.id_departamento = id_departamento
            self.nombre=nombre
            self.piso=piso

    @property
    def id_departamento(self)-> int:
        return self._id_departamento

    @id_departamento.setter
    def id_departamento(self,id_departamento:int)-> None:
        if not isinstance(id_departamento, int):
            raise ValueError("El ID debe ser mayor a 1.")
        self._id_departamento = id_departamento

    @property
    def nombre(self)-> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre:str)-> None:
        if not isinstance(nombre,str) or len(nombre.strip()) < 2:
            raise ValueError("El nombre no puede tener menos de 2 caracteres.")
        self._nombre = nombre.strip().upper()

    @property
    def piso(self)-> int:
        return self._piso
    
    @piso.setter
    def piso(self,piso:int)-> None:
        if not isinstance(piso, int):
            raise TypeError("El piso debe ser un número entero.")
        if piso < 0 or piso > 10:
            raise ValueError("El número de piso debe corresponder a los números de los pisos dentro del edificio.")
        self._piso = piso

    def __str__(self)-> str:
        return f"Información del departamento:\nID_Departamento: {self.id_departamento}\nNombre: {self.nombre}\nPiso: {self.piso}"

    def __repr__(self)-> str:
        return f"Departamento(id_departamento='{self.id_departamento}', nombre='{self.nombre}', piso='{self.piso}')"
         