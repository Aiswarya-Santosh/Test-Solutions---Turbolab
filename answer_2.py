def find(list, n) :
  #first
	sumfi = [0] * n
	sumfi[0] = list[0]
	for i in range(1, n) :
		sumfi[i] = sumfi[i - 1] + list[i]
  #last
	sumla = [0] * n
	sumla[n - 1] = list[n - 1]
	for i in range(n - 2, -1, -1) :
		sumla[i] = sumla[i + 1] + list[i]

	# done sides
  # check same
	for i in range(1, n - 1, 1) :
		if sumfi[i] == sumla[i] :
			return i+1
		


list = [ 1,2,3,10,6]
n = len(list)
print(find(list, n))