import urllib
import json


head = {u'dyeColor': {u'item': {u'icon': u'dye_20_demonhunter_male', u'tooltipParams': u'item/abyssal-dye', u'id': u'Dye_20', u'displayColor': u'white', u'name': u'Abyssal Dye'}}, u'name': u'Helm of the Wastes', u'tooltipParams': u'item/CpABCJj8wZcBEgcIBBXIbTCJHQFgLbEdS7X5Sx3mFdsNHQnRA0gdZiMGUB2BgcbEMIsSOLwDQABIAVASWARgvANqKwoMCAAQnLfx7YiAgIAaEhsIjf3XjQISBwgEFYUnlLEwixI4AEABWASQAQCAAUaNATYA7BOlAQnRA0itAeQTmN21AX_5Tl24AZ2gyIkKwAErGO_I_OwOUAJYAKAB78j87A6gAa_KjOIOoAGt6uD8BaABsuLl9gGgAdDWzZMGoAGklPOqDw', u'displayColor': u'green', u'transmogItem': {u'icon': u'unique_helm_003_x1_demonhunter_male', u'tooltipParams': u'item/andariels-visage-mCpro', u'id': u'Unique_Helm_003_x1', u'displayColor': u'orange', u'name': u"Andariel's Visage"}, u'setItemsEquipped': [u'Unique_Chest_Set_01_p2', u'Unique_Gloves_Set_01_p2', u'Unique_Helm_Set_01_p2', u'Unique_Shoulder_Set_01_p2', u'Unique_Boots_Set_01_p2', u'Unique_Pants_Set_01_p2'], u'id': u'Unique_Helm_Set_01_p2', u'icon': u'unique_helm_set_01_p2_demonhunter_male'}



class slotItem:
  def __init__(self, item_id, name, icon, displayColor, tooltipParams,
               dyeColor, transmogItem, setItemsEquipped):
    self.item_id = item_id
    self.name = name
    self.icon = icon
    self.display_color = displayColor
    self.tooltip_params = tooltipParams
    self.dye_color = baseItem(dyeColor)
    self.transmog_item = baseItem(transmogItem)
    self.set_items_equipped = setItemsEquipped



class baseItem:
  def __init__(self, item):
    if type(item) is str:
      self.item_id = 'None'
      self.name = 'None'
      self.icon = 'None'
      self.display_color = 'None'
      self.tooltip_params = 'None'
    else:
      self.item_id = item['id']
      self.name = item['name']
      self.icon = item['icon']
      self.display_color = item['displayColor']
      self.tooltip_params = item['tooltipParams']


class itemInstance:
  def __init__(self, item):
    if type(item) is str:
      # set up blank item stats.
      self.id = 'None'
      self.name = 'None'
      self.icon = 'None'
      self.display_color = 'None'
      self.tooltip_params = 'None'
      self.required_level = 0
      self.item_level = 0
      self.stack_size_max = 0
      self.bonus_affixes = 0
      self.bonus_affixes_max = 0
      self.account_bound = False
      self.flavor_text = 'None'
      self.type_name = 'None'
      self.type = {
        "two_handed": False,
        "id": 'None'
      }
      self.damage_range = 'None'
      self.slots = []
      self.attributes= {}
      self.attributes_raw = {}
      self.random_affixes = []
      self.gems = []
      self.socket_effects = []
      self.crafted_by = []
      self.season_required_to_drop = -1
      self.is_season_required_to_drop = False
      self.description = 'None'
      self.block_chance = 'None'
    else:
      # set up actual item stats.
      self.id = item["id"]
      self.name = item["name"]
      self.icon = item["icon"]
      self.display_color = item["displayColor"]
      self.tooltip_params = item["tooltipParams"]
      self.required_level = item["requiredLevel"]
      self.item_level = item["itemLevel"]
      self.stack_size_max = item["stackSizeMax"]
      self.bonus_affixes = item["bonusAffixes"]
      self.bonus_affixes_max = item["bonusAffixesMax"]
      self.account_bound = item["accountBound"]
      self.flavor_text = item["flavorText"]
      self.type_name = item["typeName"]
      # Need to set up type
      #self.type = {
      #  "two_handed": False,
      #  "id": 'None'
      #}
      self.damage_range = item["damageRange"]
      # need to set up slots
      #self.slots = []
      # need to set up attributes
      #self.attributes= {}
      # need to set up attributes_raw
      #self.attributes_raw = {}
      # need to set up random_affixes
      #self.random_affixes = []
      # need to set up gems
      #self.gems = []
      # need to set up socktet_effects
      #self.socket_effects = []
      # need to set up crafted_by
      #self.crafted_by = []
      self.season_required_to_drop = item["seasonRequiredToDrop"]
      self.is_season_required_to_drop = item["isSeasonRequiredToDrop"]
      if item["description"] == None:
        self.description = 'None'
      else:
        self.description = item["description"]
      # need to set up block_chance (What is on non-shields?)
      #self.block_chance = 'None'



def test():
  test_item = slotItem(head['id'], head['name'], head['icon'],
                       head['displayColor'], head['tooltipParams'],
                       head['dyeColor']['item'], head['transmogItem'],
                       head['setItemsEquipped'])
  print test_item.item_id
  print test_item.name
  print test_item.icon
  print test_item.display_color
  print test_item.tooltip_params
  print test_item.dye_color.item_id
  print test_item.dye_color.name
  print test_item.dye_color.icon
  print test_item.dye_color.display_color
  print test_item.dye_color.tooltip_params
  print test_item.transmog_item.item_id
  print test_item.transmog_item.name
  print test_item.transmog_item.icon
  print test_item.transmog_item.display_color
  print test_item.transmog_item.tooltip_params
  print test_item.set_items_equipped
  print "-------------------------"


def get_item_instance_info(item_instance_id):
  API_ITEM_URL_TEMPLATE = 'http://us.battle.net/api/d3/data/item/%s'
  url = API_ITEM_URL_TEMPLATE % item_instance_id
  raw_response = urllib.urlopen(url).read()
  data = json.loads(raw_response)
  return data
