from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("NBA Analysis").getOrCreate()

df = spark.read.csv('nba_historical.csv', header=True, inferSchema=True)

df.createOrReplaceTempView("players")

# Query 1: Top 10 scorers of all time (by ppg across all seasons)
result1 = spark.sql("""
        SELECT PLAYER, TEAM, SEASON, ROUND(PTS / GP, 1) as points_per_game
        FROM players
        ORDER BY points_per_game DESC
        LIMIT 10
""")
result1.show()

# Query 2: Which team had the most players in the league leaders list per season?
result2 = spark.sql("""
        SELECT COUNT(PLAYER) AS player_count, TEAM
        FROM players
        GROUP BY TEAM, SEASON
        ORDER BY player_count  DESC
        LIMIT 10
    
""")
result2.show()

spark.stop()
