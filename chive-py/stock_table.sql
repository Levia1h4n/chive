CREATE TABLE IF NOT EXISTS stock_all(
    state_dt VARCHAR(10),
    stock_code VARCHAR(9),
    open float,
    close float,
    high float,
    low float,
    vol int,
    amount float,
    pre_close float,
    amt_change float,
    pct_change float,
    primary key (state_dt,stock_code) 
);

CREATE INDEX stock_code ON stock_all(stock_code);