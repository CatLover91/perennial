from multiprocessing import cpu_count
import math
import random

class net:
	__multiProcessEnabled = False
	__MPIEnabled = False
	BIAS = -1
	
	def setValues(numInput=0, numNeuron=0, numLayer=0, numOutput=0, mnNum=0, mxNum=0):
		self.numInputs = numInput
		self.numOutputs = numOutput
		self.numLayers = numLayer
		self.numNeurons = numNeuron
		self.minNum = mnNum
		self.maxNum = mxNum
		
		if((MPIEnabled == False) or (rank != 0)):
		  self.layers = self._createNet(numNeurons, numLayers, numInputs, minNum, maxNum)

		getNumWeights = per.getNumWeights_gen(layers)
		numWeights = getNumWeights()
		
		getWeights = per.getWights_gen(layers)
		putWeights = per.putWeights_gen(layers)
		#updateNet = per.updateNet_gen(layers, BIAS, numInputs)
		trainNet = per.trainNet_gen(updateNet, layers, updateNet, numInputs)
		simNet = per.semNet_gen(updateNet, layers, updateNet, numInputs)
		__str__ = per.str_gen(layers)
		
	def __init__(self):
	  try:
	    import mpi4py as MPI
	    import MPIWrapper
	    __MPIEnabled = True
	    self.comm = MPI.COMM_WORLD()
	    self.rank = comm.Get_rank()
	    self.size = comm.Get_size()
	    wrap = MPIWrapper.wrap(comm, rank, size) #may not be needed, just being careful with scope
	  except: ###########################################
	    ###################################################
	  try:
	    import multiprocessing
	    temp = multiprocessing.cpu_count()
	    if(temp > 1):
	      __multiProcessEnabled = True
	      __processCount = temp
	      import multiPer as per
	      import MPlayer as lay
	      import MPneuron as neu
	    else:
	      import singlePer as per
	      import layer as lay
	      import neuron as neu
	  except NotImplementedError:
	    __multiProcessEnabled = False
	    import singlePer as per
		  
		neuron = neu.neuron_gen()
		layer = lay.layer_gen(neuron)
		_createNet = per.createNet_gen(layer)