#pragma once



#include "master.h"

namespace tensor
{
	class Math_Transform
	{

	private:
		decimal seed;


	public:
		static decimal randomValue(decimal lower_bound, decimal upper_bound);
		static m1d createRandomArray(unsigned size, decimal lower_bound, decimal upper_bound);
		static m2d createRandomArray(unsigned sizeX, unsigned sizeY, decimal lower_bound, decimal upper_bound);


	public:
		inline static decimal sigmoid(decimal x) { return 1.0 / 1.0 + (exp(-x)); }
		inline static decimal sigdiv(decimal x) { return x * (1 - x); }

		inline static decimal ReLu(decimal x) { return (x < 0) ? 0 : x; }
		inline static decimal ReLu_div(decimal x) { return (x < 0) ? 0 : 1; }

		inline static m2d sigmoid(m2d const& a);

	};
}

