import urllib
import json

API_PROFILE_URL_TEMPLATE = 'http://us.battle.net/api/d3/profile/%s/'
API_HERO_URL_TEMPLATE = 'http://us.battle.net/api/d3/profile/%s/hero/%s'
API_ITEM_URL_TEMPLATE = 'http://us.battle.net/api/d3/data/item/%s'
#http://us.battle.net/api/d3/data/item/COGHsoAIEgcIBBXIGEoRHYQRdRUdnWyzFB2qXu51MA04kwNAAFAKYJMD
#http://us.battle.net/api/d3/data/follower/scoundrel
#http://us.battle.net/api/d3/data/follower/enchantress
#http://us.battle.net/api/d3/data/follower/paladin
#http://us.battle.net/api/d3/data/artisan/blacksmith
#http://us.battle.net/api/d3/data/artisan/jeweler

profile_top_level_keys = ['battleTag', 'paragonLevel', 'paragonLevelHardcore',
                          'paragonLevelSeason', 'paragonLevelSeasonHardcore',
                          'heroes', 'lastHeroPlayed', 'lastUpdated', 'kills',
                          'highestHardcoreLevel', 'timePlayed', 'progression',
                          'fallenHeroes', 'blacksmith', 'jeweler', 'mystic',
                          'blacksmithHardcore', 'jewelerHardcore',
                          'mysticHardcore', 'blacksmithSeasonHardcore',
                          'jewelerSeasonHardcore', 'mysticSeasonHardcore',
                          'seasonalProfiles']
profile_heroes_keys = ['seasonal', 'name', 'level', 'gender', 'dead', 'class',
                       'paragonLevel', 'hardcore', 'id', 'last-updated']
profile_kills_keys = ['hardcoreMonsters', 'monsters', 'elites']
profile_time_played_keys = ['crusader', 'wizard', 'monk', 'barbarian',
                            'witch-doctor', 'demon-hunter']
profile_progression_keys = ['act1', 'act2', 'act3', 'act4', 'act5']
hero_top_level_keys = ['seasonal', 'stats', 'name', 'kills', 'level', 'skills',
                       'gender', 'progression', 'seasonCreated', 'dead', 'id',
                       'followers', 'items', 'paragonLevel', 'hardcore',
                       'class', 'last-updated']

bnet_id = 'gray808-1128'


url = API_PROFILE_URL_TEMPLATE % bnet_id
print "Calling URL: %s" % url
raw_response = urllib.urlopen(url).read()
data = json.loads(raw_response)

print "Battle Tag: %s" % data['battleTag']
print "Paragon Level: %s" % data['paragonLevel']
print "List of Heroes:"
heroes = data['heroes']


#for hero in heroes:
#  print "Name: %s" % hero['name']
#  print "Class: %s" % hero['class']
#  print "Level(Paragon): %s(%s)" % (hero['level'], hero['paragonLevel'])
#  print "Hardcore: %s" % hero['hardcore']
#  print "Seasonal: %s" % hero['seasonal']
#  print "ID: %s" % hero['id']
#  myid = 52087190
#  hero_url = API_HERO_URL_TEMPLATE % (bnet_id, hero['id'])
#  hero_response = urllib.urlopen(hero_url).read()
#  hero_data = json.loads(hero_response)
#  print hero_data['skills']

hero_id = 6470632
hero_url = API_HERO_URL_TEMPLATE % (bnet_id, hero_id)
hero_response = urllib.urlopen(hero_url).read()
hero_data = json.loads(hero_response)

#get seasonal <bool>
seasonal = hero_data['seasonal']

#get stats <dict>
stats = hero_data['stats']
dexterity = hero_data['stats']['dexterity']
intelligence = hero_data['stats']['intelligence']
strength = hero_data['stats']['strength']
vitality = hero_data['stats']['vitality']
healing = hero_data['stats']['healing']
primaryResource = hero_data['stats']['primaryResource']
secondaryResource = hero_data['stats']['secondaryResource']
life = hero_data['stats']['life']
toughness = hero_data['stats']['toughness']
armor = hero_data['stats']['armor']
attackSpeed = hero_data['stats']['attackSpeed']
damage = hero_data['stats']['damage']
critChance = hero_data['stats']['critChance']
critDamage = hero_data['stats']['critDamage']
damageIncrease = hero_data['stats']['damageIncrease']
blockChance = hero_data['stats']['blockChance']
blockAmountMin = hero_data['stats']['blockAmountMin']
blockAmountMax = hero_data['stats']['blockAmountMax']
damageReduction = hero_data['stats']['damageReduction']
lifeSteal = hero_data['stats']['lifeSteal']
lifeOnHit = hero_data['stats']['lifeOnHit']
lifePerKill = hero_data['stats']['lifePerKill']
goldFind= hero_data['stats']['goldFind']
thorns = hero_data['stats']['thorns']
magicFind = hero_data['stats']['magicFind']
arcaneResist = hero_data['stats']['arcaneResist']
fireResist = hero_data['stats']['fireResist']
lightningResist = hero_data['stats']['lightningResist']
poisonResist = hero_data['stats']['poisonResist']
coldResist = hero_data['stats']['coldResist']
physicalResist = hero_data['stats']['physicalResist']

