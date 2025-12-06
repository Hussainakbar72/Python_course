import numpy as np

x = np.array([5,4,3,2])
y = np.array([1200,1100,1000,900])

# multiply x and y
mul = x * y
print("Multiplication of xy =", mul)

# means
meanOfxy = np.mean(mul)
print("Mean of xy =", meanOfxy)

meanOfx = np.mean(x)
print("Mean of x =", meanOfx)

meanOfy = np.mean(y)
print("Mean of y =", meanOfy)

# numerator
MulOfmeanxy = meanOfx * meanOfy
numerator = meanOfxy - MulOfmeanxy
print("Numerator =", numerator)

# x^2
Xsqure = x**2
meanOfXsqure = np.mean(Xsqure)
print("Mean of x^2 =", meanOfXsqure)

squreOFmeanx = meanOfx**2
print("Square of mean x =", squreOFmeanx)

# FIXED denominator
denominator = meanOfXsqure - squreOFmeanx
print("Denominator =", denominator)

# Slope
a = numerator / denominator
print("Slope a =", a)

# Intercept
b = meanOfy - a * meanOfx
print("Intercept b =", b)

# prediction function
def predict(exp):
    return a * exp + b

print("Predicted salary for 7 years:", predict(7))
print("Predicted salary for 10 years:", predict(10))
print("Predicted salary for 0 years:", predict(0))
