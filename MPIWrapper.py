


class wrap:
  def __init__(self, c, r, s):
    self.comm = c
    self.rank = r
    self.size = s
    
  def getNumWeights(self, f):
    def newf(self):
      if(rank != 0):
        data = f()
        MPI.send(data, dest=0, tag=23)
      else
        comm.Reduce(None, data, op=MPI.SUM, root=0)
        return data
  
  def getWeights(self, f):
    def newf(self):
      if(rank != 0):
        data = f()
        MPI.send(data, dest=0, tag=23)
      else
        comm.Gatherv(data)
        return data
  
  def simulateNet(self, f):
    
  
  def trainNet(self, f):
