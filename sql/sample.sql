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
  name LIKE "%シャツ%" -- 6
  -- 各商品あたりの利益が上位5件の商品の名前と利益を取得してください
SELECT
  name,
  price - cost
FROM
  items
ORDER BY
  price - cost DESC
LIMIT
  5 -- 7
  -- 7000円以下で「グレーパーカー」より利益が高い商品を取得してください
SELECT
  name,
  price - cost
FROM
  items
WHERE
  price <= 7000
  AND price - cost > (
    SELECT
      price - cost
    FROM
      items
    WHERE
      name = "グレーパーカー"
  );

-- 8
-- 売れた数が多い上位5商品のidと個数を取得してください
SELECT
  item_id,
  COUNT(item_id)
FROM
  sales_records
GROUP BY
  item_id
ORDER BY
  count(*) DESC
LIMIT
  5;

-- 9
SELECT
  items.id,
  items.name,
  COUNT(*)
FROM
  sales_records
  JOIN items ON sales_records.item_id = items.id
GROUP BY
  items.id,
  items.name
ORDER BY
  COUNT(*) DESC
LIMIT
  5;

-- 9-2
SELECT
  items.id,
  items.name,
  COUNT(*)
FROM
  sales_records
  JOIN items ON sales_records.item_id = items.id
GROUP BY
  items.id,
  items.name
ORDER BY
  COUNT(*) DESC
LIMIT
  5;