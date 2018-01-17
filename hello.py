
def parse_environ_query_string(query_string):
    result = ""
    if not query_string:
        list_res = query_string.split('&')
        result = '\n'.join(list_res)
    return result

def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]

    body = parse_environ_query_string(environ['QUERY_STRING']) #todo: parse request
    start_response(status, headers)
    return [body]