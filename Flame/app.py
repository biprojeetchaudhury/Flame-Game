from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_flame(name1, name2):
    x = ["Friendship","Love","Affection","Marriage","Enemity"]
    y = 0

    name1 = name1.lower()
    name2 = name2.lower()

    name1 = list(name1)
    name2 = list(name2)

    name1.sort()
    name2.sort()

    i = 0
    j = 0


    while i in range(len(name1)) and j in range(len(name2)):
        if name1[i] == name2[j]:
            y += 1
            i += 1
            j += 1
        elif name1[i] < name2[j]:
            i += 1
        else:
            j += 1

    c = len(name1) + len(name2) - 2 * y
    return x[(c%len(x)) - 1]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']
        result = calculate_flame(name1, name2)
        return render_template('index.html', result=result, name1=name1, name2=name2)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)

