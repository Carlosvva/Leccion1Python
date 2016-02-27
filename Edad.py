#!/usr/bien/env python
# -*- coding: utf-8 -*-
Nombre = raw_input("Ingrese Nombre De Usuario")
Actualidad = input("ingrese año acutual")
Nacimiento = input("Ingrese Año de Nacimiento")
Edad = Actualidad - Nacimiento
print Nombre + "Su Edad es de : " + str(Edad)
if Edad <= 12:
 	print "Nino"
else:
 	print "Joven"