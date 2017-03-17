def firebasepush(data):
	print data
	db.post('/Log',data)


def firebaseget():
	data = db.get('/Log',None)
	data = data.values()
	return data

@app.route('/fetchdata')
def fetchdata():
	data = firebaseget()
	return json.dumps(data)
