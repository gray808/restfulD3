import urllib
import json
import d3item as d3item

class Hero:
  def __init__(self, bnet_id, char_id):
    data = get_hero_info(bnet_id, char_id)
    # Now initialize the class using the data pulled from the REST response
    self.id = data['id']
    self.name = data['name']
    self.char_class = data['class']
    self.gender = data['gender']
    self.level = data['level']
    self.paragon_level = data['paragonLevel']
    self.hardcore = data['hardcore']
    self.seasonal = data['seasonal']
    self.season_created = data['seasonCreated']
    # Skills
    self.active_skills = []
    for a_skill in data['skills']['active']:
      s = a_skill['skill']
      if s.has_key('categorySlug'):
        slug = s['categorySlug']
      else:
        slug = "\'None\'"
      skill_info = {
        'slug': s['slug'],
        'name': s['name'],
        'icon': s['icon'],
        'level': s['level'],
        'category': slug,
        'tooltip_url': s['tooltipUrl'],
        'description': s['description'],
        'simple_description': s['simpleDescription'],
        'skill_calc_id': s['skillCalcId']
      }
      skill = Skill(skill_info)
      r = a_skill['rune']
      rune_info = {
        'slug': r['slug'],
        'type': r['type'],
        'name': r['name'],
        'level': r['level'],
        'description': r['description'],
        'simple_description': r['simpleDescription'],
        'tooltip_params': r['tooltipParams'],
        'skill_calc_id': r['skillCalcId'],
        'order': r['order']
      }
      rune = Rune(rune_info)
      active_skill = ActiveSkill(skill, rune)
      self.active_skills.append(active_skill)
    self.passive_skills = []
    for p_skill in data['skills']['passive']:
      s = p_skill['skill']
      if s.has_key('simpleDescription'):
        simple_description = s['simpleDescription']
      else:
        simple_description = "None"
      skill_info = {
        'slug': s['slug'],
        'name': s['name'],
        'icon': s['icon'],
        'level': s['level'],
        'tooltip_url': s['tooltipUrl'],
        'description': s['description'],
        'simple_description': simple_description,
        'flavor': s['flavor'],
        'skill_calc_id': s['skillCalcId']
      }
      skill = Skill(skill_info)
      self.passive_skills.append(skill)
    # Items
    print "Slots set."
    self.slots = {'head': None, 'torso': None, 'feet': None, 'hands': None,
             'shoulders': None, 'legs': None, 'bracers': None,
             'mainHand': None, 'offHand': None, 'waist': None,
             'rightFinger': None, 'leftFinger': None, 'neck': None}
    item_list = data['items']
    print "item_list:  %s" % item_list
    for slot in self.slots:
      print "in slot"
      info = item_list[slot]
      if info.has_key('transmogItem'):
        transmog_item = info['transmogItem']
      else:
        transmog_item = "\'None\'"
      if info.has_key('dyeColor'):
        dyecolor_item = info['dyeColor']['item']
      else:
        dyecolor_item = "\'None\'"
      if info.has_key('setItemsEquipped'):
        set_items = info['setItemsEquipped']
      else:
        set_items = "\'None\'"
      self.slots[slot] = d3item.slotItem(info['id'], info['name'],
                                         info['icon'], info['displayColor'],
                                         info['tooltipParams'],
                                         dyecolor_item,
                                         transmog_item,
                                         set_items)
    # Followers
    self.followers = {'templar': None, 'scoundrel': None, 'enchantress': None}
    for follower in data['followers']:
      self.followers[follower] = Follower(follower)
    # Stats
    stats = Stats(data['stats'])
    # Kills
    # Are we missing something here??

    # Progression
    self.dead = data['dead']
    self.last_updated = data['last-updated']

  def test(self):
    print "Testing....."
    #print "self.active_skills: %s" % self.active_skills
    #print "Type: %s" % type(self.active_skills)
    #print "self.active_skills[0]: %s" % self.active_skills[0]
    #print "Type: %s" % type(self.active_skills[0])
    #print "self.active_skills[0].skill: %s" % self.active_skills[0].skill
    #print "Type: %s" % type(self.active_skills[0].skill)
    #print "self.active_skills[0].skill.name: %s" % self.active_skills[0].skill.name
    #print "Type: %s" % type(self.active_skills[0].skill.name)




class Skill:
  def __init__(self, skill_info):
    self.slug = skill_info['slug']
    self.name = skill_info['name']
    self.icon = skill_info['icon']
    self.level = skill_info['level']
    if skill_info.has_key('category_slug'):
      self.category = skill_info['category_slug']
    else:
      self.category = "None"
    self.tooltip_url = skill_info['tooltip_url']
    self.description = skill_info['description']
    if skill_info.has_key('simple_description'):
      self.simple_description = skill_info['simple_description']
    else:
      self.simple_description = 'None'
    self.calc_id = skill_info['skill_calc_id']

