import sqlite3
from classes.request import EmployeeType, Employee
from datetime import date


class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance._conn = sqlite3.connect(
                'employee_database.db', check_same_thread=False)
            cls._instance._cursor = cls._instance._conn.cursor()
            # cls._instance.drop_table() # debugging purposes
            cls._instance._initialize_tables()
            cls._instance.populate_database_once()
        return cls._instance

    def _initialize_tables(self):
        # Create a table for Regular Employees

        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                employee_type TEXT,
                number_of_leaves INTEGER,
                benefits TEXT,
                contract_end_date DATE,
                project TEXT
            )
        ''')

        # Commit changes
        self._conn.commit()

    def drop_table(self):
        self._cursor.execute('DROP TABLE IF EXISTS employees')
        self._conn.commit()

    def populate_database_once(self):
        # Check if the database is already populated
        cursor = self._cursor
        cursor.execute('SELECT COUNT(*) FROM employees')
        count = cursor.fetchone()[0]
        if count > 0:
            print("Database already populated.")
            return

        # Example Regular Employee
        regular_employee_data = Employee(
            first_name="John",
            last_name="Doe",
            email="john.doe@email.com",
            employee_type=EmployeeType.REGULAR,
            number_of_leaves=20,
            benefits="Health Insurance"
        )
        self.insert_regular_employee(regular_employee_data)

        # Example Contractual Employee
        contractual_employee_data = Employee(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@email.com",
            employee_type=EmployeeType.CONTRACTUAL,
            contract_end_date=str(date.today()),
            project="Project X"
        )
        print("contractual_employee_data")
        print(contractual_employee_data)
        self.insert_contractual_employee(contractual_employee_data)

        print("Database populated with sample data.")

    def insert_regular_employee(self, employee_data: Employee):
        cursor = self._cursor
        cursor.execute('''
            INSERT INTO employees (first_name, last_name, email, employee_type, number_of_leaves, benefits)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (employee_data.first_name, employee_data.last_name, employee_data.email, EmployeeType.REGULAR,
              employee_data.number_of_leaves, employee_data.benefits))
        self._conn.commit()

    def insert_contractual_employee(self, employee_data: Employee):
        cursor = self._cursor
        cursor.execute('''
            INSERT INTO employees (first_name, last_name, email, employee_type, contract_end_date, project)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (employee_data.first_name, employee_data.last_name, employee_data.email, EmployeeType.CONTRACTUAL,
              employee_data.contract_end_date, employee_data.project))
        self._conn.commit()

    def get_all_regular_employees(self):
        cursor = self._cursor
        cursor.execute('''
            SELECT * FROM employees
        ''')

        columns = [col[0] for col in cursor.description]
        results = cursor.fetchall()

        return [dict(zip(columns, row)) for row in results]

    def find_employee_by_id(self, employee_id: int):
        cursor = self._cursor
        if employee_id is None:
            cursor.execute('''SELECT * FROM employees''')
            columns = [col[0] for col in cursor.description]
            results = cursor.fetchall()

            return [dict(zip(columns, row)) for row in results]
        else:
            cursor.execute('''
                SELECT * FROM employees WHERE id = ?
            ''', (employee_id,))
            columns = [col[0] for col in cursor.description]
            regular_employee = cursor.fetchone()

            if regular_employee:
                return dict(zip(columns, regular_employee))

        return None

    def update_employee_by_id(self, employee_id: int, updated_data: Employee):
        cursor = self._cursor
        current_data = self.find_employee_by_id(employee_id)
        if current_data is None:
            return None

        if current_data.get('employee_type') == EmployeeType.REGULAR:
            # Update Regular Employee by id
            cursor.execute('''
                UPDATE employees SET
                first_name = ?,
                last_name = ?,
                email = ?,
                number_of_leaves = ?,
                benefits = ?
                WHERE id = ?
            ''', (updated_data.first_name, updated_data.last_name, updated_data.email,
                  updated_data.number_of_leaves, updated_data.benefits, employee_id))

        elif current_data.get('employee_type') == EmployeeType.CONTRACTUAL:
            # Update Contractual Employee by id
            cursor.execute('''
                UPDATE employees SET
                first_name = ?,
                last_name = ?,
                email = ?,
                contract_end_date = ?,
                project = ?
                WHERE id = ?
            ''', (updated_data.first_name, updated_data.last_name, updated_data.email,
                  updated_data.contract_end_date, updated_data.project, employee_id))

        # Commit changes
        self._conn.commit()
        return True

    def delete_employee_by_id(self, employee_id: int):
        cursor = self._cursor
        cursor.execute('''
                DELETE FROM employees WHERE id = ?
            ''', (employee_id,))
        self._conn.commit()

    def get_cursor(self):
        return self._cursor

    def close_connection(self):
        self._conn.close()
