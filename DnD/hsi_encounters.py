from random import randint

tables = {}
tables['light_jungle'] = {
	'3': 'Intelligent',
	'4': 'Intelligent',
	'5': 'Intelligent',
	'6': 'Elemental',
	'7': 'Elemental',
	'8': 'Beast',
	'9': 'Beast',
	'10': 'Beast',
	'11': 'Beast',
	'12': 'Beast',
	'13': 'Beast',
	'14': 'Beast',
	'15': 'Elemental',
	'16': 'Elemental',
	'17': 'Intelligent',
	'18': 'Intelligent'
}
tables['light_jungle_intelligent'] = {
	'3':'Night Axe',
	'4':'Nereid',
	'5':'Lizardmen',
	'6':'Lizardmen',
	'7':'Adventurer',
	'8':'Adventurer',
	'9':'Fuegonauts',
	'10':'Fuegonauts',
	'11':'Fuegonauts',
	'12':'Fuegonauts',
	'13':'Adventurer',
	'14':'Adventurer',
	'15':'Lizardmen',
	'16':'Lizardmen',
	'17':'Lizardmen',
	'18':'Nereid'
};

SFI.tables.LightJungleElemental = {
	'3':'Magma Imp',
	'4':'Ooze Imp',
	'5':'Steam Imp',
	'6':'Water Imp',
	'7':'Water Imp',
	'8':'Earth Imp',
	'9':'Earth Imp',
	'10':'Fire Imp',
	'11':'Fire Elemental',
	'12':'Earth Elemental',
	'13':'Earth Elemental',
	'14':'Water Elemental',
	'15':'Water Elemental',
	'16':'Steam Elemental',
	'17':'Ooze Elemental',
	'18':'Magma Elemental'
};

SFI.tables.LightJungleBeast = {
	'3':'Crystal Frog*',
	'4':'Flayfiend*',
	'5':'Duecadre*',
	'6':'Muttering Serpent',
	'7':'Broadback*',
	'8':'Singing Golem*',
	'9':'Tabibari@',
	'10':'Giant Centipede@',
	'11':'Boar!',
	'12':'Giant Rat@',
	'13':'Zip Birds@',
	'14':'Vyderac+',
	'15':'Blindfire Vine',
	'16':'Dire Boar*',
	'17':'Spine Dragon*',
	'18':'Poison Dart Frog'
};

SFI.tables.HeavyJungle = {
	'3':'Elemental',
	'4':'Elemental',
	'5':'Intelligent',
	'6':'Intelligent',
	'7':'Intelligent',
	'8':'Beast',
	'9':'Beast',
	'10':'Beast',
	'11':'Beast',
	'12':'Beast',
	'13':'Intelligent',
	'14':'Intelligent',
	'15':'Intelligent',
	'16':'Elemental',
	'17':'Elemental',
	'18':'Elemental'
};

SFI.tables.HeavyJungleIntelligent = {
	'3':'Lizardmen',
	'4':'Lizardmen',
	'5':'Nereid',
	'6':'Adventurer',
	'7':'Adventurer',
	'8':'Night Axe',
	'9':'Night Axe',
	'10':'Night Axe',
	'11':'Fuegonauts',
	'12':'Fuegonauts',
	'13':'Fuegonauts',
	'14':'Adventurer',
	'15':'Adventurer',
	'16':'Nereid',
	'17':'Lizardmen',
	'18':'Lizardmen'
};

SFI.tables.HeavyJungleElemental = {
	'3':'Magma Imp',
	'4':'Ooze Imp',
	'5':'Steam Imp',
	'6':'Water Imp',
	'7':'Water Imp',
	'8':'Earth Imp',
	'9':'Fire Imp',
	'10':'Fire Imp',
	'11':'Fire Elemental',
	'12':'Fire Elemental',
	'13':'Earth Elemental',
	'14':'Water Elemental',
	'15':'Water Elemental',
	'16':'Steam Elemental',
	'17':'Ooze Elemental',
	'18':'Magma Elemental'
};

SFI.tables.HeavyJungleBeast = {
	'3':'Poison Dart Frog',
	'4':'Obsidian Digger',
	'5':'Blindfire Carpet',
	'6':'Dire Boar',
	'7':'Bolt Forager',
	'8':'Vyderac',
	'9':'Bat',
	'10':'Boar',
	'11':'Centipede (Giant)',
	'12':'Rat (Giant)',
	'13':'Coperback',
	'14':'Blindfire Vine',
	'15':'Vyderac',
	'16':'Centipede (Giant)',
	'17':'Wydarr, Bonebacked',
	'18':'Spine Dragon'
};

