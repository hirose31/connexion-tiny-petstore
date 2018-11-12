from connexion.apps.flask_app import FlaskJSONEncoder
from sqlathanor import FlaskBaseModel


class JSONEncoder(FlaskJSONEncoder):
    def default(self, o):
        if isinstance(o, FlaskBaseModel):
            return o.to_dict(max_nesting=2)
        return FlaskJSONEncoder.default(self, o)
