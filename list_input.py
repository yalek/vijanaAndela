def list_input(n):
	lista = []
	listb = []
	counter=1
	while counter<=n:
		user_input= raw_input("Enter a number")
		lista.append(int(user_input))
		counter+=1
	print lista
	#return lista
	#for number in lista:
	i=0
	while i<len(lista):
		if lista[i]%2==0:
			break
		else:
			listb.append(lista[i])
			i+=1
	print listb
list_input(4)