SFI.tables.MountainousJungle = {
	'3':'Intelligent',
	'4':'Intelligent',
	'5':'Intelligent',
	'6':'Intelligent',
	'7':'Elemental',
	'8':'Elemental',
	'9':'Beast',
	'10':'Beast',
	'11':'Beast',
	'12':'Beast',
	'13':'Elemental',
	'14':'Elemental',
	'15':'Intelligent',
	'16':'Intelligent',
	'17':'Intelligent',
	'18':'Intelligent'
};
SFI.tables.MountainousJungleIntelligent = {
	'3':'Lizardmen',
	'4':'Nereid',
	'5':'Night Axe',
	'6':'Night Axe',
	'7':'Adventurer',
	'8':'Adventurer',
	'9':'Fuegonauts',
	'10':'Fuegonauts',
	'11':'Fuegonauts',
	'12':'Fuegonauts',
	'13':'Adventurer',
	'14':'Adventurer',
	'15':'Night Axe',
	'16':'Night Axe',
	'17':'Nereid',
	'18':'Lizardmen'
};
SFI.tables.MountainousJungleElemental = {
	'3':'Steam Imp',
	'4':'Earth Imp',
	'5':'Steam Imp',
	'6':'Magma Imp',
	'7':'Water Imp',
	'8':'Fire Imp',
	'9':'Ooze Imp',
	'10':'Earth Imp',
	'11':'Earth Elemental',
	'12':'Ooze Elemental',
	'13':'Fire Elemental',
	'14':'Water Elemental',
	'15':'Magma Elemental',
	'16':'Steam Elemental',
	'17':'Earth Elemental',
	'18':'Steam Elemental'
};
SFI.tables.MountainousJungleBeast = {
	'3':'Spine Dragon',
	'4':'Wydarr, Boneback',
	'5':'Coppermane Prowler',
	'6':'Bat',
	'7':'Bolt Forager',
	'8':'Coppermane Prowler',
	'9':'Centipede (Giant)',
	'10':'Copperback',
	'11':'Boar',
	'12':'Rat',
	'13':'Zip Bird',
	'14':'Blinefire Vine',
	'15':'Vyderac',
	'16':'Blindfire Carpet',
	'17':'Obsidian Digger',
	'18':'Poison Dart Frog'
};

SFI.tables.Volcano = {
	'3':'Beast',
	'4':'Beast',
	'5':'Beast',
	'6':'Intelligent',
	'7':'Elemental',
	'8':'Elemental',
	'9':'Fuegonauts',
	'10':'Fuegonauts',
	'11':'Fuegonauts',
	'12':'Fuegonauts',
	'13':'Elemental',
	'14':'Elemental',
	'15':'Intelligent',
	'16':'Intelligent',
	'17':'Beast',
	'18':'Beast'
};
SFI.tables.VolcanoIntelligent = {
	'3':'Lizardmen',
	'4':'Nereid',
	'5':'Night Axe',
	'6':'Night Axe',
	'7':'Adventurer',
	'8':'Adventurer',
	'9':'Fuegonauts',
	'10':'Fuegonauts',
	'11':'Fuegonauts',
	'12':'Fuegonauts',
	'13':'Adventurer',
	'14':'Adventurer',
	'15':'Night Axe',
	'16':'Night Axe',
	'17':'Nereid',
	'18':'Lizardmen'
};
SFI.tables.VolcanoElemental = {
	'3':'Water Imp',
	'4':'Ooze Imp',
	'5':'Ooze Imp',
	'6':'Steam Imp',
	'7':'Earth Imp',
	'8':'Fire Imp',
	'9':'Magma Imp',
	'10':'Magma Imp',
	'11':'Magma Elemental',
	'12':'Magma Elemental',
	'13':'Fire Elemental',
	'14':'Earth Elemental',
	'15':'Steam Elemental',
	'16':'Ooze Elemental',
	'17':'Ooze Elemental',
	'18':'Water Elemental'
};
SFI.tables.VolcanoBeast = {
	'3':'Spine Dragon',
	'4':'Obsidian Digger',
	'5':'Obsidian Digger',
	'6':'Wydarr, Boneback',
	'7':'Wydarr, Boneback',
	'8':'Wydarr, Boneback',
	'9':'Boltforager',
	'10':'Rat (Giant)',
	'11':'Centipede (Giant)',
	'12':'Boltforager',
	'13':'Wydarr, Boneback',
	'14':'Wydarr, Boneback',
	'15':'Wydarr, Boneback',
	'16':'Obsidian Digger',
	'17':'Obsidian Digger',
	'18':'Spine Dragon'
};

