<div align="center"><img src="https://user-images.githubusercontent.com/66263776/98416555-43fa9b80-204d-11eb-800a-df8e19b62655.jpg" width="500" height= "200"> </div>

# <img src="https://user-images.githubusercontent.com/66263776/98705433-b6b88f00-234b-11eb-97b7-cb193f7424f4.png" width="20" height= "30"> 0x14. Javascript - Web scraping <img src="https://user-images.githubusercontent.com/66263776/98705433-b6b88f00-234b-11eb-97b7-cb193f7424f4.png" width="20" height= "30">

## :book: Description of the project :book:

## :books: Important concept :books:
<details>
<summary>:hammer_and_wrench:<b>Instalation requirement</b>:hammer_and_wrench:</summary>
To begin with this project you need to have the follow packet:<br>
<br>

**INSTALL NODE 10**

```console
user@ubuntu$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
user@ubuntu$ sudo apt-get install -y nodejs
```

Then to identify sintaxis error en el code you need to install this:<br>
<br>

**INSTALL SEMI-STANDARD**
```console
user@ubuntu$ $ sudo npm install semistandard --global
```

Then in this project you need to do scrapping, so you need to have de library request in javascript
**Install request module and use it**

```console
user@ubuntu$ sudo npm install request --global
user@ubuntu$ export NODE_PATH=/usr/lib/node_modules
```
</details>
<details>
	<summary>:boom:<b>How to create an object in Javascript.</b></summary>
	<br/>

</details>

## :memo: Activities :memo:
 ## [Readme ]()

Write a script that reads and prints the content of a file.

* The first argument is the file path
* The content of the file must be read in utf-8
* If an error occurred during the reading, print the error object
```console
user@ubuntu:~/0x14$ cat cisfun
C is super fun!
user@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

user@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
user@ubuntu:~/0x14$ 
```



## [Write me ]()

Write a script that writes a string to a file.

* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in utf-8
* If an error occurred during while writing, print the error object

```console
user@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
user@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
user@ubuntu:~/0x14$ 
```



## [Status code ]()

Write a script that display the status code of a GET request.

* The first argument is the URL to request (GET)
* The status code must be printed like this: code: <status code>
* You must use the module request

```console
user@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
user@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
user@ubuntu:~/0x14$ 
```



## [Star wars movie title ]()

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

* The first argument is the movie ID
* You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
* You must use the module request

```console
user@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
user@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
user@ubuntu:~/0x14$ 
```



## [Star wars Wedge Antilles ]()

Write a script that prints the number of movies where the character “Wedge Antilles” is present.

* The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
* Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
* You must use the module request

```console
user@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.hbtn.io/api/films
3
user@ubuntu:~/0x14$ 
```



## [Loripsum ]()

Write a script that gets the contents of a webpage and stores it in a file.

* The first argument is the URL to request
* The second argument the file path to store the body response
* The file must be UTF-8 encoded
* You must use the module request

```console
user@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
user@ubuntu:~/0x14$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>

<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>

<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>

<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>

user@ubuntu:~/0x14$ 
```



## [How many completed? ]()

Write a script that computes the number of tasks completed by user id.

* The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
* Only print users with completed task
* You must use the module request

```console
user@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
user@ubuntu:~/0x14$

```
