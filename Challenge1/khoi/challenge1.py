def displayinfo():
    mylist={'Home':'20GB','Docs':'15MB','Vids':'30GB','Other':'25KB'}
    userschoice = input("Please enter the location you want to lookup: ")
    print(mylist[userschoice])

displayinfo()