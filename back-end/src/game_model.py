class GamesInventory:
  title = None
  metascore = None
  developer = None
  genre = None
  cheats = None
  rating = None

  def __init__(self, title, metascore, developer, genre, cheats, rating):
    self.title = title
    self.metascore = metascore
    self.developer = developer
    self.genre = genre
    self.cheats = cheats
    self.rating = rating