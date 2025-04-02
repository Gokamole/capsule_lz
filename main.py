from PPstats import PSStatistics

if __name__ == "__main__":
    filename = "playstation_players.csv"
    stats = PSStatistics("playstation_players.csv")
    stats.plot_pie_chart()