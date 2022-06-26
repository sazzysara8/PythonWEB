from website import create_app
#whenever the "__init__.py" file inside a folder, it becomes a python package. 
#This means that when you import the "name" of the folder, it will by defult run all the stuff in the "__init__.py" file
#therefore makes it possible to import "create_app"

app = create_app()

if __name__ == '__main__':
    #Only if we run this file (not import), are we going to execute the following line
    app.run(debug=True)
    #If we do not do this process and we import "main.py" from another file, it will run the web server
    #Allows the app to run only when ordered
    #TRUE means whenever there is a change made to the python code, it will automatically re-run the web server 
    
