from flask import jsonify, make_response


class Response:
    def __init__(self):
        self.message = "successfully operation!"
        self.status = "success"
        self.status_code = 200
        self.data = None

    def response(self, **data):
        if 'status' not in data:
            data['status'] = self.status

        if 'status_code' not in data:
            data['status_code'] = self.status_code

        if 'message' not in data:
            data['message'] = self.message

        if 'data' not in data:
            data['data'] = self.data

        return make_response(jsonify(data), data['status_code'] if 'status_code' in data else 200)

    def response_created(self, **data):
        data['status_code'] = 201
        return self.response(**data)


def res():
    return Response()
