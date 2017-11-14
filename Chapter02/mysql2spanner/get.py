# Imports the Google Cloud Client Library.
from google.cloud import spanner
from ast import literal_eval as make_tuple
import sys

def insert_data(instance_id, database_id, data_file):
    """Inserts sample data into the given database.
    The database and table must already exist and can be created using
    `create_database`.
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    dat = []

    f = open(data_file,"r") #opens file with name of "test.txt"
    #print(f.read(1)) 
    for line in f:
	dat.append(line)
    #dat = f.read()
    print(dat)
    dat = [x.strip() for x in dat] 
    print(dat)
    table_name = dat.pop(0)
    print(table_name)
    dat = [make_tuple(x) for x in dat] 
    col_names = dat.pop(0)
    print(col_names)
    print(dat)
    f.close()

    with database.batch() as batch:
        batch.insert(
            table=table_name,
            columns=col_names,
	    values=dat)
            #values=[
            #    (3, u'Alice'),
            #    (4, u'Lea'),
	#	(5, u'David')])

# Instantiate a client.
spanner_client = spanner.Client()

# Your Cloud Spanner instance ID.
instance_id = 'test124'

# Get a Cloud Spanner instance by ID.
instance = spanner_client.instance(instance_id)

# Your Cloud Spanner database ID.
database_id = 'classicmodels'

# Get a Cloud Spanner database by ID.
database = instance.database(database_id)

# Execute a simple SQL statement.
with database.snapshot() as snapshot:
    results = snapshot.execute_sql('SELECT * from customers')

    for row in results:
        print(row)

data_file = sys.argv[1:].pop(0)
print data_file
insert_data(instance_id, database_id, data_file)
print('Data inserte')


