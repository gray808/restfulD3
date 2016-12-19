
# -*- coding: UTF-8 -*-

import d3profile
import d3hero
import d3item




def display_hero(hero):
  print "Hero Information:"
  print "ID: %s" % hero.id
  print "Name: %s" % hero.name
  print "Class: %s" % hero.char_class
  print "Gender: %s" % hero.gender
  print "Level: %s" % hero.level
  print "Paragon Level: %s" % hero.paragon_level
  print "Hardcore: %s" % hero.hardcore
  print "Seasonal: %s" % hero.seasonal
  print "Season Created: %s" % hero.season_created
  print "Skills:"
  for index, skill in enumerate(hero.active_skills):
    a_skill = hero.active_skills[index].skill
    a_rune = hero.active_skills[index].rune
    print "Active skill %s:" % index
    print "    Slug: %s" % a_skill.slug
    print "    Name: %s" % a_skill.name
    print "    Icon: %s" % a_skill.icon
    print "    Level: %s" % a_skill.level
    print "    Category: %s" % a_skill.category
    print "    Tooltip URL: %s" % a_skill.tooltip_url
    print "    Description: %s" % a_skill.description
    print "    Simple Description: %s" % a_skill.simple_description
    print "    Calc ID: %s" % a_skill.calc_id
    print "        Rune:"
    print "            Slug: %s" % a_rune.slug
    print "            Type: %s" % a_rune.type
    print "            Name: %s" % a_rune.name
    print "            Level: %s" % a_rune.level
    print "            Description: %s" % a_rune.description
    print "            Simple Description: %s" % a_rune.simple_description
    print "            Tooltip Params: %s" % a_rune.tooltip_params
    print "            Skill Calc ID: %s" % a_rune.skill_calc_id
    print "            Order: %s" % a_rune.order
  for index, skill in enumerate(hero.passive_skills):
    p_skill = hero.passive_skills[index]
    print "Passive Skill %s:" % index
    print "    Slug: %s" % p_skill.slug
    print "    Name: %s" % p_skill.name
    print "    Icon: %s" % p_skill.icon
    print "    Level: %s" % p_skill.level
    print "    Tooltip URL: %s" % p_skill.tooltip_url
    print "    Description: %s" % p_skill.description
    #print "    Flavor Text: %s" % p_skill.flavor
    print "    Skill Calc ID: %s" % p_skill.calc_id
  print "Items:"
  for slot in hero.slots:
    item = hero.slots[slot]
    print "   %s: " % slot
    print "       ID: %s" % item.item_id
    print "       Name: %s" % item.name
    print "       Icon: %s" % item.icon
    print "       Display Color: %s" % item.display_color
    print "       Tooltip Params: %s" % item.tooltip_params
    print "       Dye Color:"
    print "           ID: %s" % item.dye_color.item_id
    print "           Name: %s" % item.dye_color.name
    print "           Icon: %s" % item.dye_color.icon
    print "           Display Color: %s" % item.dye_color.display_color
    print "           Tooltip Params: %s" % item.dye_color.tooltip_params
    print "       Transmog Item:"
    print "           ID: %s" % item.transmog_item.item_id
    print "           Name: %s" % item.transmog_item.name
    print "           Icon: %s" % item.transmog_item.icon
    print "           Display Color: %s" % item.transmog_item.display_color
    print "           Tooltip Params: %s" % item.transmog_item.tooltip_params
    print "       Set Items Equipped:"
    if item.set_items_equipped is list:
      for equipped_item in item.set_items_equipped:
        print "       :   %s" % equipped_item
    else:
      print "           None"
    print "----------------------------------------------------"



  print "Followers:"
  print "    [[ Followers go here ]]"
  print "Stats:"
  print "    [[ Stats go here ]]"
  print "Kills:"
  print "    [[ Kills go here ]]"
  print "Progression:"
  print "    [[ Progression goes here ]]"
  print "Dead: %s" % hero.dead
  print "Last Updated: %s" % hero.last_updated


