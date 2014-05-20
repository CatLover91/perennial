def layer_gen(self, neu):
  neuron = neu
  class layer:
	  neurons = []
	
	  def __init__(self, numInput, numNeurons, minNum, maxNum):
		  self.numNeurons = numNeurons
		  self.neurons = [neuron(numInput, minNum, maxNum) for _ in range(0, self.numNeurons)]
	
	  def __str__(self):
		  return 'Layer:\n\t'+'\n\t'.join([str(neuron) for neuron in self.neurons])+''
	
	return layer