from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import visual # import entire file, rather than class, to avoid circular imports

@app.route('/')
def home():
    return render_template('index.html')

# Create Users Controller

@app.route('/visual/enter', methods =['POST'])
def enter_visual():
    if visual.Visual.enter_visual(request.form):
        return redirect('/dashboard')
    return redirect('/new/visual')

# Read Users Controller

@app.route('/dashboard')
def visuals_page():
    
    return render_template('dashboard.html')
    

@app.route('/new/visual')
def enter_visual_page():
    
    return render_template('enter_visual.html')


@app.route('/show/<int:visual_id>')
def show_visual(visual_id):
    
    return render_template('visual_page.html')

# Update Users Controller

@app.route('/edit/<int:visual_id>', methods=['POST', 'GET'])
def edit_visual(visual_id):
    
    if request.method == 'GET':
        return render_template('edit_visual.html', visual = visual.Visual.get_visual_by_id(visual_id))
    if visual.Visual.update(request.form):
        return redirect('/dashboard')
    return redirect(f'/edit/{visual_id}')


# Delete Users Controller

@app.route('/delete/<int:visual_id>')
def delete(visual_id):
    
    data = {'id' : visual_id}
    visual.Visual.delete(data)
    return redirect('/dashboard')