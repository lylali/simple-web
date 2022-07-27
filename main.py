from flask import Flask, render_template, request
from get_posts import GetPost
from send_email import EmailManager
app = Flask(__name__)

post_data = GetPost()

@app.route("/")
def home_page():
    return render_template("index.html", post_data=post_data)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact_page():
    if request.method == "POST":
        message = "Form submission successful!"
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        e_message = request.form['message']
        email_manager = EmailManager(name, email, phone, e_message)
        email_manager.send_email()
    else:
        message = None
    return render_template("contact.html", message=message)

@app.route("/posts/<int:index>")
def posts_page(index):
    return render_template("post.html", index=index, post_data=post_data)

if __name__ == '__main__':
    app.run(debug=True, port=4000)


