class GamesInventoryInit:
  def init_inventory(self):
    game1 = GamesInventory(
      "GHOST OF TSUSHIMA",
      83,
      "Sucker Punch",
      ("General", "Action Adventure", "Open-World"),
      {"label":"On GameFAQs", "link":"https://www.metacritic.com/game/playstation-4/ghost-of-tsushima"},
      "M")
    
    game2 = GamesInventory(
      "THE LAST OF US PART II",
      94,
      "Naughty Dog",
      "General, Action Adventure, Survival",
      {"label":"On GameFAQs", "link":"https://gamefaqs.gamespot.com/ps4/202466-the-last-of-us-part-ii/cheats"},
      "M")

    game3 = GamesInventory(
      "XENOBLADE CHRONICLES: DEFINITIVE EDITION",
      89,
      "Monolith Soft",
      "Role-Playing, Action RPG",
      {"label":"On GameFAQs", "link":"https://gamefaqs.gamespot.com/ps4/202466-the-last-of-us-part-ii/cheats"},
      "T")
    
    return (game1, game2, game3)


if(__name__ == "__main__"):
  pass
    
