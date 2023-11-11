SELECT
  name AS "選手名",
  height AS "身長"
FROM
  players
WHERE
  height > (
    SELECT
      AVG(height)
    FROM
      players
  );