DROP TABLE IF EXISTS silver_olympic_events;

CREATE TABLE silver_olympic_events AS
SELECT
    "ID" as athlete_id,
    "Name" as name,
    "Sex" as sex,
    COALESCE("Age", 0) as age,
    "Team" as team,
    "NOC" as noc,
    "Year" as year,
    "Sport" as sport,
    COALESCE("Medal", 'No Medal') as medal
FROM raw_athlete_events;