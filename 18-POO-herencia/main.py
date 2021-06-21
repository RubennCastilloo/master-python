import clases

persona = clases.Persona()
persona.setNombre("Ruben")
persona.setApellidos("Castillo")
persona.setAltura("174cm")
persona.setEdad("25 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("--------------------------")

informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellidos("Negro")

print(f"El informático es {informatico.getNombre()} {informatico.getApellidos()}")
print("Lenguajes de programación: ", informatico.getLenguajes())
print(informatico.caminar())

print("--------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Ruben")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())
