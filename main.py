from flask import Flask, render_template
import requests


marks_counts = {}

for n in range(1, 51):

    response = requests.get(f'https://api.dane.gov.pl/1.4/resources/54117,samochody-osobowe-w-grudniu-2023-roku/data?page={n}')

    data = response.json()
    vehicles = data["data"]

    for vehicle in vehicles:
        if vehicle["attributes"]["col1"]["repr"] == "PODLASKIE":
            marks_counts.update({vehicle["attributes"]["col2"]["repr"]: vehicle["attributes"]["col3"]["repr"]})


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', marks_counts=marks_counts)


if __name__ == "__main__":
    app.run(debug=True)
