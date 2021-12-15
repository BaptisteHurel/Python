class Stat:
    def __init__(self, player: str, season: int, nb_point: int ) -> None:
        self.player = player
        self.season = season
        self.nb_point = nb_point

    @staticmethod
    def to_dict(player: str, season: int, nb_point: int) -> dict:
        return dict(player=player, season=season, nb_point=nb_point)