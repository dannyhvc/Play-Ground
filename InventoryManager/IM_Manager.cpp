
// boost manager
#define BOOST_TEST_MODULE _I_M_
#include <boost/test/unit_test.hpp>

// Libraries
#include <iostream>
#include <vector>
#include <map>
using namespace std;

BOOST_AUTO_TEST_CASE(__intro__)
{
	cout << "Welcome to CMD inventory Manager" << endl;
	cout << "Last update compiled: " << __TIMESTAMP__ << endl;
}

BOOST_AUTO_TEST_CASE(__main__)
{

}


