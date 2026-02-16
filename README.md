## 🛠 How to Run
1. Install requirements: `pip install mysql-connector-python tabulate`
2. Run `database_setup.sql` in your MySQL Workbench.
3. Update `db_connection.py` with your MySQL root password.
4. Run `python main.py`.

## 📈 Database Schema
The project uses three main tables:
- `user`: For passenger authentication.
- `train_schedule`: To store train timings and fares.
- `booked_tickets`: To manage reservations and PNR generation.
