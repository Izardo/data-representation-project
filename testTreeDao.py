from treeDao import treeDao

# Create JSON object.
tree = {
    'english_name' : 'Spruce',
    'irish_name' : 'spruceach',
    'scientific_name' : 'Sprucirea'
}

returnvalue = treeDao.create(tree)