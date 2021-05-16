from flask import Flask, request, render_template, jsonify, url_for, redirect
# import gyanPreprocessors
app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def gyan():
	if request.method == "POST":
		input_array = request.form.get("inputArray")
		return redirect(url_for('results', input_array=input_array))
	return render_template("index.html")

@app.route('/results')
def results():
	input_array = request.args.get('input_array', None)
	return render_template("results.html", input_array=input_array)

if __name__ == "__main__":
	app.run(debug=True)
