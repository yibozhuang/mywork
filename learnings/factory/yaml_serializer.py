import yaml
from json_serializer import JSONSerializer


class YAMLSerializer(JSONSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)
