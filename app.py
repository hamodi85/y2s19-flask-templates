from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	opposite_day = True
	food_list = ["dawali","sushi","buriito"]
	least_fav_food = ["asd", "dfg", "aqwe"]
	return render_template("index.html", list1=food_list,opposite_day=opposite_day , list2=least_fav_food)
if __name__ == '__main__':
   app.run(debug = True)
