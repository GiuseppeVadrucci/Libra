#This is an example of usage

import balance

redirects=['','']

libra = balance.Balance()
libra.add(redirects)
libra.setWeight(5)
libra.listen('127.0.0.1',3000)
libra.thread()   
