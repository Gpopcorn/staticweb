# StaticWeb Description
StaticWeb is designed to make it super simple to write backend for a static Python web project. It is made from Socket to allow for creation of servers and display them on the web. It's easy to get started making static web projects with it!
# StaticWeb Documentation
## Quick Start Guide
Install using 
`pip install --index-url https://test.pypi.org/simple/ --no-deps staticweb-Gpopcorn`
OR
`python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps staticweb-Gpopcorn`

Start your first project by creating a new file called `main.py` (or whatever you want). 
Type in the file the following:
```python
from staticweb import StaticWeb

webserver = staticweb.WebServer(staticweb.LocalHost(), 1234)
webserver.MainLoop()
```
Create a new folder called `templates` (must be named this or it won't work), and create a file called `helloworld.html`. 
Go into the file and type in the following:
```html
<!DOCTYPE html>
<html>
	<head>
		<title>Hello World</title>
	</head>
	<body>
		<h1>Hello World!</h1>
	</body>
</html>
```
Run your web server by running `main.py`. Go into a web a web browser and type `localhost:1234/helloworld.html` into the search bar. Hit enter and see your web page show up! If you get brought to a 404 page see further down in the documentation to see how you can fix. If there is an error within Python you may have installed the package wrong or misspelled something in your code. If that doesn't work it's probably an error with StaticWeb (sorry if this is so) and I will try to fix as fast as I can.

MORE TO DOCUMENTATION COMING SOON!