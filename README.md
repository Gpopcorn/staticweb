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

webserver = StaticWeb.WebServer(StaticWeb.LocalHost(), 1234)
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

## WebServer
WebServer is used to create the server that all the content is hosted on. This creates a server socket that runs on the web. You can use it by typing `webserver = StaticWeb.WebServer(ip, port)` replacing `ip` with an actual IP (string) and `port` with an open port (integer). WebServer will be the main part of your StaticWeb script.
### SetMainPage
SetMainPage is used to create a page to be available using the URL `/`.  This would likely be the main front page of your site. You can use this function with `webserver.SetMainPage(file)` replacing the word `file` with an actual HTML file path (string). You have to put the file into your `templates` folder.
### Set404Page
Set404Page is somewhat like SetMainPage but it sets the page that shows up when you access a URL that doesn't exist. To use this, type `webserver.Set404Page(file)` into your script, replacing `file` with an actual HTML file path (string). You have to create a new folder called `error-templates` and put it in there. This is to separate your regular templates from your error templates so people can't access them through URL.
### MainLoop
MainLoop is the function that you call at the end of your script to run all the stuff that needs to be in a loop. It MUST be in the script for your code to work. You can use it by typing `webserver.MainLoop()` into your code.
## LocalHost
LocalHost is used to make it easy to set up a server on a local IP. It returns the value `"0.0.0.0"`. You can use it by typing `StaticWeb.LocalHost()` into your code. It cannot be used if you are trying to make your web server public.

## Multiple Pages
Getting multiple pages on your website is easy. You can create HTML files in a templates folder called `templates`. It must be in a folder with that exact name or this WILL NOT work. Every page you put in there will be accessible by the URL. All of the files can be seen by typing `/filename.html` into your browser next to the IP and port. If you want to create folders inside the `templates` folder you can go right ahead. Just remember when doing that you access it using `/foldername/filename.html` into the URL. You MUST add the .html to the end of the file or it will not work.

## Understanding Console Output
In StaticWeb there are some things that will be put out into the console. All of the console output does have a meaning and here is where I will explain the meanings.
### [LISTENING]
The full output should look like this `[LISTENING] Now listening on address: ip:port` replacing `ip` with the IP you used and `port` with the port you used. This lets you know that your web server has started and is ready for people to connect to it. If this doesn't come into your output after you run your server then you know something is wrong in your code.
### [CONNECTION]
The full output should look like this `[CONNECTION] Connection at url: url` replacing the second `url` with the URL that the person has accessed. This shows that someone connected successfully to your website at a specific page. Whenever somebody refreshes or accesses a new port on your website, this will appear.
### [404 ERROR]
The full output should look like this `[404 ERROR] 404 error at url: url` replacing the second `url` with the URL that the person has accessed. This error means that somebody has connected to a page on your website that doesn't exist. This message will show whenever somebody gets a 404 error. This does NOT mean that all of your code is broken.

# Future of StaticWeb
The future of StaticWeb is unclear. I might add on to this soon or just leave it alone for a while. I might work on other Python modules as well. This was a great learning experience to making modules, but I might have to move on to greater things. I will definitely do some bug fixing if there is any issues with that. If anyone is willing to take over StaticWeb for me, I would probably accept the offer. I'm not sure what the future is for this Python module, but it was great making it either way!
