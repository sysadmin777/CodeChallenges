#Home 20GB
#Docs 15MB
#Vids 30GB
#Other 25KB
import sys
Sizes = {'Home': '20GB', 'Docs': '15MB', 'Vid': '30GB', 'Other': '25KB'}

def returnSize(key):
    if key not in Sizes:
        print('That key does not exist '+key)
        return 0
    return print(key+' '+Sizes[key])
returnSize(sys.argv[1])