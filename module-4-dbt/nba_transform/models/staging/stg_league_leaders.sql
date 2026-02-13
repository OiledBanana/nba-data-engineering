SELECT
    PLAYER as player_name,
    TEAM as team,
    GP as games_played,
    MIN as minutes_played,
    AST as assist,
    FG_PCT as fg_percentage,
    ROUND(PTS/GP, 1) as points_per_game,
    ROUND(REB / GP, 1) as rpg,
    ROUND(AST / GP, 1) as apg,
    SEASON as season
FROM {{ source('nba_stats', 'league_leaders_historical') }}