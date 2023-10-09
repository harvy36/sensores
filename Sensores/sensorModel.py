from marshmallow import Schema, fields


class SensorPir(object):
    """Sensor schema."""

    def __init__(self, id, time, value):
        """Init."""
        self.id = id
        self.time = time
        self.value = value


class SensorPirSchema(Schema):
    """Sensor schema."""

    id = fields.Int()
    time = fields.Str()
    value = fields.Int()


class SensorDistance(object):
    """Sensor schema."""

    def __init__(self, id, time, value):
        """Init."""
        self.id = id
        self.time = time
        self.value = value


class SensorDistanceSchema(Schema):
    """Sensor schema."""

    id = fields.Int()
    time = fields.Str()
    value = fields.Int()
