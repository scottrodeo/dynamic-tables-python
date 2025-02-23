import unittest
from dynamic_tables.dynamic_tables import DynamicTables

class TestDynamicTables(unittest.TestCase):
    def setUp(self):
        """ 
        Runs before each test to set up a clean environment.
        - Initializes a DynamicTables instance.
        - Establishes a database connection.
        - Configures table settings.
        - Cleans up any existing test tables to prevent conflicts.
        """
        self.tables = DynamicTables()
        
        # Establish database connection (Update credentials as needed)
        self.tables.connectHC('mydb', 'myuser', 'losdjfaosidjf-sdfgjkd4DDSRs', 'localhost')

        # Configure table settings for testing
        self.tables.set_table_prefix("dtbltest_")  # Prefix to identify test tables
        self.tables.set_columns("domain TEXT, category TEXT, lang TEXT")  # Define table schema
        self.tables.set_dynamic_column("domain")  # Set which column determines table names
        
        # Cleanup any leftover test tables before each test
        self.cleanup_test_tables()

    def tearDown(self):
        """ 
        Runs after each test to remove any created test tables.
        - Ensures each test runs in isolation.
        - Prevents test data from accumulating across multiple runs.
        """
        self.cleanup_test_tables()

    def cleanup_test_tables(self):
        """ 
        Deletes all tables that match the test prefix (`dtbltest_`).
        - Prevents duplicate data issues.
        - Ensures that only test-related tables are deleted.
        """
        all_tables = self.tables.show_tables()  # Retrieve all tables in the database
        for table in all_tables:
            if table.startswith("dtbltest_"):  # Ensure only test tables are deleted
                self.tables.cur.execute(f"DROP TABLE IF EXISTS {table} CASCADE;")
        self.tables.conn.commit()  # Apply changes to the database

    def test_insert_data(self):
        """ 
        Tests whether data is correctly inserted into a dynamically created table.
        - Inserts a test row.
        - Verifies that exactly one row was added.
        - Ensures that the stored data matches the input.
        """
        self.tables.input("example.com", "news", "en")  # Insert sample data
        rows = self.tables.select_table("dtbltest_examplecom")  # Retrieve inserted rows

        self.assertEqual(len(rows), 1)  # Expecting exactly 1 row
        self.assertEqual(rows[0][1], "example.com")  # Verify first column matches input

    def test_table_creation(self):
        """ 
        Tests whether tables are dynamically created when inserting new data.
        - Inserts a new row with a previously unused domain.
        - Retrieves all tables and checks if the expected table exists.
        """
        self.tables.input("test.com", "tech", "en")  # Insert data that should create a new table
        all_tables = self.tables.show_tables()  # Fetch the list of existing tables

        self.assertIsInstance(all_tables, list)  # Ensure we got a list
        self.assertGreater(len(all_tables), 0, "No tables were created.")  # There should be at least one table
        self.assertIn("dtbltest_testcom", all_tables)  # Verify the new table was created

if __name__ == "__main__":
    unittest.main()

