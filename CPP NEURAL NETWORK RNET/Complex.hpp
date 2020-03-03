#pragma once

#include <iostream>
#include <cassert>

class Complex
{
private:
	double _a, _b;


public:
	Complex() = default;
	Complex(double real, double imaginary) :
		_a(real), _b(imaginary) {}

	inline double find_2d_theta(double& x, double& y) { return atan(y / x); }

	constexpr double get_a() { return this->_a; }
	constexpr double get_b() { return this->_b; }


public:
	// arethmatic operator overload
	friend Complex operator + (Complex& lhs, Complex& rhs);
	friend Complex operator - (Complex& lhs, Complex& rhs);
	friend Complex operator * (Complex& lhs, Complex& rhs);
	friend Complex operator * (double const& constant, Complex& rhs);
	friend Complex operator / (Complex& lhs, Complex& oc);

	// io op overload
	friend std::ostream& operator << (std::ostream& out, Complex& oc);

};