from sympy import symbols, Eq, solve

# দ্বিঘাত সমীকরণের জন্য চিহ্নিতকারী চর
x = symbols('x')

# সমীকরণ ইনপুট নেওয়া
equation_str = input("দ্বিঘাত সমীকরণ ইনপুট দিন: ")
equation = Eq(eval(equation_str), 0)

# সমীকরণ সমাধান
solutions = solve(equation, x)

# সমাধানগুলি প্রদর্শন
print(f"সমীকরণের সমাধান: {solutions}")
