from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'pipeline-secret-key'

# In-memory list to store registrations (no database needed)
registrations = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name  = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        event = request.form.get('event', '').strip()

        # Validate: all fields must be filled
        if not name or not email or not event:
            flash('All fields are required.', 'error')
        else:
            registrations.append({
                'name':  name,
                'email': email,
                'event': event
            })
            flash(f'Successfully registered {name} for {event}!', 'success')
            return redirect(url_for('index'))

    return render_template('index.html', registrations=registrations)


@app.route('/health')
def health():
    """Health check endpoint used by the CI pipeline to verify the app is alive."""
    return {'status': 'ok'}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7002, debug=True)