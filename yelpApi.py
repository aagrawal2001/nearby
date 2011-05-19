"""Command line interface to the Yelp Search API."""

import json
import oauth2
import optparse
import urllib
import urllib2


# Setup URL params from options
url_params = {}
url_params['sort'] = 2
url_params['limit'] = 10
url_params['radius_filter'] = 100
path = '/v2/search'

consumer_key = "XXX"
consumer_secret = "XXX"
oauth_token = "XXX"
token_secret = "XXX"
host = 'api.yelp.com'

def request(lat, lng):
  """Returns response for API request."""
  # Unsigned URL
  encoded_params = None
  url_params['ll'] = '%s,%s' % (lat,lng)
  if url_params:
    encoded_params = urllib.urlencode(url_params)
  url = 'http://%s%s?%s' % (host, path, encoded_params)
  print 'URL: %s' % (url,)

  # Sign the URL
  consumer = oauth2.Consumer(consumer_key, consumer_secret)
  oauth_request = oauth2.Request('GET', url, {})
  oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                        'oauth_timestamp': oauth2.generate_timestamp(),
                        'oauth_token': oauth_token,
                        'oauth_consumer_key': consumer_key})

  token = oauth2.Token(oauth_token, token_secret)
  oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
  signed_url = oauth_request.to_url()
  print 'Signed URL: %s\n' % (signed_url,)

  # Connect
  try:
    conn = urllib2.urlopen(signed_url, None)
    try:
      response = json.loads(conn.read())
    finally:
      conn.close()
  except urllib2.HTTPError, error:
    response = json.loads(error.read())

  return json.dumps(response)

