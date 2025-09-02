-- View 1: Média de poluentes por dia
CREATE OR REPLACE VIEW vw_media_poluentes AS
SELECT date, AVG("CO(GT)") AS co_medio, AVG("NOx(GT)") AS nox_medio
FROM air_quality
GROUP BY date;

-- View 2: Média de temperatura e umidade por dia
CREATE OR REPLACE VIEW vw_temp_umidade AS
SELECT date, AVG("T") AS temp_media, AVG("RH") AS umidade_media
FROM air_quality
GROUP BY date;

-- View 3: Top 10 registros com maior concentração de CO
CREATE OR REPLACE VIEW vw_top10_co AS
SELECT *
FROM air_quality
ORDER BY "CO(GT)" DESC
LIMIT 10;
