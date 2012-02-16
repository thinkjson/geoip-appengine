#!/usr/bin/env python
import webapp2

import auth
import models
import json

class IPHandler(webapp2.RequestHandler):
    def get(self, output_format, ip):
        authenticated = auth.basicAuth(self)
        if authenticated != True:
            return
        
        if ip == "self" or ip is None:
            ip = self.request.remote_addr

        entry=models.getIpInfo(ip)
        if entry is not None:
            if output_format == "json":
                self.response.headers['Content-Type'] = 'application/json'
                entry['ip'] = ip
                json.dump(entry, self.response.out)
            elif output_format == "xml":
                self.response.headers['Content-Type'] = 'application/xml'
                self.response.out.write('<GeoIP ip="%s">\n'% (ip))
                for key in entry:
                    self.response.out.write('   <%s>%s</%s>\n'% (key, entry[key], key))
                self.response.out.write('</GeoIP>\n')
            else: # Default to plain text
                self.response.headers['Content-Type'] = 'text/plain'
                self.response.out.write('ip=%s\n'% (ip))
                for key in entry:
                    self.response.out.write('%s=%s\n'% (key, entry[key]))
            self.response.set_status(200)
        else:
            self.response.set_status(404)

app = webapp2.WSGIApplication([('/([^/]+)?/([^/]+)?', IPHandler)])