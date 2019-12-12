from app import app
from flask import jsonify, request, render_template
		
@app.route('/')
def Dashboard():
    	#data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watching TV' : 2, 'Sleeping' : 7}
	#print(data)
	return render_template('dashboard.html')
		
if __name__ == "__main__":
    app.run(port=5000)