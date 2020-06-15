from flask import Flask, render_template, request, redirect, escape, session, copy_current_request_context

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login_page() -> 'html':
    return render_template('login.html', title='Login - Memories: Overflow')

if __name__ == '__main__':
    app.run(port='5500', debug = True)