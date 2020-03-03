/**************************************
 * Name: Daniel Herrera-Vazquez
 * Date: Dec 4, 2019
 * Desc:
 **************************************/
#include <iostream>
#include "CSVReader.hpp"
using namespace std;

// ============================== DEBUG ============================//
#ifdef _DEBUG
/**
 * \brief
 */
#define BOOST_TEST_MODULE mytest 
#include <boost/test/unit_test.hpp>

BOOST_AUTO_TEST_CASE(test1)
{
	CSVReader reader("Test_Csv.csv");
	reader.readCSV();
	cout << reader << endl;
}
#endif // _DEBUG

// ============================== RELEASE ============================//
#ifndef _DEBUG
int main(int argv, char** argc)
{
	CSVReader reader("Test_Csv.csv");
	cout << reader.to_string() << endl;
}
#endif // !1