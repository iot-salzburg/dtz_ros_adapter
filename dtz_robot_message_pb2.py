# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dtz_robot_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dtz_robot_message.proto',
  package='prototest',
  serialized_pb=_b('\n\x17\x64tz_robot_message.proto\x12\tprototest\"6\n\x0cRobotMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05state\x18\x02 \x02(\t\x12\x0b\n\x03opt\x18\x03 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ROBOTMESSAGE = _descriptor.Descriptor(
  name='RobotMessage',
  full_name='prototest.RobotMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='prototest.RobotMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='prototest.RobotMessage.state', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opt', full_name='prototest.RobotMessage.opt', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['RobotMessage'] = _ROBOTMESSAGE

RobotMessage = _reflection.GeneratedProtocolMessageType('RobotMessage', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTMESSAGE,
  __module__ = 'dtz_robot_message_pb2'
  # @@protoc_insertion_point(class_scope:prototest.RobotMessage)
  ))
_sym_db.RegisterMessage(RobotMessage)


# @@protoc_insertion_point(module_scope)
