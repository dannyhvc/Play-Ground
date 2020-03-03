#pragma once

/*******************************

********************************/

//c++ 17 runtime libs
//#include <sstream>
//#include <cassert>

//macros
#define BOOST_TEST_MODULE _DoubleLinkedList

//std libs
#include <iostream>
#include <memory>

//my libs
#include <boost/test/unit_test.hpp>
#include "Complex.hpp"
#include "feedforward.hpp"

//namespaces 
using namespace std;
using namespace NetWorks;


BOOST_AUTO_TEST_CASE(intro)
{
	cout << "\n_DblList unit test, (c) Daniel Herrera\n"
		"Last build: " __TIMESTAMP__ << endl << endl; // last time that the project was compiled.
}

BOOST_AUTO_TEST_CASE(_ff_nn_test)
{
#if true
	unique_ptr<FeedForward> f(new FeedForward(vector<unsigned>({ 3, 1000, 1000 ,1 }), "ReLu"));

	for (size_t i = 0; i < 10; i++)	f->train({ 0.123, 0.456, 0.789 }, { 1.0 }, 1);

	//cout << f->get_output()[0][0];

	//for (size_t i = 0; i < f->get_output().size(); i++)
	//	for (size_t j = 0; j < f->get_output()[i].size(); j++)
	//		cout << f->get_output()[i][j] << endl;

#endif

}//end main()

BOOST_AUTO_TEST_CASE(_complex_test)
{
#if true
	//init
	unique_ptr<Complex> com1(new Complex(1, 2));
	unique_ptr<Complex> com2(new Complex(1, 2));
	Complex com3;

	//sum
	com3 = *com1 + *com2;
	cout << "sum" << endl;
	cout << com3 << '\n' << endl;

	//sub
	com3 = *com1 - *com2;
	cout << "sub" << endl;
	cout << com3 << '\n' << endl;

	//mul
	com3 = *com1 * *com2;
	cout << "mul" << endl;
	cout << com3 << '\n' << endl;

	//mul by const
	com3 = 3 * *com2;
	cout << "mul const" << endl;
	cout << com3 << '\n' << endl;

	//div
	com3 = *com1 / *com2;
	cout << "div" << endl;
	cout << com3 << '\n' << endl;
#endif
}