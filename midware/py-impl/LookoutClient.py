#!/usr/bin/python

import sys
sys.path.append('../gen-py')

from watchtower import ImageUpload
from watchtower.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
  transport = TSocket.TSocket('localhost', 8080)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = ImageUpload.Client(protocol)

  transport.open()

  res = client.Upload('bleah')
  print res
  transport.close()

except Thrift.TException, tx:
  print '%s' % (tx.message)
