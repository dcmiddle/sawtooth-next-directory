# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_transaction.proto

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
  name='user_transaction.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x16user_transaction.proto\"z\n\x18ProposeUpdateUserManager\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x16\n\x0enew_manager_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x10\n\x08metadata\x18\x05 \x01(\t\"d\n\x18\x43onfirmUpdateUserManager\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x12\n\nmanager_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"c\n\x17RejectUpdateUserManager\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x12\n\nmanager_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"d\n\nCreateUser\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x12\n\nmanager_id\x18\x04 \x01(\t\x12\x10\n\x08metadata\x18\x05 \x01(\t\"b\n\nUpdateUser\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08new_name\x18\x02 \x01(\t\x12\x1b\n\x13old_metadata_sha512\x18\x03 \x01(\t\x12\x14\n\x0cnew_metadata\x18\x04 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROPOSEUPDATEUSERMANAGER = _descriptor.Descriptor(
  name='ProposeUpdateUserManager',
  full_name='ProposeUpdateUserManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ProposeUpdateUserManager.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ProposeUpdateUserManager.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_manager_id', full_name='ProposeUpdateUserManager.new_manager_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ProposeUpdateUserManager.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ProposeUpdateUserManager.metadata', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=148,
)


_CONFIRMUPDATEUSERMANAGER = _descriptor.Descriptor(
  name='ConfirmUpdateUserManager',
  full_name='ConfirmUpdateUserManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ConfirmUpdateUserManager.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ConfirmUpdateUserManager.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manager_id', full_name='ConfirmUpdateUserManager.manager_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ConfirmUpdateUserManager.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=250,
)


_REJECTUPDATEUSERMANAGER = _descriptor.Descriptor(
  name='RejectUpdateUserManager',
  full_name='RejectUpdateUserManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='RejectUpdateUserManager.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='RejectUpdateUserManager.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manager_id', full_name='RejectUpdateUserManager.manager_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='RejectUpdateUserManager.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=351,
)


_CREATEUSER = _descriptor.Descriptor(
  name='CreateUser',
  full_name='CreateUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateUser.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='CreateUser.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='CreateUser.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manager_id', full_name='CreateUser.manager_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='CreateUser.metadata', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=453,
)


_UPDATEUSER = _descriptor.Descriptor(
  name='UpdateUser',
  full_name='UpdateUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='UpdateUser.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_name', full_name='UpdateUser.new_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='old_metadata_sha512', full_name='UpdateUser.old_metadata_sha512', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_metadata', full_name='UpdateUser.new_metadata', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=455,
  serialized_end=553,
)

DESCRIPTOR.message_types_by_name['ProposeUpdateUserManager'] = _PROPOSEUPDATEUSERMANAGER
DESCRIPTOR.message_types_by_name['ConfirmUpdateUserManager'] = _CONFIRMUPDATEUSERMANAGER
DESCRIPTOR.message_types_by_name['RejectUpdateUserManager'] = _REJECTUPDATEUSERMANAGER
DESCRIPTOR.message_types_by_name['CreateUser'] = _CREATEUSER
DESCRIPTOR.message_types_by_name['UpdateUser'] = _UPDATEUSER

ProposeUpdateUserManager = _reflection.GeneratedProtocolMessageType('ProposeUpdateUserManager', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSEUPDATEUSERMANAGER,
  __module__ = 'user_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ProposeUpdateUserManager)
  ))
_sym_db.RegisterMessage(ProposeUpdateUserManager)

ConfirmUpdateUserManager = _reflection.GeneratedProtocolMessageType('ConfirmUpdateUserManager', (_message.Message,), dict(
  DESCRIPTOR = _CONFIRMUPDATEUSERMANAGER,
  __module__ = 'user_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ConfirmUpdateUserManager)
  ))
_sym_db.RegisterMessage(ConfirmUpdateUserManager)

RejectUpdateUserManager = _reflection.GeneratedProtocolMessageType('RejectUpdateUserManager', (_message.Message,), dict(
  DESCRIPTOR = _REJECTUPDATEUSERMANAGER,
  __module__ = 'user_transaction_pb2'
  # @@protoc_insertion_point(class_scope:RejectUpdateUserManager)
  ))
_sym_db.RegisterMessage(RejectUpdateUserManager)

CreateUser = _reflection.GeneratedProtocolMessageType('CreateUser', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUSER,
  __module__ = 'user_transaction_pb2'
  # @@protoc_insertion_point(class_scope:CreateUser)
  ))
_sym_db.RegisterMessage(CreateUser)

UpdateUser = _reflection.GeneratedProtocolMessageType('UpdateUser', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSER,
  __module__ = 'user_transaction_pb2'
  # @@protoc_insertion_point(class_scope:UpdateUser)
  ))
_sym_db.RegisterMessage(UpdateUser)


# @@protoc_insertion_point(module_scope)