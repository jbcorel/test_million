-- Необходимо: использовав агрегатные функции, выбрать 
-- все шк и цены (reports.barcode, reports.price)
-- с одинаковыми названиями точек продаж (pos.title).

CREATE TABLE pos
(
    id int PRIMARY KEY,
    title character varying
);

CREATE TABLE reports
(
    id int PRIMARY KEY,
    barcode character varying,
    price float,
    pos_id int
);


-- Пример данных
INSERT INTO reports (id, barcode, price, pos_id) VALUES
(1, '1234567890123', 10.50, 1),
(2, '1234567890124', 15.00, 1),
(3, '1234567890125', 20.00, 2),
(4, '1234567890126', 25.00, 2),
(5, '1234567890127', 30.00, 3),
(6, '1234567890128', 5.00, 1),
(7, '1234567890129', 12.00, 1),
(8, '1234567890130', 22.00, 4),
(9, '1234567890131', 18.00, 2),
(10, '1234567890132', 14.50, 2),
(11, '1234567890133', 9.99, 5),
(12, '1234567890134', 45.00, 3);

INSERT INTO pos (id, title) VALUES
(1, 'Store A'),
(2, 'Store B'),
(3, 'Store C'),
(4, 'Store D'),
(5, 'Store E');



-- Основной
SELECT reports.barcode, reports.price, pos.title
FROM reports
JOIN pos ON reports.pos_id = pos.id
WHERE reports.pos_id IN (
  SELECT pos_id
  FROM reports 
  GROUP BY pos_id 
  HAVING COUNT(pos_id) > 1
)
ORDER BY pos.title;


-- Для сравнения
SELECT pos.title, AVG(reports.price) AS avg_price, COUNT(reports.pos_id) as num_reports
FROM pos
JOIN reports ON pos.id = reports.pos_id
GROUP BY pos.title
ORDER BY pos.title;