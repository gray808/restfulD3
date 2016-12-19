import urllib
import json



class Profile:
  def __init__(self, bnet_id):
    data = get_profile_info(bnet_id)
    # Now initialize the class using the data pulled from the REST response
    self.battle_tag = data['battleTag']
    self.paragon_level = data['paragonLevel']
    self.paragon_level_hardcore = data['paragonLevelHardcore']
    self.paragon_level_season = data['paragonLevelSeason']
    self.paragon_level_season_hardcore = data['paragonLevelSeasonHardcore']
    self.heroes = []
    for hero in data['heroes']:
      seasonal = hero['seasonal']
      name = hero['name']
      level = hero['level']
      gender = hero['gender']
      dead = hero['dead']
      pc_class = hero['class']
      plvl = hero['paragonLevel']
      hardcore = hero['hardcore']
      pid = hero['id']
      last = hero['last-updated']
      profile_hero = profileHero(seasonal, name, level, gender, dead, pc_class,
                                 plvl, hardcore, pid, last)
      self.heroes.append(profile_hero)
    self.last_hero_played = data['lastHeroPlayed']
    self.last_updated = data['lastUpdated']
    self.highest_hardcore_level = data['highestHardcoreLevel']
    self.kills = profileKills(data['kills']['monsters'],
                              data['kills']['elites'],
                              data['kills']['hardcoreMonsters'])
    tmp = data['timePlayed']
    self.time_played = profileTimePlayed(tmp['barbarian'],
                                         tmp['crusader'],
                                         tmp['demon-hunter'],
                                         tmp['monk'],
                                         tmp['witch-doctor'],
                                         tmp['wizard'])
    tmp = data['progression']
    self.progression = profileProgression(tmp['act1'],
                                          tmp['act2'],
                                          tmp['act3'],
                                          tmp['act4'],
                                          tmp['act5'])
    self.fallen_heroes = data['fallenHeroes']
    tmp = data['blacksmith']
    self.blacksmith = profileNPC(tmp['slug'],
                                 tmp['level'],
                                 tmp['stepCurrent'],
                                 tmp['stepMax'])
    tmp = data['jeweler']
    self.jeweler = profileNPC(tmp['slug'],
                              tmp['level'],
                              tmp['stepCurrent'],
                              tmp['stepMax'])
    tmp = data['mystic']
    self.mystic = profileNPC(tmp['slug'],
                             tmp['level'],
                             tmp['stepCurrent'],
                             tmp['stepMax'])
    if data.has_key('blacksmithHardcore'):
      tmp = data['blacksmithHardcore']
      self.blacksmith_hardcore = profileNPC(tmp['slug'],
                                            tmp['level'],
                                            tmp['stepCurrent'],
                                            tmp['stepMax'])
    else:
      self.blacksmith_hardcore = profileNPC('None', 0, 0, 0)
    if data.has_key('jewelerHardcore'):
      tmp = data['jewelerHardcore']
      self.jeweler_hardcore = profileNPC(tmp['slug'],
                                         tmp['level'],
                                         tmp['stepCurrent'],
                                         tmp['stepMax'])
    else:
      self.jeweler_hardcore = profileNPC('None', 0, 0, 0)
    if data.has_key('mysticHardcore'):
      tmp = data['mysticHardcore']
      self.mystic_hardcore = profileNPC(tmp['slug'],
                                        tmp['level'],
                                        tmp['stepCurrent'],
                                        tmp['stepMax'])
    else:
      self.mystic_hardcore = profileNPC('None', 0, 0, 0)
    if data.has_key('blacksmithSeasonHardcore'):
      tmp = data['blacksmithSeasonHardcore']
      self.blacksmith_season_hardcore = profileNPC(tmp['slug'],
                                                   tmp['level'],
                                                   tmp['stepCurrent'],
                                                   tmp['stepMax'])
    else:
      self.blacksmith_season_hardcore = profileNPC('None', 0, 0, 0)
    if data.has_key('jewelerSeasonHardcore'):
      tmp = data['jewelerSeasonHardcore']
      self.jeweler_season_hardcore = profileNPC(tmp['slug'],
                                                tmp['level'],
                                                tmp['stepCurrent'],
                                                tmp['stepMax'])
    else:
      self.jeweler_season_hardcore = profileNPC('None', 0, 0, 0)
    if data.has_key('mysticSeasonHardcore'):
      tmp = data['mysticSeasonHardcore']
      self.mystic_season_hardcore = profileNPC(tmp['slug'],
                                               tmp['level'],
                                               tmp['stepCurrent'],
                                               tmp['stepMax'])
    else:
      self.mystic_season_hardcore = profileNPC('None', 0, 0, 0)
    self.seasonal_profiles = []
    for profile in data['seasonalProfiles']:
      cur_profile = data['seasonalProfiles'][profile]
      season_id = cur_profile['seasonId']
      tmp = cur_profile['timePlayed']
      time_played = {
        'crusader': tmp['crusader'],
        'wizard': tmp['wizard'],
        'monk': tmp['monk'],
        'barbarian': tmp['barbarian'],
        'witch-doctor': tmp['witch-doctor'],
        'demon-hunter': tmp['demon-hunter']
      }
      tmp = cur_profile['progression']
      progression = {
        'act1': tmp['act1'],
        'act2': tmp['act2'],
        'act3': tmp['act3'],
        'act4': tmp['act4'],
        'act5': tmp['act5']
      }
      tmp = cur_profile['kills']
      kills = {
        'hardcoreMonsters': tmp['hardcoreMonsters'],
        'monsters': tmp['monsters'],
        'elites': tmp['elites']
      }
      paragon_level_hardcore = cur_profile['paragonLevelHardcore']
      highest_hardcore_level = cur_profile['highestHardcoreLevel']
      paragon_level = cur_profile['paragonLevel']
      seasonal_profile = seasonalProfile(season_id, time_played, progression,
                                         kills, paragon_level_hardcore,
                                         highest_hardcore_level, paragon_level)
      self.seasonal_profiles.append(seasonal_profile)




