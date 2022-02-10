from flask import Flask, request, render_template

point_values = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

app = Flask('scrabble')

@app.route("/") # Landing page
def hello():
    return "<h1>It's alive!!!🧟‍♂️</h1>"

## Put your work here. You are also free to use static/css and templates/ if you would like
@app.route("/<my_variable>")
def main(my_variable):
    variable=my_variable.upper()
    sum=0
    for i in my_variable:
        sum+=point_values[i]
    return f'{sum}'

@app.route("/hand",methods=["GET", "POST"])
def json_score():
    return json_load(sum)

if __name__ == '__main__':
    # Start the Flask app
    app.run() # Local
