We've resurrected [geoip-appengine](http://code.google.com/p/geoip-appengine/) because we believe it can still be useful for people to deploy their own [MaxMind geolocation API](http://www.maxmind.com/app/web_services#city).

## Installation

1. Create an application on AppEngine and put your application name in the app.yaml.
2. Put your username and password in the config.py.sample and save as config.py.
3. Download the latest [GeoLiteCity](http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz) database and extract it into the /dat directory.
4. Deploy to AppEngine using the SDK

## Changes in our version

- Upgraded runtime to Python 2.7
- Switched to native json library
- Fixed invalid json
- Cleaned up codebase
- Added HTTP basic auth

## License

In keeping with the original library, this application is released under the terms of the [LGPL](http://www.gnu.org/licenses/lgpl.html).

