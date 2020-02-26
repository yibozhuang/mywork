from serializers import factory


class ObjectSerializer:
    def serialize(self, serlizable, format):
        serializer = factory.get_serializer(format)
        serlizable.serialize(serializer)
        return serializer.to_str()
