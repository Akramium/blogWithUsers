from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let me in!")


# create a comment form
class CommentForm(FlaskForm):
    # I will work on it this weekend
    # TODO: 1 - Create a CommentForm in the form.py file it will only contain a single CKEditorField for users to write their comments.
    # TODO: Hint: You might need to check the documentation or day 67 to see how we implement the CKEditor.
    # TODO: 2- Create a Table called Comment where the tablename is "comments". It should contain an id and a text property which will be the primary key and the text entered into the CKEditor.
    # TODO: 3- Establish a One to Many relationship Between the User Table (Parent) and the Comment table (Child). Where One User is linked to Many Comment objects.
    # TODO: 4- Establish a One to Many relationship between each BlogPost object (Parent) and Comment object (Child). Where each BlogPost can have many associated Comment objects.
    # TODO: 5. At this point, with a new Table added, it's a good idea to delete the existing blog.db entirely and to use the line db.create_all() to create all the tables from scratch.
    # This means you should create a new admin user (id == 1), a new blog post and another user who will make some comments.
    # TODO: 6. Log in as your John Doe user (or any user that is not the primary user) and make a comment on a blog post. In order for this to work, you will need to update the /post/<int:post_id> route. Make sure that only authenticated (logged-in) users can save their comment. Otherwise, they should see a flash message telling them to log in and redirect them to the /login route.
    # TODO: 7. Update the code in post.html to display all the comments associated with the blog post.
    # later in this week

    pass
