#This is an example of usage

import balance

redirects=['site1.example.com','site2.example.it']

libra = balance.Balance()
libra.add(redirects)
libra.setWeight(5)
libra.listen('127.0.0.1',3000)
libra.thread()   
