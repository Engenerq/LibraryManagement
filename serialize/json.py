from uuid import UUID


def json_serialize(obj):
    if isinstance(obj, UUID):
        return str(obj)
    raise TypeError(f"{type(obj)}is not JSON serializable")
