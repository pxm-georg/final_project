from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tab1')
def tab1():
    return render_template('tab1.html')

@app.route('/tab2')
def tab2():
    return render_template('tab2.html')

@app.route('/tab3')
def tab3():
    return render_template('tab3.html')

@app.route('/tab4')
def tab4():
    return render_template('tab4.html')

@app.route('/tab5')
def tab5():
    return render_template('tab5.html')

@app.route('/tab6')
def tab6():
    return render_template('tab6.html')

@app.route('/tab7')
def tab7():
    return render_template('tab7.html')

@app.route('/tab8')
def tab8():
    return render_template('tab8.html')

if __name__ == '__main__':
    app.run(debug=True)
