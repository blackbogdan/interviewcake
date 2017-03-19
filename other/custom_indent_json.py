import json

def indent_json(name = 'json_example.json'):
    with open(name) as handle:
        text = handle.read()
        print json.loads(text)
        indented = json.dumps(json.loads(text), indent=4)
        print indented


indent_json()


import _ctypes
import json
import re

def di(obj_id):
    # from http://stackoverflow.com/a/15012814/355230
    """ Reverse of id() function. """
    return _ctypes.PyObj_FromPtr(obj_id)

class NoIndent(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        if not isinstance(self.value, list):
            return repr(self.value)
        else:  # the sort the representation of any dicts in the list
            reps = ('{{{}}}'.format(', '.join(('{!r}:{}'.format(
                                        k, v) for k, v in sorted(v.items()))))
                    if isinstance(v, dict) else repr(v) for v in self.value)

            return '[' + ', '.join(reps) + ']'

class MyEncoder(json.JSONEncoder):
    FORMAT_SPEC = "@@{}@@"
    regex = re.compile(FORMAT_SPEC.format(r"(\d+)"))

    def default(self, obj):
        if not isinstance(obj, NoIndent):
            return super(MyEncoder, self).default(obj)
        return self.FORMAT_SPEC.format(id(obj))

    def encode(self, obj):
        format_spec = self.FORMAT_SPEC  # local var to expedite access
        result = super(MyEncoder, self).encode(obj)
        for match in self.regex.finditer(result):
            id = int(match.group(1))
            result = result.replace('"{}"'.format(format_spec.format(id)),
                                    repr(di(int(id))))
        return result

data_structure = {
    'layer1': {
        'layer2': {
            'layer3_1': NoIndent([{"x":1,"y":7}, {"x":0,"y":4}, {"x":5,"y":3},
                                  {"x":6,"y":9}]),
            'layer3_2': 'string',
            'layer3_3': NoIndent([{"x":2,"y":8,"z":3}, {"x":1,"y":5,"z":4},
                                  {"x":6,"y":9,"z":8}]),
            'layer3_4': NoIndent(list(range(20))),
        }
    }
}

print(json.dumps("json_exmaple.json", cls=MyEncoder, indent=2))