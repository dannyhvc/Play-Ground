//common libraries
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <boost/algorithm/string.hpp>
//headers
#include "CSVReader.hpp"
using namespace std;
using namespace boost;

/*
* Parses through csv file line by line and returns the data
* in vector of vector of strings.
*/
vector<vector<string>> CSVReader::readCSV()
{
	ifstream file(fileName_);
	string line;
	// Iterate through each line and split the content using delimeter
	while (getline(file, line))
	{
		std::vector<std::string> vec;
		algorithm::split(vec, line, is_any_of(delimeter_));
		replace(vec.begin(), vec.end(), "?", "1");
		data_.push_back(vec);
	}//end while
	file.close();
	return this->data_;
}

vector<vector<string>> CSVReader::readCSV_str(string const& data)
{
	istringstream iss(data);
	string line;
	// Iterate through each line and split the content using delimeter
	while (getline(iss, line))
	{
		std::vector<std::string> vec;
		algorithm::split(vec, line, is_any_of(delimeter_));
		replace(vec.begin(), vec.end(), "?", "1");
		data_.push_back(vec);
	}//end while
	return this->data_;
}

string CSVReader::to_string()
{
	ostringstream oss;
	for (auto outr : this->data_)
	{
		for (const auto& inr : outr)
			if (inr != outr[outr.size() - 1])
				oss << inr << ',';
			else
				oss << inr;
		oss << endl;
	}//end for
	return oss.str();
}//end to_string()