#get name <string>
name = hero_data['name']

#get kills <dict>
kills = hero_data['kills']
elite_kills = kills['elites']

#get level
level = hero_data['level']

#get skills <dict>
## print hero_data['skills']['active'][0]['skill']['name'] # e.g 'Frenzy'
## print hero_data['skills']['active'][0]['rune']['name']  # e.g 'Vanguard'
## print hero_data['skills']['active'][4]['skill']['name'] # e.g 'Call of the Ancients'
## print hero_data['skills']['active'][4]['rune']['name']  # e.g "Ancients' Fury"
##print hero_data['skills']['passive'][0]['skill']['name'] # e.g 'Unforgiving'
##print hero_data['skills']['passive'][1]['skill']['name'] # e.g 'Rampage'
##print hero_data['skills']['passive'][2]['skill']['name'] # e.g 'Superstition'
##print hero_data['skills']['passive'][3]['skill']['name'] # e.g 'Weapons Master'
skills = hero_data['skills']
active = skills['active']
active_skill_list = []
for active_skill in active:
  active_skill_item = {}
  skill = active_skill['skill']
  active_skill_item['skill_name'] = skill['name']
  active_skill_item['skill_level'] = skill['level']
  active_skill_item['skill_description'] = skill['description']
  active_skill_item['skill_tooltipUrl'] = skill['tooltipUrl']
  active_skill_item['skill_categorySlug'] = skill['categorySlug']
  active_skill_item['skill_skillCalcId'] = skill['skillCalcId']
  active_skill_item['skill_simpleDescription'] = skill['simpleDescription']
  active_skill_item['skill_icon'] = skill['icon']
  active_skill_item['skill_slug'] = skill['slug']
  rune = active_skill['rune']
  active_skill_item['rune_slug'] = rune['slug']
  active_skill_item['rune_type'] = rune['type']
  active_skill_item['rune_name'] = rune['name']
  active_skill_item['rune_level'] = rune['level']
  active_skill_item['rune_description'] = rune['description']
  active_skill_item['rune_simpleDescription'] = rune['simpleDescription']
  active_skill_item['rune_tooltipParams'] = rune['tooltipParams']
  active_skill_item['rune_skillCalcId'] = rune['skillCalcId']
  active_skill_item['rune_order'] = rune['order']
  active_skill_list.append(active_skill_item)
passive = skills['passive']
passive_skill_list = []
for passive_skill in passive:
  passive_skill_item = {}
  skill = passive_skill['skill']
  passive_skill_item['slug'] = skill['slug']
  passive_skill_item['name'] = skill['name']
  passive_skill_item['icon'] = skill['icon']
  passive_skill_item['level'] = skill['level']
  passive_skill_item['tooltipUrl'] = skill['tooltipUrl']
  passive_skill_item['description'] = skill['description']
  passive_skill_item['flavor'] = skill['flavor']
  passive_skill_item['skillCalcId'] = skill['skillCalcId']
  passive_skill_list.append(passive_skill_item)

#get gender <int>
gender = hero_data['gender']
if gender == 0:
  gender = "Male"
else:
  gender = "Female"

#get progression <dict>


#get seasonCreated <int>
seasonCreated = hero_data['seasonCreated']

#get dead <bool>
dead = hero_data['dead']
if dead:
  dead = "Yes"
else:
  dead = "No"

#get id <int>
hero_id = hero_data['id']

#get followers <dict>


#get items <dict>
slots = hero_data['items']
item_mainhand = slots['mainHand']
item_head = slots['head']
item_head_id = item_head['id']  ## Use this to get in-depth item info
item_head_name = item_head['name']
item_head_icon = item_head['icon']
item_head_display_color = item_head['displayColor']
item_head_tooltip_params = item_head['tooltipParams']
item_head_transmog_item = item_head['transmogItem']
item_head_transmog_item_id = item_head_transmog_item['id']
item_head_transmog_item_name = item_head_transmog_item['name']
item_head_transmog_item_icon = item_head_transmog_item['icon']
item_head_transmog_item_display_color = item_head_transmog_item['displayColor']
item_head_transmog_item_tooltip_params = item_head_transmog_item['tooltipParams']
#item_head_transmog_item_crafted_by = item_head_transmog_item['craftedBy']
#item_head_crafted_by = item_head['craftedBy']
item_waist = slots['waist']
item_offhand = slots['offHand']
item_neck = slots['neck']
item_shoulders = slots['shoulders']
item_feet = slots['feet']
item_ring_1 = slots['rightFinger']
item_ring_2 = slots['leftFinger']
item_hands = slots['hands']
item_legs = slots['legs']
item_chest = slots['torso']
item_wrist = slots['bracers']
print "Head Item: %s ID(%s)" % (item_head_name, item_head_id)


#get paragonLevel <int>
paragonLevel = hero_data['paragonLevel']

#get hardcore <bool>
hardcore = hero_data['hardcore']
if hardcore:
  hardcore = "Yes"
else:
  hardcore = "No"

#get class <string>
hero_class = hero_data['class'].capitalize()

#get last-updated <int>
last_updated = hero_data['last-updated']





