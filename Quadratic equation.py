import cmath as ma
a,b,c=int(input()),int(input()),int(input())
print((-b-ma.sqrt((b**2)-(4*a*c)))/(2*a),(-b+ma.sqrt((b**2)-(4*a*c)))/(2*a))