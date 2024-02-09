
class Alumno():
    def __init__(self,matricula,nombre,apellido,edad,):
        self.matricula=matricula
        self.nombre=nombre
        self.apellido=apellido
        self.calificacion=[]
        self.edad=edad
        
        pass

    
    def setCalificacion(self,calificacion):
        self.calificacion.append(calificacion)
        return calificacion

    def getProm(self,prom):
        try:
            getProm = sum(self.calificacion) / len(self.calificacion)
        except Exception as e:
            print (f"error desconocido: {e}")
        return getProm  
            
    
    def __str__(self):
        return f"matricula: {self.matricula} | nombre: {self.nombre} {self.apellido} | calificación: {self.calificacion}"
#fin clase alumno-----------------------------------------------------------------------------------------------------------------------------
      
class gradAlumno(Alumno):
    def __init__(self,matricula,nombre,apellido,edad,graduacion,fecha,tesis):
        super().__init__(matricula,nombre,apellido,edad)
        self.graduacion= graduacion
        self.fecha = fecha
        self.tesis = tesis
        pass
    def getGrad(self):
        getProm = self.promedio()
        if getProm <=6:
            print("\033[31m"+ str(getProm) + "\033[0m")
        else:
            print(getProm)
