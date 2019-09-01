def application(env, start_response):
    start_response('200 OK', [('content type', 'text/html')])
    return [b"Hello uWSGI"]