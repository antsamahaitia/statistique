import json

def getData(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    data = data['teamTableStats']
    return data    

# data = getData('attaque-domicile.json')
all_query = []
all_team = []
# for line in data:
#     query = f"INSERT INTO statistique (id_equipe, buts, tirs_pm, carton_j, carton_r, possession, passes_reussies, aeriens_gagnes, note) VALUES ('EQU{line['teamId']}', {line['goal']}, {line['shotsPerGame']}, {line['yellowCard']}, {line['redCard']}, {line['possession']}, {line['passSuccess']}, {line['aerialWonPerGame']}, {line['rating']});"
#     # query = f"INSERT INTO competion VALUES ('COMP{line['tournamentId']}', '{line['tournamentName']}');"
#     # query = f"INSERT INTO equipe VALUES ('EQU{line['teamId']}', '{line['name']}', 'COMP{line['tournamentId']}');"
#     all_query.append(query)


# data = getData('attaque-exterieur.json')
# for line in data:
#     query = f"INSERT INTO statistique (id_equipe, buts, tirs_pm, carton_j, carton_r, possession, passes_reussies, aeriens_gagnes, note) VALUES ('EQU{line['teamId']}', {line['goal']}, {line['shotsPerGame']}, {line['yellowCard']}, {line['redCard']}, {line['possession']}, {line['passSuccess']}, {line['aerialWonPerGame']}, {line['rating']});"
#     # query = f"INSERT INTO competion VALUES ('COMP{line['tournamentId']}', '{line['tournamentName']}');"
#     # query = f"INSERT INTO equipe VALUES ('EQU{line['teamId']}', '{line['name']}', 'COMP{line['tournamentId']}');"
#     all_query.append(query)

# data = getData('attaque-general.json')
# for line in data:
#     query = f"INSERT INTO statistique (id_equipe, buts, tirs_pm, carton_j, carton_r, possession, passes_reussies, aeriens_gagnes, note) VALUES ('EQU{line['teamId']}', {line['goal']}, {line['shotsPerGame']}, {line['yellowCard']}, {line['redCard']}, {line['possession']}, {line['passSuccess']}, {line['aerialWonPerGame']}, {line['rating']});"
#     # query = f"INSERT INTO competion VALUES ('COMP{line['tournamentId']}', '{line['tournamentName']}');"
#     # query = f"INSERT INTO equipe VALUES ('EQU{line['teamId']}', '{line['name']}', 'COMP{line['tournamentId']}');"
#     all_query.append(query)

data = getData('attaque-domicile.json')
for line in data:
    # query = f"INSERT INTO statistique_defense (id_equipe, tirs_pm, tacles_pm, interceptions_pm, fautes_pm, hors_jeux_pm, categorie, note) VALUES ('EQU{line['teamId']}', {line['shotsConcededPerGame']}, {line['tacklePerGame']}, {line['interceptionPerGame']}, {line['foulsPerGame']}, {line['offsideGivenPerGame']}, 'domicil', {line['rating']});"
    # query = f"INSERT INTO statistique_general (id_equipe, buts, tirs_pm, carton_j, carton_r, possession, passes_reussies, aeriens_gagnes, categorie, note) VALUES ('EQU{line['teamId']}', {line['goal']}, {line['shotsPerGame']}, {line['yellowCard']}, {line['redCard']}, {line['possession']}, {line['passSuccess']}, {line['aerialWonPerGame']}, 'domicil', {line['rating']});"
    query = f"INSERT INTO statistique_attaque (id_equipe, tirs_pm, tirs_ca_pm, dribbles_pm, fautes_subies_pm, categorie, note) VALUES ('EQU{line['teamId']}', {line['shotsPerGame']}, {line['shotOnTargetPerGame']}, {line['dribbleWonPerGame']}, {line['foulGivenPerGame']}, 'domicil', {line['rating']});"
    # query = f"INSERT INTO competion VALUES ('COMP{line['tournamentId']}', '{line['tournamentName']}');"
    # query = f"INSERT INTO equipe VALUES ('EQU{line['teamId']}', '{line['name']}', 'COMP{line['tournamentId']}');"
    # all_query.append(query)
    print(query)
    
data = getData('attaque-exterieur.json')
for line in data:
    # query = f"INSERT INTO statistique_defense (id_equipe, tirs_pm, tacles_pm, interceptions_pm, fautes_pm, hors_jeux_pm, categorie, note) VALUES ('EQU{line['teamId']}', {line['shotsConcededPerGame']}, {line['tacklePerGame']}, {line['interceptionPerGame']}, {line['foulsPerGame']}, {line['offsideGivenPerGame']}, 'exterieur', {line['rating']});"
    # query = f"INSERT INTO statistique_general (id_equipe, buts, tirs_pm, carton_j, carton_r, possession, passes_reussies, aeriens_gagnes, categorie, note) VALUES ('EQU{line['teamId']}', {line['goal']}, {line['shotsPerGame']}, {line['yellowCard']}, {line['redCard']}, {line['possession']}, {line['passSuccess']}, {line['aerialWonPerGame']}, 'exterieur', {line['rating']});"
    query = f"INSERT INTO statistique_attaque (id_equipe, tirs_pm, tirs_ca_pm, dribbles_pm, fautes_subies_pm, categorie, note) VALUES ('EQU{line['teamId']}', {line['shotsPerGame']}, {line['shotOnTargetPerGame']}, {line['dribbleWonPerGame']}, {line['foulGivenPerGame']}, 'exterieur', {line['rating']});"
    # query = f"INSERT INTO competion VALUES ('COMP{line['tournamentId']}', '{line['tournamentName']}');"
    # query = f"INSERT INTO equipe VALUES ('EQU{line['teamId']}', '{line['name']}', 'COMP{line['tournamentId']}');"
    # all_query.append(query)
    print(query)

data = getData('attaque-general.json')
for line in data:
    # query = f"INSERT INTO statistique_defense (id_equipe, tirs_pm, tacles_pm, interceptions_pm, fautes_pm, hors_jeux_pm, categorie, note) VALUES ('EQU{line['teamId']}', {line['shotsConcededPerGame']}, {line['tacklePerGame']}, {line['interceptionPerGame']}, {line['foulsPerGame']}, {line['offsideGivenPerGame']}, 'general', {line['rating']});"
    # query = f"INSERT INTO statistique_general (id_equipe, buts, tirs_pm, carton_j, carton_r, possession, passes_reussies, aeriens_gagnes, categorie, note) VALUES ('EQU{line['teamId']}', {line['goal']}, {line['shotsPerGame']}, {line['yellowCard']}, {line['redCard']}, {line['possession']}, {line['passSuccess']}, {line['aerialWonPerGame']}, 'general', {line['rating']});"
    query = f"INSERT INTO statistique_attaque (id_equipe, tirs_pm, tirs_ca_pm, dribbles_pm, fautes_subies_pm, categorie, note) VALUES ('EQU{line['teamId']}', {line['shotsPerGame']}, {line['shotOnTargetPerGame']}, {line['dribbleWonPerGame']}, {line['foulGivenPerGame']}, 'general', {line['rating']});"
    # query = f"INSERT INTO competion VALUES ('COMP{line['tournamentId']}', '{line['tournamentName']}');"
    # query = f"INSERT INTO equipe VALUES ('EQU{line['teamId']}', '{line['name']}', 'COMP{line['tournamentId']}');"
    # all_query.append(query)
    print(query)

# unique = list(set(all_query))
# for query in unique:
#     print(query)