from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        if 'add_btn' in request.form:
            # Handle form submission for adding an entry
            # Code to add entry to database or perform other necessary actions
            add_btn_value = request.form['add_btn']
            print(f"Add button value: {add_btn_value}")
            return render_template('add_entry.html')
        elif 'search' in request.form:
            # Handle form submission for searching an entry
            # Code to search database or perform other necessary actions
            search_query = request.form['search']
            print(f"Search query: {search_query}")
            return render_template('index.html')
    # Handle GET request or other button clicks
    return render_template('index.html')

def add_
if __name__ == '__main__':
    app.run(debug=True)
