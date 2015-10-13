[![Build Status](https://img.shields.io/travis/JamieCressey/python-restful-client.svg)](https://travis-ci.org/JamieCressey/python-restful-client)
[![PyPi Version](https://img.shields.io/pypi/v/RestfulClient.svg)](https://pypi.python.org/pypi/RestfulClient)
[![PyPi Downloads](https://img.shields.io/pypi/dm/RestfulClient.svg)](https://pypi.python.org/pypi/RestfulClient)
[![PyPi License](https://img.shields.io/pypi/l/RestfulClient.svg)](http://opensource.org/licenses/MIT)

# Generic RESTful Python client

A generic RESTful Python client for interacting with JSON APIs.

## Usage

To use this client you just need to import ApiClient and initialize it with an API Key, Secret and URL endpoint

    from RestfulClient.api import ApiClient
    api = ApiClient('#your_api_key', '#your_api_secret', '#your_api_endpoint')

Now that you have a RESTful API object you can start sending requests.

## Request Authentication

All requests include the following headers by default:
- 'X-Authentication-Key' - The API Key provided when creating the ApiClient object.
- 'X-Authentication-Nonce' - An incremental number to prevent request replays. By default this is the current epoch time in milliseconds.
- 'X-Authentication-Signature' - A SHA512 HMAC signature of the nonce, signed using the API Secret provided when creating the ApiClient object.

## Making a request

The framework supports GET, PUT, POST and DELETE requests:

    api.get('/books/')
    api.post('/books/', {'title': 'Twilight', 'author': 'Stephenie Meyer'})
    api.put('/book/Twilight/', {'release_date': '06/09/2006'})
    api.delete('/book/Twilight/')

## Verifying Requests

Two helpers are built in to verify the success of requests made. `ok()` checks for a 20x status code and returns a boolean, `errors()` returns the body content as a dict object if the status code is not 20x:

    req = api.get('/books/')
    if req.ok():
        print 'Success!'
    else:
        print req.errors()

## Extending the client

The client can be extended to be more application specific, e.g. `api.create_book('Twilight', 'Stephenie Meyer')`:

    def create_book(title, author):
        _data = {
            'title': title,
            'author': author,
        }
        return self.post('/books/', _data)

## Contributing

All contributions are welcome, either for new\improved functionality or in response to any open bugs.
