import configparser
import builtins

__all__ = ['read_params', 'PARAMS']

PARAMS = {
    'precision': 0.00001,
    'output_type': float,
    'possible_types': None,
    'dest': None
}


def read_params(file_path):
    config = configparser.ConfigParser()
    config.read_file(open(file_path))

    params = {}
    for section in config.sections():
        for key, value in config.items(section):
            params[key] = value

    if 'output_type' in params:
        output_type_name = params['output_type']
        output_type = getattr(builtins, output_type_name, float)
    else:
        output_type = float

    params['output_type'] = output_type

    PARAMS.update(params)
