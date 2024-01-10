import json  # Import the 'json' module to use JSON-related functions

class Cumple:
    
    def __init__(self, data):
        self.datos = json.loads(data)
        self.AllValues = []

    def buscar_cumple(self, diccionario, clave_padre=""):        
        for clave, subdiccionario in diccionario.items():
            if isinstance(subdiccionario, dict):
                if "cumple" in subdiccionario and subdiccionario["cumple"] == True:                    
                    self.AllValues.append(True)
                if "cumple" in subdiccionario and subdiccionario["cumple"] == False:
                    self.AllValues.append(False)
                self.buscar_cumple(subdiccionario, f"{clave_padre}.{clave}")


    def BuscarFalse(self):
        for indice, valor in enumerate(self.AllValues):
            if valor is False:                
                return False
        
        return True
                

    def buscar_cumple_principal(self):
        
        for clave, valor in self.datos.items():
            if clave == "cumple" and valor == True:
                self.AllValues.append(True)                
            if clave == "cumple" and valor == False:
                self.AllValues.append(False)            
        
                 