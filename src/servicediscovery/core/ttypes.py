#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class ServiceInfo:
  """
  Attributes:
   - server_name
   - server_url
   - expire_s
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'server_name', None, None, ), # 1
    (2, TType.STRING, 'server_url', None, None, ), # 2
    (3, TType.I32, 'expire_s', None, None, ), # 3
  )

  def __init__(self, server_name=None, server_url=None, expire_s=None,):
    self.server_name = server_name
    self.server_url = server_url
    self.expire_s = expire_s

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.server_name = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.server_url = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.expire_s = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ServiceInfo')
    if self.server_name is not None:
      oprot.writeFieldBegin('server_name', TType.STRING, 1)
      oprot.writeString(self.server_name)
      oprot.writeFieldEnd()
    if self.server_url is not None:
      oprot.writeFieldBegin('server_url', TType.STRING, 2)
      oprot.writeString(self.server_url)
      oprot.writeFieldEnd()
    if self.expire_s is not None:
      oprot.writeFieldBegin('expire_s', TType.I32, 3)
      oprot.writeI32(self.expire_s)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.server_name is None:
      raise TProtocol.TProtocolException(message='Required field server_name is unset!')
    if self.server_url is None:
      raise TProtocol.TProtocolException(message='Required field server_url is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.server_name)
    value = (value * 31) ^ hash(self.server_url)
    value = (value * 31) ^ hash(self.expire_s)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)