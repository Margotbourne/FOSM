-- Drop existing tables (Order matters! Drop tables with foreign keys first)
DROP TABLE IF EXISTS donations;
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
  publish_date DATE NOT NULL, 
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
  beneficiaries INTEGER NOT NULL, 
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  constraint fk_program foreign key(program_id)
        references program(id)
        on delete cascade
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
-- Add is_active to Supporter
CREATE TABLE supporter (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  is_gift_aid_eligible BOOLEAN NOT NULL,
  marketing_consent BOOLEAN NOT NULL,
  total_donated DECIMAL(12, 2) NOT NULL,
  is_active BOOLEAN NOT NULL DEFAULT TRUE -- <--- The new flag
);

-- Note: Donations don't need is_active because we 
-- want to keep the money records linked to the supporter.
CREATE TABLE donations (
  id SERIAL PRIMARY KEY,
  amount DECIMAL(12, 2) NOT NULL,
  donation_date DATE NOT NULL DEFAULT CURRENT_DATE,
  supporter_id INTEGER REFERENCES supporter(id) -- Keep as standard reference
);



-- Insert Programs first (needed for Foreign Keys)
INSERT INTO program (name, description) VALUES 
('Education', 'Rural education programs for tribal children.'),
('Health', 'Primary healthcare and nutrition services.');

-- Insert Branches
INSERT INTO branch (name, region_code, charity_number, address, email, currency) VALUES 
('Udaipur Main', 'UDA-01', '12345', 'Old Fatehpura, Udaipur', 'info@sevamandir.org', 'INR');

-- Insert People (Staff and Trustees)
INSERT INTO person (name, email, role, bio, image_url) VALUES 
('Anjali Devi', 'anjali@example.com', 'Program Coordinator', 'Expert in rural education.', 'anjali.jpg'),
('Dr. Mohan', 'mohan@example.com', 'Trustee', 'Specialist in public health.', 'mohan.jpg');

-- Insert Projects (linked to Programs)
-- Program 1 is Education, Program 2 is Health
INSERT INTO project (name, program_id, beneficiaries, is_active) VALUES 
('Shikshantar School', 1, 150, TRUE),
('Mobile Health Van', 2, 500, TRUE),
('Bridge School 2023', 1, 45, FALSE);

-- Insert News
INSERT INTO news (title, content, publish_date, image_url) VALUES 
('Dunkirk Commemoration', 'The position of the B.E.F had now become critical...', '1940-05-26', 'dunkirk.jpg'),
('New School Opening', 'We are excited to announce a new school in Delwara.', '2024-02-10', 'school.jpg');

-- Insert Reports
INSERT INTO report (title, reporting_year, report_type, file_url, is_public) VALUES 
('Annual Report 2023', 2023, 'Annual', 'report23.pdf', TRUE),
('Internal Audit', 2024, 'Audit', 'audit.pdf', FALSE);

-- Insert Supporters
INSERT INTO supporter (name, email, is_gift_aid_eligible, marketing_consent, total_donated) VALUES 
('Alice Smith', 'alice@test.com', TRUE, TRUE, 1200.00),
('Bob Jones', 'bob@test.com', FALSE, TRUE, 50.00);

-- Insert Donations
INSERT INTO donations (amount, supporter_id) VALUES (500.00, 1);
INSERT INTO donations (amount, supporter_id) VALUES (700.00, 1);