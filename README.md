# Krisp Assignment for an Associate Data Engineer role

## Setup container



1. Run the 'docker-compose.yml' file
Docker compose file which includes containers
 * **database** - This container runs init.sql file, make image and environment of the database.
 * **app** — For a python application file where it included short functions and its definition, querying functions to deal with a database.
2. In **app** file you can find the python code, docker file, which is configuration for server. The requirement file includes a python library which is crucial for this project


3.  In **db** file you will find init.sql file, which creates tables in taskdb

## Database structure 


* **user** table is the main table which includes user_id filed as a primary key for this table and foreign key for rest tables
* **talked_time** table has the main field duration which is the duration of talked time.
* **speaker_used** table has speaker_type and speaker_amount
* **voice_sentiment** includes sentiment filed which indicates about emotional tone of conversation
