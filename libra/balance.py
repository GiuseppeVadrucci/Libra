#Class balance define all the features of the balancer
#the goal would be to add as much as possible

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
                          
     #add te list of redirects to wich balance the requests
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

 
 
     	            
          
#functionality
     def setProxy(self):
          self._proxy = True
     	  

#     def addHeader(list=[]):
#       	  if self._proxy == true:
       	     #implement
#       	  else:
             #raiseerror
     	
#Here the types of redirections ( e.g. round robin, based on weight )

     def setWeight(self,weight):
       	  self._weight = weight #after 5 requests change the server
 
#def round robin(self):

#def statefull(self): 

  
  
