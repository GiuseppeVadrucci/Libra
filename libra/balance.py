import sys, os, socket, time
import libra

global config 
#open(configfile,"r")


class Balance(libra.Libra):

     def __init__(self):
          super().__init__()
          self._weight = 5
          self._random = False
          self._proxy = False
                          
     
     def add(self, redirects = []):
          for el in redirects:
           try:
            socket.gethostbyname(el)
            self._redirects.append(el)
           except socket.gaierror:
            print(' '+str(el)+' is not a valid hostname.\n')
            if(len(self._redirects)) > 0:
             self._redirects.remove(el)
           time.sleep(1)

          if(len(self._redirects) > 0):
           print('\n List of servers successfully updated.')
           print('\n')
           print(' Waiting for the balancer...')
           time.sleep(1)
          else:
           print(' No redirects list.')
           self.server.close()
           sys.exit(0)

     def setProxy(self):
          self._proxy = True
     	  

#     def addHeader(list=[]):
#       	  if self._proxy == true:
       	     #implement
#       	  else:
             #raiseerror
     	

     def setWeight(self,weight):
       	  self._weight = weight
 

  
  
