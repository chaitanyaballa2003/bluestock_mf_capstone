-- Fund Master Table
CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

-- NAV History Table
CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date TEXT,
    nav REAL
);

-- AUM Table
CREATE TABLE fact_aum (
    fund_house TEXT,
    month TEXT,
    aum REAL
);