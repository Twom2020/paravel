from flask import request


def get(name=None):
    if name is None:
        return request.args
    return request.args.get(name)


def post(name=None):
    if name is None:
        return request.form
    return request.form.get(name)
