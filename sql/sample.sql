-- 1
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

-- 2
SELECT
  AVG(players.goals) AS "平均得点",
  countries.name AS "国名"
FROM
  players
  JOIN countries ON players.country_id = countries.id
GROUP BY
  countries.name;

-- 3
-- 全商品の名前を重複無く取得
SELECT
  DISTINCT(name)
FROM
  items -- 4
  -- 全商品の名前と値段を、値段が高い順に並べてください
SELECT
  price,
  name DESC
FROM
  items
ORDER BY
  price DESC -- 5
  -- 名前の一部に「シャツ」を含む商品の、全てのカラムの値を取得
SELECT
  *
FROM
  items
WHERE
  name LIKE "%シャツ%"