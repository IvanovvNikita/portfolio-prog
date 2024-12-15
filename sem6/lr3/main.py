#Лабораторная работа №3
# Иванов Никита
from flask import Flask
from utils import Memoize
app = Flask(__name__)
memoized = Memoize()


@app.route('/')
def index():
    return 'Hello world!'

@app.route('/about')
def about():
    return 'Nikita Ivanov'

@app.route('/calc/<string:func>/<int:n>')
def factorial(func: str, n: int):
    return factorial_helper(func, n)


@memoized
def factorial_helper(func: str, n: int):
    from math import factorial as f1
    from scipy.special import factorial as f2
    if func == "f1":
        return str(f1(n))
    elif func == "f2":
        return str(int(f2(n)))

    return ""


if __name__ == '__main__':
    cache_path = "cache.json"
    memoized.load_cache(cache_path)
    
    app.run(host='0.0.0.0', port=80)
    
    memoized.dump_cache(cache_path)
    

  