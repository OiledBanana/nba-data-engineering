SELECT
    player_name,
    team,
    games_played,
    points_per_game,
    rpg,
    apg
FROM {{ ref('stg_league_leaders') }}
WHERE season = '2024-25'
  AND games_played > 50
ORDER BY points_per_game DESC