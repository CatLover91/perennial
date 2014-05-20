def neuron_gen(self):
  class neuron:
	  weights = []
	  def __init__(self, numInputs, minNum, maxNum):
		  self.numInputs = numInputs
		  self.set_weights([random.uniform(minNum,maxNum) for x in range(0,numInputs+1)]) # +1 for bias weight
		
	  def sum(self, inputs):
		  # Does not include the bias
		  return sum(val * self.weights[i] for i, val in enumerate(inputs))

	  def set_weights(self, weights ):
		  self.weights = weights
						
	  def __str__(self):
		  return 'Weights: %s, Bias: %s' % (str(self.weights[:-1]),str(self.weights[-1]))
		  
	return neuron
