from treeDao import treeDao

# Create JSON object.
tree = {
    'tree_id' : 999, 
    'english_name' : 'Spruce',
    'irish_name' : 'spruceach',
    'scientific_name' : 'Sprucirea'
}

returnvalue = treeDao.create(tree)
print(returnvalue)