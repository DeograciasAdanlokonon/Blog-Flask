from flask import Flask, render_template, request
from post import Post
from email_manager import NewEmail
import requests
from random import random, randint, choice
import datetime as dt


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']


# let create an empty list
posts_list = []

posts_url = "https://api.npoint.io/179d86aeefbaf6842b0f"
response = requests.get(url=posts_url)
posts = response.json()
for post in posts:
    day = randint(1, 32)
    month = choice(months)
    year = dt.datetime.now().year
    post_date = month + " " + str(day) + ", " + str(year)

    posts_list.append(Post(post['id'], post['title'], post['subtitle'], post['body'], post['image_url'], post_date))


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', posts=posts_list)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def post(index):
    for post_item in posts:
        if post_item['id'] == index:
            current_post = Post(post_item['id'], post_item['title'], post_item['subtitle'], post_item['body'],
                                post_item['image_url'], post_date)
            return render_template('post.html', id=index, post=current_post)


@app.route("/form-entry", methods=['POST'])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    if request.method == "POST":
        if name != "" and email != "" and phone != "" and message != "":
            new_email = NewEmail()
            new_email.send_email(name, phone, email, message)
            return render_template('contact.html', success="Successfully sent your message!")
        else:
            return render_template('contact.html', success="Fill out all inputs!")


if __name__ == "__main__":
    # run app in debug mode to auto-reload our server
    app.run(debug=True)
