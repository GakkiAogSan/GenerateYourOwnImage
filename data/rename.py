#-*- coding: UTF-8 -*-
#@ 2017-3-5 
#@ JX

import os
filenames = os.listdir('./faces/')#
for name in filenames:
  print(name)
for num in range(0,len(filenames)):
    os.rename('./faces/'+filenames[num],str(num)+'.jpg')
