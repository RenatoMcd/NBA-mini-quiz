import requests
import json
import random

def main():
    while True:
        try:
            stat = val_stat(input("Chose one of the stats (PTS, AST, REB): ").upper())
            break
        except ValueError:
            pass

    score = 0

    for _ in range(10):
        player_1, player_2 = get_players(stat)
        asw = get_answer(player_1, player_2)
        while True:
            try:
                response = input(f"Which of this players as more {stat}, {player_1[0]}(1) or {player_2[0]}(2): ")
                if response == "1" or response == "2":
                    if response == asw:
                        print("Correct")
                        score +=1
                        break
                    elif response != asw:
                        print("Wrong")
                        break
                else:
                    print(f"Choose {player_1[0]}(1) or {player_2[0]}(2)")
                    pass
            except ValueError:
                pass

    print(f"Score: {score}/10")


def val_stat(s):

    if s in ["PTS", "AST", "REB"]:
        return s
    else:
        raise ValueError


def get_players(stat):
    response = requests.get(f"https://stats.nba.com/stats/leagueLeaders?ActiveFlag=No&LeagueID=00&PerMode=Totals&Scope=S&Season=All%20Time&SeasonType=Regular%20Season&StatCategory={stat}")
    o = response.json()

    top_50 = o["resultSet"]["rowSet"][0:50]

    players_stats = {}
    if stat == "PTS":
        stat_id = 21
    elif stat == "AST":
        stat_id = 16
    elif stat == "REB":
        stat_id = 15

    for player in top_50:
        players_stats[top_50[top_50.index(player)][1]] = top_50[top_50.index(player)][stat_id]

    try:
        player_1 = random.choice(list(players_stats.items()))
        player_2 = random.choice(list(players_stats.items()))
        if player_1 != player_2:
            return [player_1, player_2]
    except ValueError:
        pass


def get_answer(player_1, player_2):

    if int(player_1[1]) > int(player_2[1]):
        return "1"
    else:
        return "2"


if __name__ == "__main__":
    main()
