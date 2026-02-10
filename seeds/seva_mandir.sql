-- Drop existing tables (Order matters! Drop tables with foreign keys first)
DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS branch;
DROP TABLE IF EXISTS news;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS program;
DROP TABLE IF EXISTS report;
DROP TABLE IF EXISTS supporter;

-- 1. Branch Table
CREATE TABLE branch (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  region_code TEXT NOT NULL UNIQUE, -- Region codes often have letters/leading zeros
  charity_number TEXT NOT NULL,
  address TEXT NOT NULL,
  email TEXT NOT NULL,
  currency TEXT NOT NULL
);

-- 2. News Table
CREATE TABLE news (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  publish_date DATE NOT NULL, -- Using DATE to match your "YYYY-MM-DD" tests
  image_url TEXT
);

-- 3. Person Table
CREATE TABLE person (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  role TEXT NOT NULL,
  bio TEXT NOT NULL,
  image_url TEXT
);

-- 4. Program Table
CREATE TABLE program (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT NOT NULL
);

-- 5. Project Table
CREATE TABLE project (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  program_id INTEGER REFERENCES program(id) ON DELETE CASCADE, -- Link to Program
  beneficiaries INTEGER NOT NULL, -- Fixed spelling
  is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- 6. Report Table
CREATE TABLE report (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  reporting_year INTEGER NOT NULL,
  report_type TEXT NOT NULL,
  file_url TEXT NOT NULL,
  is_public BOOLEAN NOT NULL DEFAULT TRUE
);

-- 7. Supporter Table
CREATE TABLE supporter (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  is_gift_aid_eligible BOOLEAN NOT NULL,
  marketing_consent BOOLEAN NOT NULL,
  total_donated DECIMAL(12, 2) NOT NULL -- Good for currency
);