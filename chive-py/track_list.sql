CREATE TABLE IF NOT EXISTS track_list(
    stock_code VARCHAR(10),
    primary key (stock_code)
);

CREATE INDEX stock_code ON track_list(stock_code);