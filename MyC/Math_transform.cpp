#pragma once

#include "Math_transform.hpp"

using namespace tensor;

m1d Math_Transform::createRandomArray(unsigned size, decimal lower_bound, decimal upper_bound)
{
	if (size < 1)
		throw exception("One or more of the sizes were to small.");

	m1d rand_arr(size);

	for (unsigned i = 0; i < size; i++)
		rand_arr[i] = Math_Transform::randomValue(lower_bound, upper_bound);

	return rand_arr;
}


m2d tensor::Math_Transform::createRandomArray(unsigned sizeX, unsigned sizeY, decimal lower_bound, decimal upper_bound)
{
	m2d rand_arr(sizeX);

	for (unsigned i = 0; i < sizeX; i++)
		rand_arr[i] = Math_Transform::createRandomArray(sizeY, lower_bound, upper_bound);

	return rand_arr;
}


decimal Math_Transform::randomValue(decimal lower_bound, decimal upper_bound)
{
	return (((decimal)rand()) / (decimal)(RAND_MAX + 1)) * (decimal)(upper_bound - lower_bound + 1.0) + lower_bound;
}


m2d Math_Transform::sigmoid(m2d const& a)
{
	auto m = a.size();
	auto n = a[0].size();
	m2d z(m);

	for (unsigned i = 0; i < m; i++)
		z[i].resize(n);

	for (unsigned i = 0; i < m; i++)
		for (unsigned j = 0; j < n; j++)
			z[i][j] = (1.0 / (1 + exp(-a[i][j])));

	return z;
}//end sigmoid

