# posts/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import current_user,login_required
from blog import db
from blog.models import BlogPost
from blog.posts.forms import BlogPostForm


posts = Blueprint('posts',__name__)

# create
@posts.route("/create",methods=['GET','POST'])
@login_required
def create_post():
	form = BlogPostForm()
	if request.method == 'POST' and form.validate() and form.validate_on_submit():
		blog_post = BlogPost(title=form.title.data,text=form.text.data,user_id=current_user.id)
		db.session.add(blog_post)
		db.session.commit()
		flash('Post Created')
		return redirect(url_for('core.index'))
	return render_template('create_post.html',form=form)


# View Post
@posts.route("/<int:post_id>",methods=['GET','POST'])
def post(post_id):
	post = BlogPost.query.get_or_404(post_id)
	return render_template('post.html',post=post)

# Update
@posts.route("/<int:post_id>/update",methods=['GET','POST'])
@login_required
def update_post(post_id):
	post = BlogPost.query.get_or_404(post_id)
	if post.author != current_user:

		abort(403)

	form = BlogPostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.text = form.text.data
		db.session.commit()
		flash('Post Updated')
		return redirect(url_for('posts.post', post_id=post.id))

	elif request.method == 'GET':
		form.title.data = post.title
		form.text.data = post.text
		return render_template('create_post.html', title='Update',form=form)

# Delete
@posts.route("/<int:post_id>/delete",methods=['GET','POST'])
@login_required
def delete_post(post_id):
	post = BlogPost.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash('Post Deleted')
	return redirect(url_for('core.index'))
