# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello_world.proto
#pylint: disable-all

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
  name='hello_world.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x11hello_world.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"4\n\x17MultipleHelloResRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03res\x18\x02 \x01(\x05\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xef\x01\n\x07Greeter\x12(\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x12@\n\x13SayHelloUnaryStream\x12\x18.MultipleHelloResRequest\x1a\x0b.HelloReply\"\x00\x30\x01\x12\x35\n\x13SayHelloStreamUnary\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00(\x01\x12\x41\n\x12SayHelloBidiStream\x12\x18.MultipleHelloResRequest\x1a\x0b.HelloReply\"\x00(\x01\x30\x01\x62\x06proto3')
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=21,
  serialized_end=49,
)


_MULTIPLEHELLORESREQUEST = _descriptor.Descriptor(
  name='MultipleHelloResRequest',
  full_name='MultipleHelloResRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='MultipleHelloResRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res', full_name='MultipleHelloResRequest.res', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=51,
  serialized_end=103,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=105,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['MultipleHelloResRequest'] = _MULTIPLEHELLORESREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

MultipleHelloResRequest = _reflection.GeneratedProtocolMessageType('MultipleHelloResRequest', (_message.Message,), dict(
  DESCRIPTOR = _MULTIPLEHELLORESREQUEST,
  __module__ = 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:MultipleHelloResRequest)
  ))
_sym_db.RegisterMessage(MultipleHelloResRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREPLY,
  __module__ = 'hello_world_pb2'
  # @@protoc_insertion_point(class_scope:HelloReply)
  ))
