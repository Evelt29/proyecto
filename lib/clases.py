
class Alumno():
    def __init__(self,matricula,nombre,apellido,edad):
        self.matricula=matricula
        self.nombre=nombre
        self.apellido=apellido
        self.calificacion=[]
        self.edad=edad
        pass
    def __str__(self):
        return f"nombre:{self.nombre} | apellido:{self.apellido} | matricula:{self.matricula} | edad:{self.edad} | calificación:{self.calificacion}"
    def setCalificacion(self,calificacion):
        self.calificacion.append(calificacion)
        return calificacion
    def getProm(self):
        getProm = sum(self.calificacion) / len(self.calificacion)
        return getProm
    
class gradAlumno(Alumno):
    def __init__(self,matricula,nombre,apellido,edad,graduacion,fecha,tesis):
        super().__init__(matricula,nombre,apellido,edad)
        self.graduacion= graduacion
        self.fecha = fecha
        self.tesis = tesis

        