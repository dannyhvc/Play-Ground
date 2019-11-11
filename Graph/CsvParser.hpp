#pragma once
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <sstream>
#include <memory>
//using namespace std;

template<typename T = std::string, typename U = std::string>
struct mapper
{
	T				colName_;
	std::vector<U>* colValues_;
};

class CsvParser
{
	std::string	contents_;
	std::ifstream csvFile_;
	std::stringstream SS_;
	std::vector<mapper<>>* structure_;

public:
	inline std::string Contents() const { return this->contents_; }
	inline std::vector<mapper<>>* Structure() const { return this->structure_; }
	void read_csv(std::string const& file_name);
	void parse(void);
};