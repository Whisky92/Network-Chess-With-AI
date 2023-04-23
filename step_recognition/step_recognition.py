"""Based on https://www.chess.com/openings/"""


class StepRecognition:
    """
    A class to contain the most popular openings in chess
    """

    popular_openings = {
        "Sicilian Defense": [[((6, 4), (4, 4)), ((1, 2), (3, 2))], "Sicilian-Defense"],
        "French Defense": [[((6, 4), (4, 4)), ((1, 4), (2, 4))], "French-Defense"],
        "Ruy López Opening": [[((6, 4), (4, 4)), ((1, 4), (3, 4)), ((7, 6), (5, 5)), ((0, 1), (2, 2)),
                               ((7, 5), (3, 1))], "Ruy-Lopez-Opening"],
        "Caro-Kann Defense": [[((6, 4), (4, 4)), ((1, 2), (2, 2))], "Caro-Kann-Defense"],
        "Italian Game": [[((6, 4), (4, 4)), ((1, 4), (3, 4)), ((7, 6), (5, 5)), ((0, 1), (2, 2)),
                          ((7, 5), (4, 2))], "Italian-Game"],
        "Scandinavian Defense": [[((6, 4), (4, 4)), ((1, 3), (3, 3))], "Scandinavian-Defense"],
        "Pirc Defense": [[((6, 4), (4, 4)), ((1, 3), (2, 3)), ((6, 3), (4, 3)), ((0, 6), (2, 5))],
                         "Pirc-Defense-2.d4-Nf6"],
        "Alekhine's Defense": [[((6, 4), (4, 4)), ((0, 6), (2, 5))], "Alekhines-Defense"],
        "King's Gambit": [[((6, 4), (4, 4)), ((1, 4), (3, 4)), ((6, 5), (4, 5))], "Kings-Gambit"],
        "Scotch Game": [[((6, 4), (4, 4)), ((1, 4), (3, 4)), ((7, 6), (5, 5)), ((0, 1), (2, 2)), ((6, 3), (4, 3))],
                        "Scotch-Game"],
        "Vienna Game": [[((6, 4), (4, 4)), ((1, 4), (3, 4)), ((7, 1), (5, 2))], "Vienna-Game"],
        "Queen's Gambit": [[((6, 3), (4, 3)), ((1, 3), (3, 3)), ((6, 2), (4, 2))], "Queens-Gambit"],
        "Slav Defense": [[((6, 3), (4, 3)), ((1, 3), (3, 3)), ((6, 2), (4, 2)), ((1, 2), (2, 2))], "Slav-Defense"],
        "King's Indian Defense": [[((6, 3), (4, 3)), ((0, 6), (2, 5)), ((6, 2), (4, 2)), ((1, 6), (2, 6))],
                                  "Kings-Indian-Defense"],
        "Nimzo-Indian Defense": [[((6, 3), (4, 3)), ((0, 6), (2, 5)), ((6, 2), (4, 2)), ((1, 4), (2, 4)),
                                  ((7, 1), (5, 2)), ((0, 5), (4, 1))], "Nimzo-Indian-Defense"],
        "Queen's Indian Defense": [[((6, 3), (4, 3)), ((0, 6), (2, 5)), ((6, 2), (4, 2)), ((1, 4), (2, 4)),
                                    ((7, 6), (5, 5)), ((1, 1), (2, 1))], "Queens-Indian-Defense"],
        "Catalan Opening": [[((6, 3), (4, 3)), ((0, 6), (2, 5)), ((6, 2), (4, 2)), ((1, 4), (2, 4)), ((6, 6), (5, 6))],
                            "Catalan-Opening"],
        "Bogo-Indian Defense": [[((6, 3), (4, 3)), ((0, 6), (2, 5)), ((6, 2), (4, 2)), ((1, 4), (2, 4)),
                                 ((7, 6), (5, 5)), ((0, 5), (4, 1))], "Bogo-Indian-Defense"],
        "Grünfeld Defense": [[((6, 3), (4, 3)), ((0, 6), (2, 5)), ((6, 2), (4, 2)), ((1, 6), (2, 6)), ((7, 1), (5, 2)),
                              ((1, 3), (3, 3))], "Grunfeld-Defense"],
        "Dutch Defense": [[((6, 3), (4, 3)), ((1, 5), (3, 5))], "Dutch-Defense"],
        "Trompowsky Attack": [[((6, 3), (4, 3)), ((0, 6), (2, 5)), ((7, 2), (3, 6))], "Trompowsky-Attack"],
        "Benko Gambit": [[((6, 3), (4, 3)), ((0, 6), (2, 5)), ((6, 2), (4, 2)), ((1, 2), (3, 2)), ((4, 3), (3, 3)),
                          ((1, 1), (3, 1))], "Benko-Gambit"],
        "London System": [[((6, 3), (4, 3)), ((1, 3), (3, 3)), ((7, 6), (5, 5)), ((0, 6), (2, 5)), ((7, 2), (4, 5))],
                          "London-System"],
        "Benoni Defense: Modern Variation": [[((6, 3), (4, 3)), ((0, 6), (2, 5)), ((6, 2), (4, 2)), ((1, 2), (3, 2)),
                                              ((4, 3), (3, 3)), ((1, 4), (2, 4)), ((7, 1), (5, 2)), ((2, 4), (3, 3)),
                                              ((4, 2), (3, 3)), ((1, 3), (2, 3))],
                                             "Benoni-Defense-Modern-Variation-4.Nc3-exd5-5.cxd5-d6"],
        "Réti Opening": [[((7, 6), (5, 5))], "Reti-Opening"],
        "English Opening": [[((6, 2), (4, 2))], "English-Opening"],
        "Bird's Opening": [[((6, 5), (4, 5))], "Birds-Opening"],
        "King's Indian Attack": [[((7, 6), (5, 5)), ((1, 3), (3, 3)), ((6, 6), (5, 6))], "Kings-Indian-Attack"],
        "King's Fianchetto Opening": [[((6, 6), (5, 6))], "Kings-Fianchetto-Opening"],
        "Nimzowitsch-Larsen Attack": [[((6, 1), (5, 1))], "Nimzowitsch-Larsen-Attack"],
        "Polish Opening": [[((6, 1), (4, 1))], "Polish-Opening"],
        "Grob Opening": [[((6, 6), (4, 6))], "Grob-Opening"]
    }
