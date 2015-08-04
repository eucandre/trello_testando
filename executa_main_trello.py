from main_trello import *


Testa_Conecta = Manipula_Trello()

key = u'9cd60a9e9eab461420670948ad742fbb'
auth = u'e595b1844450a51fd0ce615d7a295fe5cb669ba104aaf2dbb010d1d27d626283'



#print Testa_Conecta.Conecta_Usuario_id(key, auth)
print Testa_Conecta.listas(Testa_Conecta.Conecta_Usuario_id(key, auth))
#print Testa_Conecta.Seleciona__Boards_Pessoa(Testa_Conecta.Conecta_Usuario_id(key,auth))
#print Testa_Conecta.testaLazy(Testa_Conecta.Conecta_Usuario_id(key, auth))