#---------------------------------->
#---------------------------------->
#Ciencias de la computacion - Facultad de Ingenieria - Universidad Nacional de Cuyo
#diego.xmen123@gmail.com
#Diego Rinaldo Cazon Condori
#---------------------------------->
#---------------------------------->

class Linkedlist:
  head=None
class Node:
  value=None
  nextNode=None
#------------------------------
#------------------------------

def Ver_Lista(L):
	currentnode = L.head
	print('--------------->>')
	print('Lista: ')
	while currentnode != None:
		print(currentnode.value,' ->',end=' ')
		currentnode = currentnode.nextNode
	print('')
	print('--------------->>')


def add(L,element):
  Node1=Node()
  Node1.value=element
  Node1.nextNode=L.head
  L.head=Node1
#------------------------------
def search(L,element): #Retorna None si el elemento no se encuentra sino retorna contador
  currentnode = L.head
  contador = 0
  while currentnode != None and currentnode.value != element:
      contador += 1
      currentnode = currentnode.nextNode

  if currentnode!= None:
  	return contador


#------------------------------
def length(L):
    contador = 0
    currentnode=L.head
    while currentnode!=None:
      
      contador += 1
      currentnode=currentnode.nextNode
      
    return(contador)
#------------------------------
def delete(L,element):
  currentnode = L.head
  if currentnode.value == element:
      L.head = currentnode.nextNode
  else:
      while currentnode.nextNode != None:
          if currentnode.nextNode.value == element:
              break
          currentnode = currentnode.nextNode
      if currentnode != None:
          currentnode.nextNode = currentnode.nextNode.nextNode
          return(True)
      else:
          return(False)

def update(L,element,position):
  if length(L)>=position and position>=0 :
    Lcopia=L.head
    for x in range(0,position):
      Lcopia=Lcopia.nextNode
    Lcopia.value=element
    return(position)

def insert(L , element , position):
	if L.head == None or position == 0:
		add(L,element)
		return 0

	currentnode = L.head
	contador = 0
	while currentnode.nextNode != None and contador != position-1:
		contador += 1
		currentnode = currentnode.nextNode

	Node1=Node()
	Node1.value=element
	Node1.nextNode= currentnode.nextNode
	currentnode.nextNode = Node1

	return(contador)

def access(L,position):
	if L.head != None:
	    Longitud=length(L)
	    if Longitud > position and position >= 0:
	    	currentnode = L.head
	    	contador = 0
	    	while currentnode != None and position != contador:
	    		contador += 1
	    		currentnode = currentnode.nextNode
	    	return(currentnode.value)

def deletePosicion(L,posicion):#La primera posicion es el cero
	long_list =  length(L)
	
	if L.head != None and long_list>posicion and posicion>=0:
		 	
	    currentnode = L.head
	    if posicion == 0:
	    	L.head = L.head.nextNode
	    	return(currentnode.value)
	   
	    for i in range(posicion):
	    	if i != 0:
	    		currentnode = currentnode.nextNode
	    valor_Retorno = currentnode.nextNode.value
	    currentnode.nextNode = currentnode.nextNode.nextNode
	    return(valor_Retorno)

