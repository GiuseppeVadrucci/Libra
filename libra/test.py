#This is an example of usage

import balance

redirects=['','']

libra = balance.Balance()
libra.add(redirects)
libra.setWeight(5)
libra.listen('159.65.21.180',3000)
libra.thread()   