class Rune:
  def __init__(self, rune_info):
    self.slug = rune_info['slug']
    self.type = rune_info['type']
    self.name = rune_info['name']
    self.level = rune_info['level']
    self.description = rune_info['description']
    self.simple_description = rune_info['simple_description']
    self.tooltip_params = rune_info['tooltip_params']
    self.skill_calc_id = rune_info['skill_calc_id']
    self.order = rune_info['order']

class ActiveSkill:
  def __init__(self, skill, rune):
    self.skill = skill
    self.rune = rune

class PassiveSkill:
  def __init__(self, skill):
    self.skill = skill

class Follower:
  def __init__(self, follower):
    self.slug = follower['slug']
    self.level = follower['level']
    self.items = {'special': None, 'mainHand': None, 'offHand': None,
                  'rightFinger': None, 'leftFinger': None, 'neck': None}
    for item in self.items:
      f_item = follower["items"][item]
      self.items[item] = d3item.baseItem(f_item)
    f_stat = follower['stats']
    self.stats = FollowerStats(f_stat['goldFind'], f_stat['magicFind'],
                               f_stat['experienceBonus'])
    f_skills = follower['skills']
    self.skills = []
    for skill in f_skills:
      s = f_skills[skill]
      skill_info = {
        'slug': s['slug'],
        'name': s['name'],
        'icon': s['icon'],
        'level': s['level'],
        'tooltip_url': s['tooltipUrl'],
        'description': s['description'],
        'simple_description': s['simpleDescription'],
        'skill_calc_id': s['skillCalcId']
      }
      self.skills.append(Skill(skill_info))

class Stats:
  def __init__(self, stat_info):
    self.dexterity = stat_info['dexterity']
    self.toughness = stat_info['toughness']
    self.life_steal = stat_info['lifeSteal']
    self.intelligence = stat_info['intelligence']
    self.block_amount_min = stat_info['blockAmountMin']
    self.arcane_resist = stat_info['arcaneResist']
    self.fire_resist = stat_info['fireResist']
    self.secondary_resource = stat_info['secondaryResource']
    self.damage_increase = stat_info['damageIncrease']
    self.strength = stat_info['strength']
    self.block_amount_max = stat_info['blockAmountMax']
    self.armor = stat_info['armor']
    self.damage = stat_info['damage']
    self.block_chance = stat_info['blockChance']
    self.life = stat_info['life']
    self.crit_chance = stat_info['critChance']
    self.damage_reduction = stat_info['damageReduction']
    self.vitality = stat_info['vitality']
    self.gold_find = stat_info['goldFind']
    self.healing = stat_info['healing']
    self.lightning_resist = stat_info['lightningResist']
    self.magic_find = stat_info['magicFind']
    self.poison_resist = stat_info['poisonResist']
    self.cold_resist = stat_info['coldResist']
    self.life_per_kill = stat_info['lifePerKill']
    self.crit_damage = stat_info['critDamage']
    self.primary_resource = stat_info['primaryResource']
    self.physical_resist = stat_info['physicalResist']
    self.attack_speed = stat_info['attackSpeed']
    self.thorns = stat_info['thorns']
    self.life_on_hit = stat_info['lifeOnHit']





class FollowerStats:
  def __init__(self, gold, magic, xp_bonus):
    self.gold_find = gold
    self.magic_find = magic
    self.xp_bonus = xp_bonus



def get_hero_info(bnet_id, char_id):
  ## Call out to API, decode JSON
  API_HERO_URL_TEMPLATE = 'http://us.battle.net/api/d3/profile/%s/hero/%s'
  url = API_HERO_URL_TEMPLATE % (bnet_id, char_id)
  raw_response = urllib.urlopen(url).read()
  data = json.loads(raw_response)
  return data

"""
results = []
for level1 in data:
  if type(data[level1]) is dict:
    for level2 in data[level1]:
      if type(data[level1][level2]) is dict:
        for level3 in data[level1][level2]:
          if type(data[level1][level2][level3]) is dict:
            for level4 in data[level1][level2][level3]:
              if type(data[level1][level2][level3][level4]) is dict:
                result = "DEEPER THAN LEVEL 4"
              else:
                result = "data[\'%s\'][\'%s\'][\'%s\'][\'%s\'] (%s)" % (level1,level2,level3,level4,type(level4))
                results.append(result)
            else:
              result = "data[\'%s\'][\'%s\'][\'%s\'][\'%s\'] (%s)" % (level1,level2,level3,level4,type(level4))
              results.append(result)
          else:
            result = "data[\'%s\'][\'%s\'][\'%s\'] (%s)" % (level1,level2,level3,type(level3))
            results.append(result)
      else:
        result = "data[\'%s\'][\'%s\'] (%s)" % (level1, level2, type(level2))
        results.append(result)
  else:
    result = "data[\'%s\'] (%s)" % (level1, type(level1))
    results.append(result)
"""



