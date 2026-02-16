CREATE DATABASE train_reservation;
USE train_reservation;

-- Table for user details [cite: 7, 21]
CREATE TABLE user (
    user_id VARCHAR(50) PRIMARY KEY,
    pid INT,
    name VARCHAR(100),
    phone VARCHAR(15),
    email_id VARCHAR(100),
    password VARCHAR(50)
);

-- Table for train details [cite: 118, 121]
CREATE TABLE train_schedule (
    train_no INT PRIMARY KEY,
    train_name VARCHAR(100),
    origin VARCHAR(100),
    destination VARCHAR(100),
    journey_distance INT,
    total_time VARCHAR(50),
    ac1 INT,
    sl INT,
    gen INT,
    ac_fare INT,
    sl_fare INT,
    gen_fare INT,
    avl_days VARCHAR(100)
);

-- Table for booked tickets [cite: 680, 681]
CREATE TABLE booked_tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    pnr_no INT,
    train_no INT,
    cus_name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    fare INT,
    status VARCHAR(20)
);