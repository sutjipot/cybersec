#!/usr/bin/env python3
import sys
import sqlite3


def add_agent(conn, aid, name):
	cursor = conn.cursor()
	query = f"INSERT INTO Agent VALUES ('{aid}', '{name}')"
	cursor.execute(query)
	conn.commit()

def delete_agent(conn, aid):
    cursor = conn.cursor()
    query = "DELETE FROM Agent WHERE id = ?"
    cursor.execute(query, (aid,))
    conn.commit()


def read_database(conn):
	agents = []
	c = conn.cursor()
	
	for t in c.execute('SELECT id, name FROM Agent ORDER by id'):
		agents.append(t)
 
 
	return agents


def main(argv):
	name = sys.argv[1]
	conn = sqlite3.connect(name)
	while True:
		agents = read_database(conn)
		print('\nActive agents:\n')
		for agent in agents:
			print(agent[0], agent[1])
		print()
		command = input('What would you like to do: [a]dd, [r]emove, or [q]uit? ')

		if command[0].startswith('a'):
			aid = input('id? ')
			name = input('name? ')
			add_agent(conn, aid, name)
		elif command[0].startswith('r'):
			aid = input('id? ')
			delete_agent(conn, aid)
		elif command[0].startswith('q'):
			break
	conn.close()
	

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s database' % sys.argv[0])
	else:
		main(sys.argv)
