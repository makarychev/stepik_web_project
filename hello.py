def parse_qs(query_string):
    result = ""
    if query_string:
        list_res = query_string.split('&')
        result = [bytes(i+'\n', 'ascii') for i in list_res]
    return result

def wsgi_application(environ, start_response):
    print("===*** wsgi_app START ***===")
    print(environ['PATH_INFO'])
    print(environ['QUERY_STRING'])
    body = parse_qs(environ['QUERY_STRING']) #todo: parse request
    status = '200 OK'
    content_length = sum(len(s) for s in body)
    headers = [
        ('Content-Type', 'text/plain'),
       ('Content-Length', str(content_length))
    ]
    print("response body: " + str(body))
    print("body len: " + str(content_length))
    start_response(status, headers)

    return body