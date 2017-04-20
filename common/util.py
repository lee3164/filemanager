from flask import request, make_response
import json

from common.error import FileManagerErrorCode


def _get_param(key, default_value, value_type):
    assert request.method == 'GET'
    value = None
    try:
        value = request.args.get(key) or default_value
        if value_type:
            value = value_type(value)
    except:
        value = default_value

    return value


def _post_param(key, default_value, value_type):
    assert request.method == 'POST'
    value = None
    try:
        value = request.form.get(key) or default_value
        if value_type:
            value = value_type(value)
    except:
        value = default_value

    return value


def get_post_param(key, default_value, value_type):
    value = None
    if request.method == 'GET':
        value = _get_param(key, default_value, value_type)
    elif request.method == 'POST':
        value = _post_param(key, default_value, value_type)

    return value


def make_json_success_response(data=None):
    ret = {
        'code': FileManagerErrorCode.ERROR_CODE_OK,
        'message': FileManagerErrorCode.get_err_msg(FileManagerErrorCode.ERROR_CODE_OK),
        'data': data
    }
    if data is None or data == {}:
        del ret['data']
    return make_json_response(ret)


def make_json_response(data):
    content_type = 'application/json'
    response = make_response(json.dumps(data))
    response.headers['Content-type'] = content_type
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8080'
    response.headers['Access-Control-Allow-Credentials'] = "true"
    return response


def assert_param_is_none(*args):
    for arg in args:
        assert arg is not None and arg != '', 'assert error'
