#Main file, defininf Libra, socket select server to accept requests 
#it should be optimized

import select, queue, math
import socket, sys, random, client
import threading, reques
import time


counter = 1
weight = 0
class Libra:
  def __init__(self):
   self._redirects = []
   self.outputs = []
   self.message_queues = {}
   self.inputs = []
   self._weight = 5

  def listen(self,address,port):
   self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
   self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   self.server.setblocking(0)
   self.server.bind((address, port))
   self.server.listen(5)
   self.inputs = [self.server]
   print('\n\n')
   print(' Server listening on: '+address+':'+str(port))
   time.sleep(1)
   print('\n')


  def start(self):
   global counter
   global weight 
   n = 0
   weight = self._weight  
   if len(self._redirects) > 0:
    print('\n')
    print(' Libra started waiting for requests...')
    print('\n')
    while self.inputs:
      readable, writable, exceptional = select.select(self.inputs, self.outputs, self.message_queues)
      for s in readable:
        if s is self.server:
            self.connection, client_address = s.accept()
            self.connection.setblocking(0)
            self.inputs.append(self.connection)
            self.message_queues[self.connection] = queue.Queue()
        else:
            data = str(s.recv(1024))
            if data:
                self.message_queues[s].put(data)
                if s not in self.outputs:
                    self.outputs.append(s)
            else:
                if s in self.outputs:
                    self.outputs.remove(s)
                self.inputs.remove(s)
                s.close()
                del self.message_queues[s]


      for s in writable:
        try:
            next_msg = self.message_queues[s].get_nowait()
            print(' Request from: '+ str(client_address))
        except queue.Empty:
            self.outputs.remove(s)
        if next_msg != '':
            if len(self._redirects) > 0:
             for el in self._redirects:
               try:
                  client.connect(socket.gethostbyname(el))
               except SystemExit:
                  self._redirects.remove(el)
             if len(self._redirects) > 0:
              if(reques.http(next_msg)):
                 test = math.inf
                 if(counter > weight):
                    try:
                       self._redirects[n+1]
                       n += 1
                       
                       weight = self._weight + weight
                       
                    except IndexError:
                       n = 0
                       counter = 1
                       weight = self._weight
                 r = 'HTTP/1.1 301 Moved Permanently\r\nServer: Libra\r\nRetry-After: 1\r\nLocation: https://'+str(self._redirects[n])+'\r\n'
                 counter += 1
                 print(' Redirected to: '+str(self._redirects[n]))
                 s.send(str.encode(r))
                 if s in self.outputs:
                   self.outputs.remove(s)
                 self.inputs.remove(s)
                 s.close()
                 del self.message_queues[s]
             else:
              print(' No servers aviable, change redirects list.')

      for s in exceptional:
        self.inputs.remove(s)
        if s in self.outputs:
            self.outputs.remove(s)
        s.close()
        del self.message_queues[s]

   else:
    print(' No redirects list, use add method.')
    self.server.close()
    print(' Server closed.\n')
    sys.exit(0)



  def thread(self):
    for i in range(10):
       t = threading.Thread(target=self.start())
       t.start()


     
