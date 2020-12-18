Using cURL to debug
Higher-level programming

cURL is a computer software project providing a library and command-line tool for transferring data using various protocols. It’s a command line tool for getting or sending files using URL syntax.

With this tool, you can request a webpage, an API or a RestAPI easily.

You can test on this simple RestAPI

For example: get the homepage of Google:

i-love-curl $ curl "http://www.google.com"
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"><meta content="noodp" name="robots"><me ....
....
0,"sce":5,"stok":"dS2NgmCFVVJ61nWw37vHdkjsH_I"},"d":{}};google.y.first.push(function(){if(google.med){google.med('init');google.initHistory();google.med('history');}});if(google.j&&google.j.en&&google.j.xi){window.setTimeout(google.j.xi,0);}
</script></div></body></html> i-love-curl $ 
Or, request a film for the RestAPI Swapi (Star Wars API)

i-love-curl $ curl https://swapi-api.hbtn.io/api/films/1/
{"title":"A New Hope","episode_id":4,"opening_crawl":"It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....","director":"George Lucas","producer":"Gary Kurtz, Rick McCallum","release_date":"1977-05-25","characters":["https://swapi-api.hbtn.io/api/people/1/","https://swapi-api.hbtn.io/api/people/2/","https://swapi-api.hbtn.io/api/people/3/","https://swapi-api.hbtn.io/api/people/4/","https://swapi-api.hbtn.io/api/people/5/","https://swapi-api.hbtn.io/api/people/6/","https://swapi-api.hbtn.io/api/people/7/","https://swapi-api.hbtn.io/api/people/8/","https://swapi-api.hbtn.io/api/people/9/","https://swapi-api.hbtn.io/api/people/10/","https://swapi-api.hbtn.io/api/people/12/","https://swapi-api.hbtn.io/api/people/13/","https://swapi-api.hbtn.io/api/people/14/","https://swapi-api.hbtn.io/api/people/15/","https://swapi-api.hbtn.io/api/people/16/","https://swapi-api.hbtn.io/api/people/18/","https://swapi-api.hbtn.io/api/people/19/","https://swapi-api.hbtn.io/api/people/81/"],"planets":["https://swapi-api.hbtn.io/api/planets/2/","https://swapi-api.hbtn.io/api/planets/3/","https://swapi-api.hbtn.io/api/planets/1/"],"starships":["https://swapi-api.hbtn.io/api/starships/2/","https://swapi-api.hbtn.io/api/starships/3/","https://swapi-api.hbtn.io/api/starships/5/","https://swapi-api.hbtn.io/api/starships/9/","https://swapi-api.hbtn.io/api/starships/10/","https://swapi-api.hbtn.io/api/starships/11/","https://swapi-api.hbtn.io/api/starships/12/","https://swapi-api.hbtn.io/api/starships/13/"],"vehicles":["https://swapi-api.hbtn.io/api/vehicles/4/","https://swapi-api.hbtn.io/api/vehicles/6/","https://swapi-api.hbtn.io/api/vehicles/7/","https://swapi-api.hbtn.io/api/vehicles/8/"],"species":["https://swapi-api.hbtn.io/api/species/5/","https://swapi-api.hbtn.io/api/species/3/","https://swapi-api.hbtn.io/api/species/2/","https://swapi-api.hbtn.io/api/species/1/","https://swapi-api.hbtn.io/api/species/4/"],"created":"2014-12-10T14:23:31.880000Z","edited":"2015-04-11T09:46:52.774897Z","url":"https://swapi-api.hbtn.io/api/films/1/"} i-love-curl $ 
Some wording/vocabulary
First, I really encourage you to read the Bilal post about HTTP headers here

