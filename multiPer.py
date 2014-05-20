def createNet_gen(self, lay):
  layer = lay
	def createNet(self, nn, nl, ni, minN, maxN):
		if nl>0:
			# create the first layer
			layers = [layer(nn, ni, minN, maxN)]

			# create hidden layers
			for _ in range(0, nl):
				layers += layer(nn, ni, minN, maxN)

			# hidden-to-output layer
			layers += [layer(nn, ni, minN, maxN)]
		else:
			# If we don't require hidden layers
			layers = [layer(nn, ni, minN, maxN)]
			
		return layers
	return createNet
		

def gerWeights_gen(self, lays):
  layers = lays
	#get weights from net
	def getWeights(self):
		out = []
		for lay in layers:
			for neu in layers.neurons:
				amount += neu.weights
		return out
		
	return getWeights

def getNumWeights_gen(self, lays):
  layers = lays
	#get total number of weights
	def getNumWeights(self):
		amount = 0
		for lay in layers:
			for neu in layers.neurons:
				amount += neu.numInputs + 1
		return amount
	
	return getNumWeights
		

def putWeights_gen(self, lays, nW):
  numWeights = nW
  layers = lays
	#replace weights
	def putWeights(self, theWeights):
		assert len(theWeights) == numWeights, "Incorrect amount of weights."
		end = 0
		for lay in layers:
			for neu in layers.neurons:
				begin, end = begin, end + (neu.numInputs + 1)
				neu.set_weights(weights[start:stop])
		return self
		

def updateNet_gen(self, lays, bias, NI):
  layers = lays
  numInputs = NI
	#calculate output
	def updateNet(self, inputs, response = 1):
		assert len(inputs) == numInputs, "Incorrect amount of inputs."

		for layer in layers:
			outputs = []
			for neuron in layers.neurons:
		      tot = neuron.sum(inputs) + neuron.weights[-1] * bias
		      
		      #sigmoid response curve
		      try:
		        tot = (1 / (1 + math.exp(-tot / response))) #tot is the activation value
		      except OverFlowError:
		        tot = float("inf")
		        
					outputs.append(tot)
					inputs = outputs
		return outputs
			
	
	return updateNet
			
def trainNet_gen(self, lays, UD, NI):
  layers = lays
  updateNet = UD
  numInputs = NI
  def trainNet(self, inputs, expected):
    assert (len(inputs) % numInputs == 0), "Incorrect amount of inputs."
    
    error = [updateNet(?????)]######################################################################
    count = numInputs
    while(count < len(inputs)):
      ##############################################################################################
      count += numInputs
    
    return error
    
def simNet_gen(self, lays, UD, NI):
  layers = lays
  updateNet = UD
  numInputs = NI
  def simNet(self, inputs):
    assert (len(inputs) % numInputs == 0), "Incorrect amount of inputs."
    
    out = [updateNet(?????)]######################################################################
    count = numInputs
    while(count < len(inputs)):
      ##############################################################################################
      count += numInputs
    
    return out
    
def str_gen(self, lays):
  layers = lays
	def stringer(self):
		return '\n'.join([str(i +	1) + ' ' + str(layer) for i, layer in enumerate(layers)])
	return stringer
	
