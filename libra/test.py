import balance

redirects=['giuseppevadrucci.eu','lexanalyzer.eu']

libra = balance.Balance()
libra.add(redirects)
libra.setWeight(5)
libra.listen('159.65.21.180',3000)
libra.thread()   
