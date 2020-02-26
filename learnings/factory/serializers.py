from json_serializer import JSONSerializer
from xml_serializer import XMLSerializer
from yaml_serializer import YAMLSerializer


class SerializerFactory:
    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('JSON', JSONSerializer)
factory.register_format('XML', XMLSerializer)
factory.register_format('YAML', YAMLSerializer)