URL: “Uniform Resource Locator”, defines the web address to a specific resource. An URL is composed in 4 parts:
protocol: http:// or https:// or ftp://… => defines also on which port the server will be requested
host: www.example.com or intranet.hbtn.io… => will be resolved by the DNS = hostname to IP address
path: /index.html or /states/1/cities… => path from the root of the website or webservice on this host
query string: ?name=Jon or ?q=dress&color=FF0000… => always starts by the symbol ? and follow by a list of parameters (key=value) separated by the symbol &
request: action of client to send “data” to a specific URL and return a response
response: result of a request return from the server to the client
HTTP method: or called “verb” for a RestAPI. It’s part of the HTTP protocol only (http and https request):
GET: most common method to retreive information from the server (read). When you are surfing in Google or other website, your web browser is doing GET requests to each website to reteive HTML/CSS/JS etc… to render correctly the website. Client can send some information to the server via query string.
POST: use to send datas to the server (write) contain in the request body (see below)
HEAD: same as GET but with an empty response. It’s mainly used to check if a resource is available but without get it.
PUT/PATCH: to update a resource with datas contain in the request body
DELETE: to remove a resource in the server (mainly used for an RestAPI)
others…
Header: an header is a hash of Key-Value information. You can have request header (informations from the client to the server), but also response header (server to client). Headers are really useful and some “Keys-Values” are standardized:
User-Agent: from the client to the server for describing the client. Ex: Chrome used as User-Agent: “Mozilla/5.0 (Macintosh; Intel Mac OS X 10116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36”
Origin: from the client to the server for giving information of where come from the request to the server
Content-Type: define how the body can be read. Ex: “https://swapi-api.hbtn.io/api/planets/1/” => “Content-Type: application/json” because the response body is a JSON
Content-Length: size in Bytes of the request/response body
others
Body: a body is Bytes transmitted in HTTP. You can have request body (parameters from the client to the server) and response body (return result of the server to the client)
URL encoding: action to transcode regular string to query string. It’s also used for request body in case of Content-Type: application/x-www-form-urlencoded
Some cool options:

Verbose mode
-vvv will print all headers and transfer state of a request/response

Output direction
-o redirect the response body of a request to a file:

i-love-curl $ curl "http://www.google.com" -o google_homepage.html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 11279    0 11279    0     0   145k      0 --:--:-- --:--:-- --:--:--  146k
i-love-curl $ ls
google_homepage.html
i-love-curl $
or to nothing:

i-love-curl $ curl "http://www.google.com" -o /dev/null
i-love-curl $ 
HTTP method
-X define which HTTP:

-X GET: to do a GET request (by default)
-X POST: to do a POST request
-X PUT: to do a PUT request
-X DELETE: to do a DELETE request
Body / parameters
All query string parameters can be directly add to the URL. But for other HTTP method, you should use the attribute -d. You can use only one and it should be url encoded (separated by the symbol &) or multiples. By default, the Content-Type: application/x-www-form-urlencoded

Add a new state to a RestAPI:

i-love-curl $ curl "http://localhost:5555/states" -X POST -d "name=California&code=CA"
{ "id": 12, "name": "California", "code": "CA" }
i-love-curl $ 
or for update a state to a RestAPI:

i-love-curl $ curl "http://localhost:5555/states/12" -X PUT -d "name=California Forever" -d "code=CAF"
{ "id": 12, "name": "California Forever", "code": "CAF" }
i-love-curl $ 
and if you encode the request body as JSON (by setting a correct Content-Type in the header) and your server understand it:

i-love-curl $ curl "http://localhost:5555/states" -X POST -H "Content-Type: application/json" -d "{ \"name\": \"California\", \"code\": \"CA\" }"
{ "id": 13, "name": "California", "code": "CA" }
i-love-curl $ 
Header values
-H will set your parameter in the Header part.

For example, to send a custom Header (by convention, it will start by X-):

i-love-curl $ curl "http://localhost:5555/states" -X GET -H "X-Application-id: 14"
[{ "id": 12, "name": "California Forever", "code": "CAF" }, { "id": 13, "name": "California", "code": "CA" }]
i-love-curl $ 
or overwriting a standard Header (here Content-Type and User-Agent):

i-love-curl $ curl "http://localhost:5555/states" -X GET -H "X-Application-id: 14" -H "Content-Type: text/xml" -H "User-Agent: MyCustomClient"
<xml>
  <states>
    <state id="12" code="CAF">
      <name>California Forever</name>
    </state>
    <state id="13" code="CA">
      <name>California</name>
    </state>
  </states>
</xml>
i-love-curl $ 
