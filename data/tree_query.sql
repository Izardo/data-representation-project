# https://www.treecouncil.ie/native-irish-trees
show databases;
use native_irish_trees;
drop table trees;

create table trees (
id int PRIMARY KEY, 
english_name varchar(255), 
irish_name varchar(255), 
scientific_name varchar(255)
);

select * from trees;

INSERT INTO trees VALUES (1, "Alder", "Fearnóg", "Alnus glutinosa");
INSERT INTO trees VALUES (2, "Arbutus (Strawberry Tree)", "Caithne", "Arbutus unedo");
INSERT INTO trees VALUES (3, "Ash", "Fuinseóg", "Fraxinus excelsior");
INSERT INTO trees VALUES (4, "Aspen", "Crann creathach", "Populus tremula");
INSERT INTO trees VALUES (5, "Birch (Downy)", "Beith chlúmhach", "Betula pubescens");
INSERT INTO trees VALUES (6, "Birch (Silver)", "Beith gheal", "Betula pendula");
INSERT INTO trees VALUES (7, "Blackthorn - Shrub", "Draighean", "Prunus spinosa");
INSERT INTO trees VALUES (8, "Bramble - Shrub", "Dris", "Rubus fructicosus");
INSERT INTO trees VALUES (9, "Broom - Shrub", "Giolcach sléibhe", "Cytisus scoparius");
INSERT INTO trees VALUES (10, "Buckthorn - Shrub (Alder)", "Paide bréan", "Frangula alnus");
INSERT INTO trees VALUES (11, "Buckthorn - Shrub (Purging)", "Paide bréan", "Rhamnus cathartic");
INSERT INTO trees VALUES (12, "Cherry (Bird)", "Donnroisc", "Prunus padus");
INSERT INTO trees VALUES (13, "Cherry (Wild)", "Gean – crann silíní fiáin", "Prunus avium");
INSERT INTO trees VALUES (14, "Crab Apple", "Crann fia-úll", "Malus sylvestris");
INSERT INTO trees VALUES (15, "Dog Rose - Shrub", "Feirdhris", "Rosa canina");
INSERT INTO trees VALUES (16, "Elder - Shrub", "Tromán", "Sambucus nigra");
INSERT INTO trees VALUES (17, "Gorse - Shrub", "Aiteann", "Ulex europaeus & Ulex gallii");
INSERT INTO trees VALUES (18, "Guelder Rose - Shrub", "Caorchon", "Viburnum opulus");
INSERT INTO trees VALUES (19, "Hawthorn", "Sceach gheal", "Crataegus monogyna");
INSERT INTO trees VALUES (20, "Hazel", "Coll", "Corylus avellana");
INSERT INTO trees VALUES (21, "Holly", "Cuilleann", "Ilex aquifolium");
INSERT INTO trees VALUES (22, "Honeysuckle - Shrub", "Féithleann", "Lonicera periclymenum");
INSERT INTO trees VALUES (24, "Ivy - Shrub", "Eidhneán", "Hedera helix");
INSERT INTO trees VALUES (25, "Juniper - Shrub", "Aiteal", "Juniperus communis");
INSERT INTO trees VALUES (26, "Oak (Pedunculate)", "Dair ghallda", "Quercus robur");
INSERT INTO trees VALUES (27, "Oak (Sessile)", "Dair ghaelach", "Quercus petraea");
INSERT INTO trees VALUES (28, "Rowan/Mountain Ash", "Caorthann", "Sorbus aucuparia");
INSERT INTO trees VALUES (29, "Scots Pine", "Péine albanach", "Pinus syvestris");
INSERT INTO trees VALUES (30, "Spindle - Shrub", "Feoras", "Euonymous eoropaeus");
INSERT INTO trees VALUES (31, "Whitebeam", "Fionncholl", "Sorbus spp.");
INSERT INTO trees VALUES (32, "Willow", "Saileach", "Salix spp.");
INSERT INTO trees VALUES (33, "Wych Elm", "Leamhán sléibhe", "Ulmus glabra");
INSERT INTO trees VALUES (34, "Yew", "Lúr", "Taxus baccata");