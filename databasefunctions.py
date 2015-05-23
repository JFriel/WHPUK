#CREATE TABLE songs(title TEXT)


def insert(songtitle):
	db = sqlite.connect(':songs:')
	cursor = db.cursor()

	cursor.execute('''INSERT INTO songs(title)
                  VALUES(?)''', (songtitle))

	db.commit
	db.close

def retrieve(songnumber):
	#SELECT * FROM mytable ORDER BY somefield LIMIT 1 OFFSET number;
	number = songnumber
	db = sqlite.connect(':songs:')
	cursor = db.cursor()
	curser.execute('''SELECT * FROM table ORDER BY RANDOM() LIMIT 1; ''')
	randomsong = curser.fetchone()
	db.commit
	db.close
	return randomsong 