def display_profile(profile):
  print "Character Information:"
  print "BattleTag: %s" % profile.battle_tag
  print "Paragon Level: %s" % profile.paragon_level
  print "Hardcore Paragon Level: %s" % profile.paragon_level_hardcore
  print "Seasonal Paragon Level: %s" % profile.paragon_level_season
  print "Hardcore Seasonal Paragon Level: %s" % profile.paragon_level_season_hardcore
  print "Heroes:"
  for hero in profile.heroes:
    print "    %s" % hero.name
    print "        Seasonal: %s" % hero.seasonal
    print "        Level: %s" % hero.level
    print "        Gender: %s" % hero.gender
    print "        Dead: %s" % hero.dead
    print "        Class: %s" % hero.pc_class
    print "        Paragon Level: %s" % hero.paragon_level
    print "        Hardcore: %s" % hero.hardcore
    print "        ID: %s" % hero.id
    print "        Last Updated: %s" % hero.last_updated
  print "Last Hero Played: %s" % profile.last_hero_played
  print "Last Updated: %s" % profile.last_updated
  print "Highest Hardcore Level Achieved: %s" % profile.highest_hardcore_level
  print "Kills:"
  print "     Monsters: %s" % profile.kills.monsters
  print "     Elites: %s" % profile.kills.elites
  print "     Monsters (Hardcore): %s" % profile.kills.hardcore_monsters
  print "Time Played:"
  print "     Barbarian: %s" % profile.time_played.barbarian
  print "     Crusader: %s" % profile.time_played.crusader
  print "     Demon Hunter: %s" % profile.time_played.demon_hunter
  print "     Monk: %s" % profile.time_played.monk
  print "     Witch Doctor: %s" % profile.time_played.witch_doctor
  print "     Wizard: %s" % profile.time_played.wizard
  print "Quest Progression:"
  print "     Act 1: %s" % profile.progression.act1
  print "     Act 2: %s" % profile.progression.act2
  print "     Act 3: %s" % profile.progression.act3
  print "     Act 4: %s" % profile.progression.act4
  print "     Act 5: %s" % profile.progression.act5
  print "Fallen Heros:"
  if profile.fallen_heroes == []:
    print "    None"
  else:
    print "    Fallen Heroes Info Goes here"
  print "Blacksmith:"
  print "     Slug: %s" % profile.blacksmith.slug
  print "     Level: %s" % profile.blacksmith.level
  print "     Step Current: %s" % profile.blacksmith.step_current
  print "     Step Max: %s" % profile.blacksmith.step_max
  print "Jeweler:"
  print "     Slug: %s" % profile.jeweler.slug
  print "     Level: %s" % profile.jeweler.level
  print "     Step Current: %s" % profile.jeweler.step_current
  print "     Step Max: %s" % profile.jeweler.step_max
  print "Mystic:"
  print "     Slug: %s" % profile.mystic.slug
  print "     Level: %s" % profile.mystic.level
  print "     Step Current: %s" % profile.mystic.step_current
  print "     Step Max: %s" % profile.mystic.step_max
  print "Blacksmith (Hardcore):"
  print "     Slug: %s" % profile.blacksmith_hardcore.slug
  print "     Level: %s" % profile.blacksmith_hardcore.level
  print "     Step Current: %s" % profile.blacksmith_hardcore.step_current
  print "     Step Max: %s" % profile.blacksmith_hardcore.step_max
  print "Jeweler (Hardcore):"
  print "     Slug: %s" % profile.jeweler_hardcore.slug
  print "     Level: %s" % profile.jeweler_hardcore.level
  print "     Step Current: %s" % profile.jeweler_hardcore.step_current
  print "     Step Max: %s" % profile.jeweler_hardcore.step_max
  print "Mystic (Hardcore):"
  print "     Slug: %s" % profile.mystic_hardcore.slug
  print "     Level: %s" % profile.mystic_hardcore.level
  print "     Step Current: %s" % profile.mystic_hardcore.step_current
  print "     Step Max: %s" % profile.mystic_hardcore.step_max
  print "Blacksmith (Hardcore, Seasonal):"
  print "     Slug: %s" % profile.blacksmith_season_hardcore.slug
  print "     Level: %s" % profile.blacksmith_season_hardcore.level
  print "     Step Current: %s" % profile.blacksmith_season_hardcore.step_current
  print "     Step Max: %s" % profile.blacksmith_season_hardcore.step_max
  print "Jeweler(Hardcore, Seasonal):"
  print "     Slug: %s" % profile.jeweler_season_hardcore.slug
  print "     Level: %s" % profile.jeweler_season_hardcore.level
  print "     Step Current: %s" % profile.jeweler_season_hardcore.step_current
  print "     Step Max: %s" % profile.jeweler_season_hardcore.step_max
  print "Mystic(Hardcore, Seasonal):"
  print "     Slug: %s" % profile.mystic_season_hardcore.slug
  print "     Level: %s" % profile.mystic_season_hardcore.level
  print "     Step Current: %s" % profile.mystic_season_hardcore.step_current
  print "     Step Max: %s" % profile.mystic_season_hardcore.step_max
  print "Seasonal Profiles:"
  for sprofile in profile.seasonal_profiles:
    print "    Season ID: %s" % sprofile.season_id
    print "        Time Played:"
    print "            Barbarian: %s" % sprofile.time_played.barbarian
    print "            Crusader: %s" % sprofile.time_played.crusader
    print "            Wizard: %s" % sprofile.time_played.wizard
    print "            Monk: %s" % sprofile.time_played.monk
    print "            Witch Doctor: %s" % sprofile.time_played.witch_doctor
    print "            Demon Hunter: %s" % sprofile.time_played.demon_hunter
    print "        Progression:"
    print "            Act 1: %s" % sprofile.progression.act1
    print "            Act 2: %s" % sprofile.progression.act2
    print "            Act 3: %s" % sprofile.progression.act3
    print "            Act 4: %s" % sprofile.progression.act4
    print "            Act 5: %s" % sprofile.progression.act5
    print "        Kills:"
    print "            Hardcore Monsters: %s" % sprofile.kills.hardcore_monsters
    print "            Monsters: %s" % sprofile.kills.monsters
    print "            Elites: %s" % sprofile.kills.elites
    print "        Hardcore Paragon Level: %s" % sprofile.paragon_level_hardcore
    print "        Highest Hardcore Level: %s" % sprofile.highest_harcore_level
    print "        Paragon Level: %s" % sprofile.paragon_level














bnet_id = 'gray808-1128'
char_id = '6470632'

#profile = d3profile.Profile(bnet_id)
#display_profile(profile)
hero = d3hero.Hero(bnet_id, char_id)
display_hero(hero)