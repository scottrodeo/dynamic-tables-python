# this is test.py

import sys, logging
import os

# Add the parent directory (dynamic-tables-python) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dynamic_tables import DynamicTables  # Now Python should find this!

# Test the class
tables = DynamicTables()
print("DynamicTables initialized successfully!")


from dynamic_tables import DynamicTables

# initiate the dtable object
tables = DynamicTables()


tables.show_version()

#tables.change_log_level('DEBUG')

 
tables.connectHC('mydb','myuser','losdjfaosidjf-sdfgjkd4DDSRs','localhost')
#tables.connectJSON()
#tables.connectENVS() # source: . setenv.sh


tables.set_table_prefix('dt1_')

# clear existing tables created with the prefix
tables.delete_tables()

# define input columns
tables.set_columns('domain VARCHAR(100), keyword VARCHAR(100), language VARCHAR(100)')

# define automatic column
tables.set_dynamic_column('domain')


#input test data
tables.input('wikipedia.org','cats','en')
tables.input('wikipedia.org','dogs','en')

tables.input('google.com','maps','en')
tables.input('google.com','images','en')


# formatted dynamic column name example
print('---'+tables.format_table_name('wikipedia.org')+'---')

# select a table with the converted dynamic column name
tables.show_table(tables.format_table_name('wikipedia.org'))


#print('---'+tables.format_table_name('google.com')+'---')
#tables.show_table(tables.format_table_name('google.com'))

#tables.status()
#tables.show_tables()
#tables.show_columns_all()

tables.close()



























