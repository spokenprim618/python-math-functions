from flask import Flask, render_template, request, redirect, url_for
from logic.arithmetic import calculate as arit_calc, get_history as arit_hist, delete_from_history as arit_del
from logic.geo import calculate as geo_calc, get_history as geo_hist, delete_from_history as geo_del
from logic.quadratic import QuadraticCalculator, get_history as quad_hist, add_to_history as quad_add, delete_from_history as quad_del
from logic.percent_error import calculate as pe_calc, get_history as pe_hist, add_to_history as pe_add, delete_from_history as pe_del
from logic.law_of_cosines import calculate_sides, calculate_angles, get_history as loc_hist, add_to_history as loc_add, delete_from_history as loc_del
from linkedPack import LinkedList, Node
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/arithmetic', methods=['GET', 'POST'])
def arithmetic():
    result = None
    calc_type = "arithmetic"

    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        nth = float(request.form['nth'])
        calc_type = request.form['type']

        if calc_type == 'arithmetic':
            result = arit_calc(n1, n2, nth)
        elif calc_type == 'geometric':
            result = geo_calc(n1, n2, nth)

    results = arit_hist() if calc_type == 'arithmetic' else geo_hist()
    return render_template('arithmetic.html', result=result, results=results, calc_type=calc_type)

@app.route('/delete/<calc_type>/<int:index>', methods=['POST'])
def delete_result(calc_type, index):
    if calc_type == "arithmetic":
        arit_del(index)
    elif calc_type == "geometric":
        geo_del(index)
    elif calc_type == "quadratic":
        quad_del(index)
    elif calc_type == "percent_error":
        pe_del(index)
    elif calc_type == "law_of_cosines":
        loc_del(index)
    return redirect(url_for(calc_type.replace('-', '_')) if '-' in calc_type else redirect(url_for(calc_type)))

@app.route('/quadratic', methods=['GET', 'POST'])
def quadratic():
    result = None
    calculation_type = None
    inputs = None
    
    if request.method == 'POST':
        if 'orientation' in request.form:
            a = request.form.get('a')
            calculation_type = "orientation"
            result = QuadraticCalculator.get_orientation(a)
            inputs = {'a': a}
            
        elif 'vertex' in request.form:
            a = request.form.get('a')
            b = request.form.get('b')
            calculation_type = "vertex"
            result = QuadraticCalculator.find_vertex(a, b)
            inputs = {'a': a, 'b': b}
            
        elif 'evaluate' in request.form:
            a = request.form.get('a')
            b = request.form.get('b')
            c = request.form.get('c')
            x = request.form.get('x')
            calculation_type = "evaluation"
            result = QuadraticCalculator.evaluate_equation(a, b, c, x)
            inputs = {'a': a, 'b': b, 'c': c, 'x': x}
            
        elif 'solve' in request.form:
            a = request.form.get('a')
            b = request.form.get('b')
            c = request.form.get('c')
            calculation_type = "solution"
            root1, root2 = QuadraticCalculator.solve_quadratic(a, b, c)
            result = (root1, root2)
            inputs = {'a': a, 'b': b, 'c': c}
        
        if calculation_type and inputs and result:
            quad_add(calculation_type, inputs, result)
    
    history = quad_hist()
    return render_template('quadratic.html', result=result, history=history)

@app.route('/percent_error', methods=['GET', 'POST'])
def percent_error():
    result = None
    if request.method == 'POST':
        experimental = float(request.form.get('experimental'))
        actual = float(request.form.get('actual'))
        
        try:
            result = pe_calc(experimental, actual)
            pe_add(experimental, actual, result)
        except ZeroDivisionError:
            result = "Error: Actual value cannot be zero"
    
    history = pe_hist()
    return render_template('percent_error.html', result=result, history=history)

@app.route('/law_of_cosines', methods=['GET', 'POST'])
def law_of_cosines():
    sides_result = None
    angles_result = None
    
    if request.method == 'POST':
        if 'side_submit' in request.form:
            a = float(request.form.get('side1', 0))
            b = float(request.form.get('side2', 0))
            c = float(request.form.get('side3', 0))
            A = float(request.form.get('angle1', 0))
            B = float(request.form.get('angle2', 0))
            C = float(request.form.get('angle3', 0))
            
            sides_result = calculate_sides(a, b, c, A, B, C)
            loc_add('sides', {'a': a, 'b': b, 'c': c, 'A': A, 'B': B, 'C': C}, sides_result)
        
        elif 'angle_submit' in request.form:
            a = float(request.form.get('a1', 0))
            b = float(request.form.get('b1', 0))
            c = float(request.form.get('c1', 0))
            
            angles_result = calculate_angles(a, b, c)
            loc_add('angles', {'a': a, 'b': b, 'c': c}, angles_result)
    
    history = loc_hist()
    return render_template('law_of_cosines.html', 
                         sides_result=sides_result, 
                         angles_result=angles_result,
                         history=history)

if __name__ == '__main__':
    app.run(debug=True)