SFI.tables.Volcanic = {
	'3':'Beast',
	'4':'Beast',
	'5':'Intelligent',
	'6':'Intelligent',
	'7':'Elemental',
	'8':'Elemental',
	'9':'Fuegonauts',
	'10':'Fuegonauts',
	'11':'Night Axe',
	'12':'Night Axe',
	'13':'Elemental',
	'14':'Elemental',
	'15':'Intelligent',
	'16':'Intelligent',
	'17':'Beast',
	'18':'Beast'
};
SFI.tables.VolcanicIntelligent = {
	'3':'Lizardmen',
	'4':'Adventurer',
	'5':'Adventurer',
	'6':'Nereid',
	'7':'Night Axe',
	'8':'Night Axe',
	'9':'Night Axe',
	'10':'Night Axe',
	'11':'Fuegonauts',
	'12':'Fuegonauts',
	'13':'Fuegonauts',
	'14':'Fuegonauts',
	'15':'Nereid',
	'16':'Adventurer',
	'17':'Adventurer',
	'18':'Lizardmen'
};
SFI.tables.VolcanicElemental = {
	'3':'Water Imp',
	'4':'Ooze Imp',
	'5':'Ooze Imp',
	'6':'Steam Imp',
	'7':'Earth Imp',
	'8':'Fire Imp',
	'9':'Magma Imp',
	'10':'Magma Imp',
	'11':'Magma Elemental',
	'12':'Magma Elemental',
	'13':'Fire Elemental',
	'14':'Earth Elemental',
	'15':'Steam Elemental',
	'16':'Ooze Elemental',
	'17':'Ooze Elemental',
	'18':'Water Elemental'
};
SFI.tables.VolcanicBeast = {
	'3':'Spine Dragon',
	'4':'Obsidian Digger',
	'5':'Obsidian Digger',
	'6':'Wydarr, Boneback',
	'7':'Wydarr, Boneback',
	'8':'Wydarr, Boneback',
	'9':'Boltforager',
	'10':'Rat (Giant)',
	'11':'Centipede (Giant)',
	'12':'Boltforager',
	'13':'Wydarr, Boneback',
	'14':'Wydarr, Boneback',
	'15':'Wydarr, Boneback',
	'16':'Obsidian Digger',
	'17':'Obsidian Digger',
	'18':'Spine Dragon'
};

SFI.tables.Ruins = {
	'3':'Intelligent',
	'4':'Intelligent',
	'5':'Intelligent',
	'6':'Elemental',
	'7':'Elemental',
	'8':'Elemental',
	'9':'Beast',
	'10':'Beast',
	'11':'Beast',
	'12':'Beast',
	'13':'Beast',
	'14':'Elemental',
	'15':'Elemental',
	'16':'Elemental',
	'17':'Intelligent',
	'18':'Intelligent'
};
SFI.tables.RuinsIntelligent = {
	'3':'Night Axe',
	'4':'Nereid',
	'5':'Fuegonauts',
	'6':'Fuegonauts',
	'7':'Lizardmen',
	'8':'Lizardmen',
	'9':'Adventurer',
	'10':'Adventurer',
	'11':'Adventurer',
	'12':'Adventurer',
	'13':'Lizardmen',
	'14':'Lizardmen',
	'15':'Fuegonauts',
	'16':'Fuegonauts',
	'17':'Nereid',
	'18':'Night Axe'
};
SFI.tables.RuinsElemental = {
	'3':'Magma Imp',
	'4':'Ooze Imp',
	'5':'Ooze Imp',
	'6':'Steam Imp',
	'7':'Fire Imp',
	'8':'Earth Imp',
	'9':'Earth Imp',
	'10':'Water Imp',
	'11':'Water Elemental',
	'12':'Earth Elemental',
	'13':'Earth Elemental',
	'14':'Fire Elemental',
	'15':'Steam Elemental',
	'16':'Ooze Elemental',
	'17':'Ooze Elemental',
	'18':'Magma Elemental'
};
SFI.tables.RuinsBeast = {
	'3':'Crystal Frog*',
	'4':'Flayfiend*',
	'5':'Duecadre*',
	'6':'Muttering Serpent',
	'7':'Giant Rat@',
	'8':'Singing Golem*',
	'9':'Shadow',
	'10':'Giant Centipede@',
	'11':'Zip Birds@',
	'12':'Orange Sludge',
	'13':'Boar!',
	'14':'Vyderac+',
	'15':'Blindfire Vine',
	'16':'Dire Boar*',
	'17':'Spine Dragon*',
	'18':'Poison Dart Frog'
};

