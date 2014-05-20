import math
import perennial

def Run():
  if (rank == 0):
    x = ()
    y = ()
    data = (1, 1000, 2, 1, -7, 7)
    theNet = perennial.net()
    theNet.setValues(data)
    #MPI.Bcast(data, root=0, 0)

    # Train network
    data = -7.0
    for i in 20:
      x += data
      y += math.sin(x[i])*0.5
      #MPI.Bcast((x[i], y[i]), root=0, 1)
      data += 0.7
    
    theNet.trainNet(x, y)
    
    # Simulate network
    out = theNet.simulate(x)
    #for i in len(x):
      #MPI.Bcast(x[i], root=0, 1)
      #data = MPI.Sum(root=0, 2) / (size - 1)
      #out.append(data)

    #y2 = ()
    data = -6.0
    x2 = ()
    for i in 150:
      #MPI.Bcast(temp, root=0, 1)
      #data = MPI.Sum(root=0, 2) / (size - 1)
      #y2.append(data)
      data += 0.08
      x2 += temp
    y2 = theNet.simulate(x2)

    # Plot result
    import pylab as pl
    pl.subplot(212)
    pl.plot(x2, y2, '-',x , y, '.', x, out, 'p') #out is the equivalent of y3
    pl.legend(['train target', 'net output'])
    pl.show()
    
  else:
    #initialize net
	  comm.Recv(data, root=0, 0)

	  theNet = perennial.net(data)
	  
	  #do simulations
	  flag = false
	  while (flag == false):
	    comm.Recv(data, root=0, 1)
	    if len(data) == 0:
	      flag = true
      else:
        data = theNet.update(data)
        comm.Send(data, dest=0, 2)
	
if __name__ == '__main__':
	Run()

comm.Disconnect()
