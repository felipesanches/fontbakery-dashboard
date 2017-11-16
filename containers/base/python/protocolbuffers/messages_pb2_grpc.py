# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
import messages_pb2 as messages__pb2


class CacheStub(object):
  """The Cache service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Put = channel.stream_stream(
        '/fontbakery.dashboard.Cache/Put',
        request_serializer=messages__pb2.CacheItem.SerializeToString,
        response_deserializer=messages__pb2.CacheKey.FromString,
        )
    self.Get = channel.unary_unary(
        '/fontbakery.dashboard.Cache/Get',
        request_serializer=messages__pb2.CacheKey.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_any__pb2.Any.FromString,
        )
    self.Purge = channel.unary_unary(
        '/fontbakery.dashboard.Cache/Purge',
        request_serializer=messages__pb2.CacheKey.SerializeToString,
        response_deserializer=messages__pb2.CacheStatus.FromString,
        )


class CacheServicer(object):
  """The Cache service
  """

  def Put(self, request_iterator, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Sends another greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Purge(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CacheServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Put': grpc.stream_stream_rpc_method_handler(
          servicer.Put,
          request_deserializer=messages__pb2.CacheItem.FromString,
          response_serializer=messages__pb2.CacheKey.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=messages__pb2.CacheKey.FromString,
          response_serializer=google_dot_protobuf_dot_any__pb2.Any.SerializeToString,
      ),
      'Purge': grpc.unary_unary_rpc_method_handler(
          servicer.Purge,
          request_deserializer=messages__pb2.CacheKey.FromString,
          response_serializer=messages__pb2.CacheStatus.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fontbakery.dashboard.Cache', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ManifestStub(object):
  """The Manifest service

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Poke = channel.unary_unary(
        '/fontbakery.dashboard.Manifest/Poke',
        request_serializer=messages__pb2.PokeRequest.SerializeToString,
        response_deserializer=messages__pb2.GenericResponse.FromString,
        )


class ManifestServicer(object):
  """The Manifest service

  """

  def Poke(self, request, context):
    """FIXME: this is outdated but may have some good bits!
    check for updates and emit a notice if since the last poke families
    were updated
    so if there's a change, we'll download it directly and put the files
    ordered into a Files message. The sha256 hash is what we emit as
    a change message ManifestKey: (manifiestid/collectionid, family name, filesHash)
    PokeResponse, is basically nothing, just a OK message ... how to do this
    best with grpc?
    Maybe we could directly send this to the cache?
    If we need to re-run an entiren Collection, because Font Bakery changed,
    we still need the latest versions of the collection on disk.
    so, it would be nice to have some form of atomicity between asking the
    informing the ManifestMaster and running the tests. Therefore, we could
    just put the entire current state into the cache and then let the
    ManifestMaster decide which ones to keep and which ones to drop.
    The Manifest itselt can in the meantime update itself etc.
    I.e. We create a "Snapshot" of the manifest in the cache, then
    we can forget about it
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ManifestServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Poke': grpc.unary_unary_rpc_method_handler(
          servicer.Poke,
          request_deserializer=messages__pb2.PokeRequest.FromString,
          response_serializer=messages__pb2.GenericResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fontbakery.dashboard.Manifest', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
