# Core/views.py
from flask import render_template,request,Blueprint
from blog.models import BlogPost

core = Blueprint('core',__name__)

@core.route('/')
def index():
	page = request.args.get('page',1,type=int)
	posts = BlogPost.query.order_by(BlogPost.created_at.desc()).paginate(page=page,per_page=4)
	return render_template('index.html',posts=posts)

@core.route('/about')
def about():
	return render_template('about.html')
