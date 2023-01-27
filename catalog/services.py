from .  import forms, models

def createEmptyEthap ():
    try:
        ethap = models.TouristProductEthap.objects.create()
        return ethap.id
    except Exception as err: 
        print ( "ERROR: Create empty ethap " + str (err) )
    return False

def deleteEthap ( request, ethapId ):
    try:
        ethap = models.TouristProductEthap.objects.get(pk=ethapId)
        models.TouristProductEthap.objects.remove(ethap)
        return True
    except Exception as err:
        print ("ERROR: Delete ethap " + str (err))
    return False



def editEthap (request, ethapId):
    form = forms.EthapForm (request.POST)
    if form.is_valid():
        ethap = models.TouristProductEthap.objects.get(pk=ethapId)
        ethap.set ( **request.args )
        ethap.save ()
        
        
        

    
