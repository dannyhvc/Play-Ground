#pragma once
#include "Complex.hpp"


Complex operator + (Complex& lhs, Complex& rhs)
{
	return Complex(
		(lhs._a + rhs._a),
		(lhs._b + rhs._b)
	);
}


Complex operator - (Complex& lhs, Complex& rhs)
{
	return Complex(
		(lhs._a - rhs._a),
		(lhs._b - rhs._b)
	);
}


Complex operator * (Complex& lhs, Complex& rhs)
{
	return Complex(
		(lhs._a * rhs._a) - (lhs._b * rhs._b),
		(lhs._a * rhs._b) + (lhs._b * rhs._a)
	);
}


Complex operator*(double const& constant, Complex& oc)
{
	return Complex(
		constant * oc._a,
		constant * oc._b
	);
}


Complex operator / (Complex& lhs, Complex& rhs)
{
	//assert((rhs * rhs)._a != 0);

	return Complex(
		(lhs * rhs)._a / (rhs * rhs)._a,
		(lhs * rhs)._b / (rhs * rhs)._b
	);
}


std::ostream& operator << (std::ostream& out, Complex& oc)
{
	// TODO: insert return statement here
	out << oc._a << '+' << oc._b << 'i';
	return out;
}

