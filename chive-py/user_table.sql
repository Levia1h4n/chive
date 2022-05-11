CREATE TABLE IF NOT EXISTS user_info(
    user_acct VARCHAR(10),
    stock_pool BLOB,
    primary key (user_acct)
);

CREATE INDEX user_acct ON user_info(user_acct);