class profileHero:
  def __init__(self, seasonal, name, level, gender, dead, pc_class, plvl,
               hardcore, pid, last):
    self.seasonal = seasonal
    self.name = name
    self.level = level
    self.gender = gender
    self.dead = dead
    self.pc_class = pc_class
    self.paragon_level = plvl
    self.hardcore = hardcore
    self.id = pid
    self.last_updated = last


class profileKills:
  def __init__(self, monster_kills, elite_kills, hc_kills):
    self.monsters = monster_kills
    self.elites = elite_kills
    self.hardcore_monsters = hc_kills


class profileTimePlayed:
  def __init__(self, tp_barb, tp_sader, tp_dh, tp_monk, tp_wd, tp_wiz):
    self.barbarian = tp_barb
    self.crusader = tp_sader
    self.demon_hunter = tp_dh
    self.monk = tp_monk
    self.witch_doctor = tp_wd
    self.wizard = tp_wiz


class profileProgression:
  def __init__(self, a1, a2, a3, a4, a5):
    self.act1 = a1
    self.act2 = a2
    self.act3 = a3
    self.act4 = a4
    self.act5 = a5


class profileNPC:
  def __init__(self, slug, level, stepCurrent, stepMax):
    self.slug = slug
    self.level = level
    self.step_current = stepCurrent
    self.step_max = stepMax


class seasonalProfile:
  def __init__(self, season_id, time_played, prog, kills, plvlhc, hhclvl, plvl):
    self.season_id = season_id
    self.time_played = profileTimePlayed(time_played['barbarian'],
                                         time_played['crusader'],
                                         time_played['wizard'],
                                         time_played['monk'],
                                         time_played['witch-doctor'],
                                         time_played['demon-hunter'])
    self.progression = profileProgression(prog['act1'],
                                          prog['act2'],
                                          prog['act3'],
                                          prog['act4'],
                                          prog['act5'])
    self.kills = profileKills(kills['hardcoreMonsters'],
                              kills['monsters'],
                              kills['elites'])
    self.paragon_level_hardcore = plvlhc
    self.highest_harcore_level = hhclvl
    self.paragon_level = plvl


def get_profile_info(bnet_id):
  ## Call out to API, decode JSON
  API_PROFILE_URL_TEMPLATE = 'http://us.battle.net/api/d3/profile/%s/'
  url = API_PROFILE_URL_TEMPLATE % bnet_id
  raw_response = urllib.urlopen(url).read()
  data = json.loads(raw_response)
  return data

