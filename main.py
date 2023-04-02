from flask import Flask,render_template,redirect

app =Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/home")
def home():
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/package")
def package():
    return render_template("package.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog")
def blog_grid():
    return render_template("blog.html")

@app.route("/single")
def blog_detail():
    return render_template("single.html")

@app.route("/destination")
def destination():
    return render_template("destination.html")

@app.route("/guide")
def travel_guide():
    return render_template("guide.html")

@app.route("/testimonial")
def test():
    return render_template("testimonial.html")

app.run(debug=True)