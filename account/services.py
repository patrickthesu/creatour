from django.contrib.auth.models import User
from django.contrib import auth 

def signin (filledForm):
    try:
        group = filledForm.cleaned_data["group"]
        del ( filledForm.cleaned_data["group"]) 
        user = User.objects.create_user(**filledForm.cleaned_data)
        group.user_set.add(user)
        return True                
    except Exception as err:
        print (err)
        return False

def login ( request, username, password ):
    user = auth.authenticate(request, username = username, password = password)
    auth.login (request, user)
    if user is not None: return True
    return False

def logout ( request ):
    try: 
        auth.logout (request)
        return True
    except Exception as err:
        print ( "ERROR: Logout " + str (err) )
        return False

def isUserAuthor ( user ):
    group = user.groups.all()[0]
    if group.name in ( "private author", "author"): return True
    return False


        
 
    
 
