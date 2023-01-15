class IsReadMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        print('Request on url {}'.format(request.path))

        return response
