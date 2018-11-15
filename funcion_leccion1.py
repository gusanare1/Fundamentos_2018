'''
superheroe = ["S1:: H1, H2, H3" , "S2:: H4, H2, H1"]
sh=[]
for superh in superheroe:
	superheroe_puntuado = superh.replace("H1","H1+1").replace("H2","H2+2").replace("H3","H3+0.3").replace("H4","H4+0.1")
	sh.append(superheroe_puntuado)
'''
superheroe=[]
sh=[]
#1
def bono(habilidad):
	superheroe_puntuado = ''.join(sh)
	k=superheroe_puntuado.find(habilidad)
	l=len(habilidad)+k
	m=superheroe_puntuado.find(',',l)
	return superheroe_puntuado[l:m]
#print(bono('H1'))
#2
def listaHabilidades(nombre_superheroe):
	lista=[]
	for hero in superheroe:
		if nombre_superheroe in hero:
			return hero.replace(nombre_superheroe,"").replace("::","").split(",")
	return lista
#print(listaHabilidades('S2'))
#3
def sumaHabilidades(nombre_superheroe):
	sum=0
	for super in sh:
		if nombre_superheroe in super:
			habilidades = super.replace(nombre_superheroe,"").replace("::","")
			listaHabilidades = habilidades.split(",")
			for habilidad in listaHabilidades:
				k=habilidad.find("+")
				l = habilidad[k+1:]
				sum = sum + float(l)
	return sum
#print(sumaHabilidades('S1'))
#4
def caracteristicas_superheroes(super1, super2):
	print("Primer superheroe: "+super1)
	print(listaHabilidades(super1))
	print("Segundo Superheroe: "+super2)
	print(listaHabilidades(super2))
	print("Quien Gana?")
	bono1=sumaHabilidades(super1)
	bono2=sumaHabilidades(super2)
	print("Nombre1: "+str(bono1)+" Nombre2: "+str(bono2))
	if bono1>bono2:
		print("Gana 1: "+str(super1))
	else:
		print("Gana 2 "+str(super2))
#caracteristicas_superheroes('S1','S2')
#5
def menorBono():
	lis_pun=[]
	lis_nom_sup=[]
	for sup in superheroe:
		lis_nom_sup.append(sup.split("::")[0])
	for nom_sup in lis_nom_sup:
		lis_pun.append(str(sumaHabilidades(nom_sup))+" "+nom_sup)
	lis_pun.sort()#De menor a mayor
	menorBono = lis_pun[0].split(" ")[0]
	print("SuperHeroes con el menor bono")
	for i in lis_pun:
		if menorBono in i:
			print("*. "+i.split(' ')[1])
#menorBono()
#6
def muestreTodosSuperHueroesEnLista(list):
	lis_pun=[]
	lis_nom_sup=[]
	for sup in superheroe:
		lis_nom_sup.append(sup.split("::")[0])
	for nom_sup in lis_nom_sup:
		lis_pun.append(str(sumaHabilidades(nom_sup))+" "+nom_sup)
	lis_pun.sort()#De menor a mayor
	for i in lis_pun:
		for j in list:
			if j in i:
				print(i)
#muestreTodosSuperHueroesEnLista(['S2'])
