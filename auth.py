import config
import base64

def basicAuth(webappRequest):
    # Parse the header to extract a user/password combo.
    # We're expecting something like "Basic XZxgZRTpbjpvcGVuIHYlc4FkZQ=="
    auth_header = webappRequest.request.headers.get('Authorization')

    if auth_header == None:
        webappRequest.response.set_status(401, message="Authorization Required")
        webappRequest.response.headers['WWW-Authenticate'] = 'Basic realm="geoip"'
        user_arg = None
        pass_arg = None
    else:
        # Isolate the encoded user/passwd and decode it
        auth_parts = auth_header.split(' ')
        user_pass_parts = base64.b64decode(auth_parts[1]).split(':')
        user_arg = user_pass_parts[0]
        pass_arg = user_pass_parts[1]
    
    authenticated = False
    if user_arg == config.username and pass_arg == config.password:
        authenticated = True
    else:
        webappRequest.response.set_status(401, message="Authorization Required")
        webappRequest.response.headers['WWW-Authenticate'] = 'Basic realm="geoip"'
        
        # Rendering a 401 Error page is a good way to go...
        webappRequest.response.out.write("Authorization Required")
    return authenticated