#pragma once
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <utility>
#include <sstream>
#include <memory>
#include <iostream>
using namespace std;

// ================================== CsvParser <CLASS DEFINITION> ================================== //
class CsvParser
{
private:
	// computational members
	string	contents_;
	ifstream csvFile_;
	stringstream SS_;

	// data members
	vector< string> names_;
	vector< vector< string>> values_;

public:

	CsvParser() = default;
	~CsvParser();

	//functions
	std::string Contents() const { return this->contents_; }
	void read(std::string const& file_name);
	void parse(void);

	inline std::string to_string(void)
	{
		std::stringstream ss;
		for (auto str : names_)
			ss << str << ' ';
		for (size_t i = 0; i < values_.size(); ++i)
		{
			for (size_t j = 0; j < values_[j].size(); ++j)
				for (size_t k = 0; k < values_[k].size(); ++k)
					ss << values_[i][j] << ' ';
			ss << "\n";
		}
		return ss.str();
	}

	//operators
	inline std::ostream& operator << (std::ostream& oss);
};

inline std::ostream& CsvParser::operator<<(std::ostream& oss)
{
	return oss << this->to_string();
}