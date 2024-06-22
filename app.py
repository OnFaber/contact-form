import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm
from models import db, Contact


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/", methods=["GET", "POST"])
    def index():
        form = ContactForm(db_model=Contact)
        if request.method == "POST" and form.validate_on_submit():
            new_contact = Contact(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                options=form.options.data,
                message=form.textarea.data,
                consent=form.checkbox.data,
            )

            db.session.add(new_contact)
            db.session.commit()
            flash("thanks for completing the form. We'll be in touch soon!", "success")
            return redirect(url_for("index"))

        return render_template("index.html", form=form)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
