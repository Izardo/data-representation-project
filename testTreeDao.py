# This program was used to test the functioning of the DAO.

from treeDao import treeDao

# Create JSON object.
tree = {
    'english_name' : 'Spruce',
    'irish_name' : 'spruceach',
    'scientific_name' : 'Sprucirea'
}


tree1 = {'english_name' : 'hello', 
        'irish_name' : 'meh',
        'scientific_name' : 'wah', 
        'tree_id' : 1004
        }

returnValue = treeDao.delete(1000)
#returnValue = treeDao.getAll()
print(returnValue)