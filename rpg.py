class RpgCommands:
    def party(party):
        newparty = {
            'name': party[0],
            'server': party[1]
        }
        name = newparty['name']
        print(f'criada party: {name}')

    def character(character, player):
        newcharacter = {
            'player': player,
            'name': character[0],
            'race': character[1],
            'level': character[2],
            'health': character[3],
            'proficiency': character[4],
            'strength': character[5],
            'dexterity': character[6],
            'constitution': character[7],
            'intelligence': character[8],
            'wisdom': character[9],
            'charisma': character[10],
            'sheet_url': character[11],
        }
        return "Character created: " + newcharacter['name']