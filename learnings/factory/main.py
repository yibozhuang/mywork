from object_serializer import ObjectSerializer
from songs import Song


def main():
    song = Song('1', 'Water of Love', 'Kelly Clarkson')
    serializer = ObjectSerializer()

    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
    print(serializer.serialize(song, 'YAML'))


if __name__ == "__main__":
    main()
