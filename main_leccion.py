import funcion_leccion1 as l

superheroe = ["S1:: H1, H2, H3" , "S2:: H4, H2, H1"]
sh=[]

for superh in superheroe:
	superheroe_puntuado = superh.replace("H1","H1+1").replace("H2","H2+2").replace("H3","H3+0.3").replace("H4","H4+0.1")
	sh.append(superheroe_puntuado)

l.superheroe = superheroe
l.sh = sh
print(l.bono('H1'))
print(l.listaHabilidades('S2'))
print(l.sumaHabilidades('S1'))
print(l.caracteristicas_superheroes('S1','S2'))
l.menorBono()
l.muestreTodosSuperHueroesEnLista(['S2'])
