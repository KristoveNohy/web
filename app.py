from flask import Flask, render_template, request, redirect, url_for, 

app = Flask(__name__)

@app.route("/")
def index():
    services = [
        {'id': 1, 'title': 'Klampiarske práce', 'desc': 'Precízne oplechovanie a montáž odkvapov.', 'image': 'https://via.placeholder.com/400x200'},
        {'id': 2, 'title': 'Tesárske práce', 'desc': 'Krovy, altánky, pergoly — krásne drevené konštrukcie.', 'image': 'https://via.placeholder.com/400x200'},
        {'id': 3, 'title': 'Pokrývačské práce', 'desc': 'Škridlové, plechové a trapézové krytiny.', 'image': 'https://via.placeholder.com/400x200'},
    ]
    return render_template("index.html", services=services)

@app.route("/service/<int:service_id>")
def service_detail(service_id):
    services = [
        {'id': 1, 'title': 'Klampiarske práce', 'desc': 'Detailné info o klampiarskych prácach.'},
        {'id': 2, 'title': 'Tesárske práce', 'desc': 'Detailné info o tesárskych prácach.'},
        {'id': 3, 'title': 'Pokrývačské práce', 'desc': 'Detailné info o pokrývačských prácach.'},
    ]
    service = next((s for s in services if s['id'] == service_id), None)
    if not service:
        return "Služba nenájdená", 404
    return render_template("detail.html", service=service)

if __name__ == "__main__":
    app.run(debug=True)