_sym_db.RegisterMessage(HelloReply)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='Greeter',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=137,
  serialized_end=376,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='Greeter.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloUnaryStream',
    full_name='Greeter.SayHelloUnaryStream',
    index=1,
    containing_service=None,
    input_type=_MULTIPLEHELLORESREQUEST,
    output_type=_HELLOREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloStreamUnary',
    full_name='Greeter.SayHelloStreamUnary',
    index=2,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloBidiStream',
    full_name='Greeter.SayHelloBidiStream',
    index=3,
    containing_service=None,
    input_type=_MULTIPLEHELLORESREQUEST,
    output_type=_HELLOREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.SayHello = channel.unary_unary(
          '/Greeter/SayHello',
          request_serializer=HelloRequest.SerializeToString,
          response_deserializer=HelloReply.FromString,
          )
      self.SayHelloUnaryStream = channel.unary_stream(
          '/Greeter/SayHelloUnaryStream',
          request_serializer=MultipleHelloResRequest.SerializeToString,
          response_deserializer=HelloReply.FromString,
          )
      self.SayHelloStreamUnary = channel.stream_unary(
          '/Greeter/SayHelloStreamUnary',
          request_serializer=HelloRequest.SerializeToString,
          response_deserializer=HelloReply.FromString,
          )
      self.SayHelloBidiStream = channel.stream_stream(
          '/Greeter/SayHelloBidiStream',
          request_serializer=MultipleHelloResRequest.SerializeToString,
          response_deserializer=HelloReply.FromString,
          )


  class GreeterServicer(object):
    """The greeting service definition.
    """

    def SayHello(self, request, context):
      """Sends a greeting.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def SayHelloUnaryStream(self, request, context):
      """Sends one greeting, get multiple response.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def SayHelloStreamUnary(self, request_iterator, context):
      """Send multiple greetings, get one response.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def SayHelloBidiStream(self, request_iterator, context):
      """Send multiple greetings, get multiple response.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SayHello': grpc.unary_unary_rpc_method_handler(
            servicer.SayHello,
            request_deserializer=HelloRequest.FromString,
            response_serializer=HelloReply.SerializeToString,
        ),
        'SayHelloUnaryStream': grpc.unary_stream_rpc_method_handler(
            servicer.SayHelloUnaryStream,
            request_deserializer=MultipleHelloResRequest.FromString,
            response_serializer=HelloReply.SerializeToString,
        ),
        'SayHelloStreamUnary': grpc.stream_unary_rpc_method_handler(
            servicer.SayHelloStreamUnary,
            request_deserializer=HelloRequest.FromString,
            response_serializer=HelloReply.SerializeToString,
        ),
        'SayHelloBidiStream': grpc.stream_stream_rpc_method_handler(
            servicer.SayHelloBidiStream,
            request_deserializer=MultipleHelloResRequest.FromString,
            response_serializer=HelloReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaGreeterServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The greeting service definition.
    """
    def SayHello(self, request, context):
      """Sends a greeting.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SayHelloUnaryStream(self, request, context):
      """Sends one greeting, get multiple response.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SayHelloStreamUnary(self, request_iterator, context):
      """Send multiple greetings, get one response.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SayHelloBidiStream(self, request_iterator, context):
      """Send multiple greetings, get multiple response.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaGreeterStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The greeting service definition.
    """
    def SayHello(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Sends a greeting.
      """
      raise NotImplementedError()
    SayHello.future = None
    def SayHelloUnaryStream(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Sends one greeting, get multiple response.
      """
      raise NotImplementedError()
    def SayHelloStreamUnary(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      """Send multiple greetings, get one response.
      """
      raise NotImplementedError()
    SayHelloStreamUnary.future = None
    def SayHelloBidiStream(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      """Send multiple greetings, get multiple response.
      """
      raise NotImplementedError()


  def beta_create_Greeter_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Greeter', 'SayHello'): HelloRequest.FromString,
      ('Greeter', 'SayHelloBidiStream'): MultipleHelloResRequest.FromString,
      ('Greeter', 'SayHelloStreamUnary'): HelloRequest.FromString,
      ('Greeter', 'SayHelloUnaryStream'): MultipleHelloResRequest.FromString,
    }
    response_serializers = {
      ('Greeter', 'SayHello'): HelloReply.SerializeToString,
      ('Greeter', 'SayHelloBidiStream'): HelloReply.SerializeToString,
      ('Greeter', 'SayHelloStreamUnary'): HelloReply.SerializeToString,
      ('Greeter', 'SayHelloUnaryStream'): HelloReply.SerializeToString,
    }
    method_implementations = {
      ('Greeter', 'SayHello'): face_utilities.unary_unary_inline(servicer.SayHello),
      ('Greeter', 'SayHelloBidiStream'): face_utilities.stream_stream_inline(servicer.SayHelloBidiStream),
      ('Greeter', 'SayHelloStreamUnary'): face_utilities.stream_unary_inline(servicer.SayHelloStreamUnary),
      ('Greeter', 'SayHelloUnaryStream'): face_utilities.unary_stream_inline(servicer.SayHelloUnaryStream),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Greeter_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Greeter', 'SayHello'): HelloRequest.SerializeToString,
      ('Greeter', 'SayHelloBidiStream'): MultipleHelloResRequest.SerializeToString,
      ('Greeter', 'SayHelloStreamUnary'): HelloRequest.SerializeToString,
      ('Greeter', 'SayHelloUnaryStream'): MultipleHelloResRequest.SerializeToString,
    }
    response_deserializers = {
      ('Greeter', 'SayHello'): HelloReply.FromString,
      ('Greeter', 'SayHelloBidiStream'): HelloReply.FromString,
      ('Greeter', 'SayHelloStreamUnary'): HelloReply.FromString,
      ('Greeter', 'SayHelloUnaryStream'): HelloReply.FromString,
    }
    cardinalities = {
      'SayHello': cardinality.Cardinality.UNARY_UNARY,
      'SayHelloBidiStream': cardinality.Cardinality.STREAM_STREAM,
      'SayHelloStreamUnary': cardinality.Cardinality.STREAM_UNARY,
      'SayHelloUnaryStream': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Greeter', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
