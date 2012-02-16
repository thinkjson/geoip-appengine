from google.appengine.api import memcache
import pygeoip

def getIpInfo(txt_ip):
	entry=memcache.get(txt_ip)

	if entry is None:
		plik=open('dat/GeoLiteCity.dat')
		gic = pygeoip.GeoIP(filename='dat/GeoLiteCity.dat', filehandle=plik)
		entry=gic.record_by_addr(txt_ip)
		if entry is not None:
			memcache.set(key=txt_ip,value=entry)
	return entry