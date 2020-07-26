#!C:\Users\mis\AppData\Local\Programs\Python\Python38-32\python.exe
print("content-type: text/html\n\n")

import cgi,cgitb
import mysql.connector
"""
print("<h1>welcome to python file</h1>")
print("<hr>")
print("<h1>using input tag</h1>")
print("<body bgcolor='orange'>")"""
print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('<meta charset="utf-8">')
print('<meta name="viewport" content="width=device-width,initial-scale=1.0">')
print('<title>corona update </title>')
#<!-- css -->
print('<link rel="stylesheet" href="./css/state.css">')
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">')
print('<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap" rel="stylesheet">')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">')
print('<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">')
print('</head>')   
print('<body>')
print('<header>')

#<!--===================nav======================-->


print('<nav class="navbar navbar-expand-lg navbar-dark bg-dark">')
print('<a class="navbar-brand" href="#"><h2>cor&nbsp<span><img src="images/image.svg" height="40" width="40"></span>&nbspna</h2></a>')
print('<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">')
print('<span class="navbar-toggler-icon"></span>')
print('</button>')
  
print('<div class="collapse navbar-collapse" id="navbarSupportedContent">')
print('<ul class="navbar-nav mr-auto">')
print('<li class="nav-item active">')
print('<a class="nav-link" href="home.html">Home <span class="sr-only">(current)</span></a>')
print('</li>')
print('<li class="nav-item">')
print('<a class="nav-link" href="plans.html">plans</a>')
print('</li>')

print('<li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">update</a>')
print('<div class="dropdown-menu" aria-labelledby="navbarDropdown">')
          
print('<a action="home.py" method="POST" type="submit" class="dropdown-item" href="home.py">total case</a>')
print('<a action="home.py" method="POST" class="dropdown-item" href="state.py">state wise</a>')
        # <!----   <div class="dropdown-divider"></div>
         #   <a class="dropdown-item" href="#"></a>
          #</div>-->
print('</li>')
print('<li class="nav-item">')
print('<a class="nav-link" href="symptoms.html">symptoms</a>')
print('</li>')
print('<li class="nav-item">')
print('<a class="nav-link" href="prevention.html">prevention</a>')
print('</li>')
print('</ul>')
print('<form class="form-inline my-2 my-lg-0 navbar-dark bg-dark">')
     # <!----  <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      #  <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      #-->

      
print('<a class="nav-link text-white" href="feedback.html">feedback</a>')
      
  
print('<a class="nav-link text-white" href="about.html">about</a>')
print('<a class="nav-link text-white" href="contact.html">contact</a>')

    
print('</form>')
print('</div>')
print('</nav>')

form = cgi.FieldStorage()


email=form.getvalue("email")
suggestion=form.getvalue("suggestion")

con=mysql.connector.connect(user='root',password='',host='localhost',database='coronaupdate')
cur=con.cursor()

cur.execute("insert into feedback values(%s,%s)",(email,suggestion))
con.commit()
cur.close()
con.close()
print('<div class="bg-info">')
print('<div class="d-flex align-content-center p-5 ml-5">')
print('<div class="card p-5 m-5 ml-5" style="width: 158rem;">')
print('<div class="card-body p-5 ml-5">')
print('<h3 class="card-text text-primary ml-5">thank you for your valuable feedback</h3>')
print('<h6 class="card-text ml-5 ">go back to home page or check corona details</h6>')
print('<button href="home.html" class="card-link ml-5  btn-primary">home</button>')
print('<button href="home.py" class="card-link ml-5  btn-primary">total case</button>')
print('</div>')
print('</div>')
print('</div>')
print('</div>')
#<!-- js -->
print('<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>')
print('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>')
print('</header>')
print('</body>')
print('</html')

