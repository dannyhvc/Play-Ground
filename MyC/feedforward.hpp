#pragma once
#include "master.h"
#include "Math_transform.hpp"

namespace NetWorks
{
	class FeedForward
	{
		/*
		Defining the private feilds.
		*/
		vector<unsigned>  _Network_Layer_Size;
		size_t			  _Network_size;
		size_t			  _Input_size;
		size_t			  _output_size;

		m2d	_output;
		m3d	_weights;
		m2d	_bias;

		m2d	_error_signal;
		m2d	_output_derivative;

		string activeFunction;


	private:
		decimal MSE(m1d const& t_input, m1d const& target);
		void backpropError(m1d const& target);
		void updateSynapse(decimal const& eta);


	public:
		/*
		Constructors and destructors in this public modifier declaration.
		*/
		FeedForward(vector<unsigned> const& net_lay_size, string const& afunc);

		//getters
		vector<unsigned> get_Network_Layer_Size() { return this->_Network_Layer_Size; }
		size_t get_Network_size() { return this->_Network_size; }
		size_t get_Input_size() { return this->_Input_size; }
		size_t get_output_size() { return this->_output_size; }

		// accessors
		inline m2d get_output() { return this->_output; }//end get_output()
		inline m3d get_weights() { return this->_weights; }
		inline m2d get_bias() { return this->_bias; }
		inline m2d getError_S() { return this->_error_signal; }
		inline m2d get_output_D() { return this->_output_derivative; }


	public:
		// cognitive data mutation done by the neural network.
		m1d think(m1d const& input);
		decimal activation(string const& afunc, decimal const& x);
		decimal deActive(string const& afunc, decimal const& x);
		void train(m1d const& t_inputs, m1d const& target, decimal eta);
	};//end class

};

ostream& operator <<(ostream& oss, NetWorks::FeedForward& _left);