SFI.tables.Village = {
	'3':'Intelligent',
	'4':'Elemental',
	'5':'Beast',
	'6':'Night Axe',
	'7':'Night Axe',
	'8':'Night Axe',
	'9':'Night Axe',
	'10':'Night Axe',
	'11':'Night Axe',
	'12':'Night Axe',
	'13':'Night Axe',
	'14':'Night Axe',
	'15':'Night Axe',
	'16':'Beast',
	'17':'Elemental',
	'18':'Intelligent'
};
SFI.tables.VillageIntelligent = {
	'3':'Lizardmen',
	'4':'Adventurer',
	'5':'Adventurer',
	'6':'Fuegonauts',
	'7':'Fuegonauts',
	'8':'Nereid',
	'9':'Night Axe',
	'10':'Night Axe',
	'11':'Night Axe',
	'12':'Night Axe',
	'13':'Nereid',
	'14':'Fuegonauts',
	'15':'Fuegonauts',
	'16':'Adventurer',
	'17':'Adventurer',
	'18':'Lizardmen'
};
SFI.tables.VillageElemental = {
	'3':'Fire Imp',
	'4':'Steam Imp',
	'5':'Ooze Imp',
	'6':'Ooze Imp',
	'7':'Earth Imp',
	'8':'Earth Imp',
	'9':'Water Imp',
	'10':'Water Imp',
	'11':'Water Elemental',
	'12':'Water Elemental',
	'13':'Earth Elemental',
	'14':'Earth Elemental',
	'15':'Ooze Elemental',
	'16':'Ooze Elemental',
	'17':'Steam Elemental',
	'18':'Fire Elemental'
};
SFI.tables.VillageBeast = {
	'3':'Poison Dart Frog',
	'4':'Poison Dart Frog',
	'5':'Obsidian Digger',
	'6':'Dire Boar',
	'7':'Boltforager',
	'8':'Centipede (Giant)',
	'9':'Bat',
	'10':'Boar',
	'11':'Boar',
	'12':'Rat (Giant)',
	'13':'Centipede (Giant)',
	'14':'Boltforager',
	'15':'Copperback',
	'16':'Centipede (Giant)',
	'17':'Spine Dragon',
	'18':'Spine Dragon'
};
SFI.tables.Adventurer = {
	'1':'Ada',
	'2':'Joni',
	'3':'Charlie',
	'4':'Jack The Jeweler',
	'5':'Audrey',
	'6':'Baxter',
	'7':'Tomas',
	'8':'Eunice',
	'9':'Ruben',
	'10':'Claire',
	'11':'Luther',
	'12':'Marcia',
	'13':'Jenny',
	'14':'Trevor',
	'15':'Bryan',
	'16':'Horatio',
	'17':'Alphonse',
	'18':'Benedict',
	'19':'Cain',
	'20':'Marco'
};
SFI.tables.NPC = {
	'1':'Blade Bone',
	'2':'Tricksy',
	'3':'Fatty',
	'4':'Stone Spear',
	'5':'Boars Head Warrior',
	'6':'Shatter Claw',
	'7':'The Twins',
	'8':'Son of Jus',
	'9':'Duffy',
	'10':'Gold Bone'
};
SFI.tables.Fuegonauts = {
	'3':'1 Giant, 2 Bladeguards, 5 Tricksters, 20 Warriors',
	'4':'4 Bladeguards, 2 Tricksters, 8 Warriors',
	'5':'1 Bladeguard, 2 Tricksters, 2 Combustarinos',
	'6':'6 Combustarinos',
	'7':'2 Tricksters, 8 Warriors, 2 Combustarinos',
	'8':'2 Tricksters, 3 Combustarinos',
	'9':'6 Warriors',
	'10':'1 Trickster, 4 Warriors',
	'11':'1 Trickster, 4 Warriors',
	'12':'2 Combustarinos',
	'13':'4 Combustarinos',
	'14':'1 Trickster, 2 Combustarinos',
	'15':'2 Tricksters, 3 Combustarinos',
	'16':'1 Bladeguard, 2 Tricksters, 2 Combustarinos',
	'17':'2 Bladeguards, 5 Tricksters, 20 Warriors',
	'18':'1 Bladeguard, 6 Tricksters, 28 Warriors'
};
SFI.tables['Night Axe'] = {
	'3':'10 Ogres, 4 Edgeswords, 1 Bonebinder',
	'4':'4 Ogres, 4 Edgeswords, 5 Bonebinders',
	'5':'6 Ogres, 4 Edgeswords, 3 Bonebinders',
	'6':'5 Ogres, 2 Edgeswords, 4 Bonebinders',
	'7':'3 Edgeswords, 3 Bonebinders',
	'8':'4 Ogres, 1 Bonebinder',
	'9':'2 Ogres, 2 Edgeswords',
	'10':'2 Ogres, 1 Bonebinder',
	'11':'2 Ogres',
	'12':'1 Ogre, 2 Edgeswords',
	'13':'1 Ogre, 4 Edgeswords',
	'14':'4 Ogres, 2 Edgeswords, 1 Bonebinder',
	'15':'2 Bonebinders',
	'16':'9 Ogres, 5 Edgeswords, 4 Bonebinders',
	'17':'7 Ogres, 6 Edgeswords, 5 Bonebinders',
	'18':'7 Ogres, 2 Edgeswords, 5 Bonebinders'
};

def three_dice():
    return (randint(1, 6) + randint(1, 6) + randint(1, 6))
