from PPstats import PlayerStats

if __name__ == "__main__":
    file_name = "playstation_players.csv"  
    stats = PlayerStats(file_name)
    stats.plot_country_distribution()
