
def parse_qs(query_string):
    result = ""
    if query_string:
        list_res = query_string.split('&')
        result = '\n'.join(list_res)
    return result

def wsgi_application(environ, start_response):
    # print("===*** wsgi_app START ***===")
    # print(environ['PATH_INFO'])
    body = parse_qs(environ['QUERY_STRING']) #todo: parse request
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]
    # print("response body: " + body)
    start_response(status, headers)
    return [body]