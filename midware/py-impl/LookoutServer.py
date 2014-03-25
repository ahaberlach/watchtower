#!/usr/bin/python

import sys
sys.path.append('../gen-py')

from watchtower import ImageUpload
from watchtower.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import socket

class ImageUploadHandler(object):
  def __init__(self):
    self.log = {}

  def Upload(self, msg):
    print "Upload!"
    print msg
    return True

handler = ImageUploadHandler()
processor = ImageUpload.Processor(handler)
transport = TSocket.TServerSocket(port=8080)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
print "Starting python server"
server.serve()
print "done!"
