#pragma once

/*
Author: Daniel Herrera
Date (revised): Spet 24, 2019.

using boost lib
*/

#include "feedforward.hpp"
using namespace NetWorks;


FeedForward::FeedForward(vector<unsigned> const& net_lay_size, string const& afunc)
{
	//OIII
	// object instantiation is init.
	this->_Network_Layer_Size = net_lay_size;
	this->_Network_size = net_lay_size.size();
	this->_Input_size = net_lay_size[0];
	this->_output_size = net_lay_size[_Network_size - 1];

	this->_output.resize(_Network_size);
	this->_weights.resize(_Network_size);
	this->_bias.resize(_Network_size);

	this->_error_signal.resize(_Network_size);
	this->_output_derivative.resize(_Network_size);

	this->activeFunction = afunc;


	//sets the weights and bias's for the network.
	for (unsigned i = 0; i < _Network_size; i++) {
		this->_output[i].resize(_Network_Layer_Size[i]);
		this->_error_signal[i].resize(_Network_Layer_Size[i]);
		this->_output_derivative[i].resize(_Network_Layer_Size[i]);

		this->_bias[i] = tensor::Math_Transform::createRandomArray(_Network_Layer_Size[i], -1, 1);

		if (i > 0)
			_weights[i] = tensor::Math_Transform::createRandomArray(
				_Network_Layer_Size[i], _Network_Layer_Size[i - 1], -1, 1
			);
	}//end for
}//end constructor ff


decimal FeedForward::activation(string const& afunc, decimal const& x)
{
	if (afunc.compare("sigmoid"))
		return tensor::Math_Transform::sigmoid(x);
	else if (afunc.compare("ReLu"))
		return tensor::Math_Transform::ReLu(x);
	else
		throw exception("Invalid function type");
}//end activation()


void FeedForward::backpropError(m1d const& target)
{
	for (size_t neuron = 0; neuron < _Network_Layer_Size[_Network_size - 1]; neuron++)
		_error_signal[_Network_size - 1][neuron] = (_output[_Network_size - 1][neuron] - target[neuron])
		* _output_derivative[_Network_size - 1][neuron];

	/*
	  @IMPORTANT starts at n-2 because it it where the last neuron is located
	 */
	for (size_t layer = _Network_size - 2; layer > 0; layer--)
		for (size_t neuron = 0; neuron < _Network_Layer_Size[layer]; neuron++) {
			decimal sum = 0;
			for (size_t nextNeuron = 0; nextNeuron < _Network_Layer_Size[layer + 1]; nextNeuron++)
				sum += _weights[layer + 1][nextNeuron][neuron] * _error_signal[layer + 1][nextNeuron];
			this->_error_signal[layer][neuron] = sum * _output_derivative[layer][neuron];
		}//end for #neuron#

}//end backpropError()


decimal FeedForward::deActive(string const& afunc, decimal const& x)
{
	if (afunc.compare("sigmoid"))
		return tensor::Math_Transform::sigdiv(x);
	else if (afunc.compare("ReLu"))
		return tensor::Math_Transform::ReLu_div(x);
	else
		throw exception("Invalid activation function(2).");
}//end deActive()


m1d FeedForward::think(m1d const& input)
{
	if (input.size() != this->_Input_size)
		throw exception("Invalid matrix");
	this->_output[0] = input;

	for (unsigned layer = 1; layer < _Network_size; layer++)
		for (unsigned neuron = 0; neuron < _Network_Layer_Size[layer]; neuron++) {
			decimal sum = _bias[layer][neuron];
			for (unsigned prevNeuron = 0; prevNeuron < _Network_Layer_Size[layer - 1]; prevNeuron++)
				sum += _output[layer - 1][prevNeuron] * _weights[layer][neuron][prevNeuron];

			_output[layer][neuron] = activation(activeFunction, sum);
			_output_derivative[layer][neuron] = deActive(activeFunction, _output[layer][neuron]);
		}//end for $neuron$

	return _output[_Network_size - 1];
}//end think()


void FeedForward::train(m1d const& t_inputs, m1d const& target, decimal eta)
{
	if (t_inputs.size() != _Input_size || target.size() != _output_size)
		throw exception("Invalid matrix exception");
	this->think(t_inputs);
	this->backpropError(target);
	this->updateSynapse(eta);
	cout << MSE(t_inputs, target) << endl;
}//end train()


void FeedForward::updateSynapse(decimal const& eta)
{
	for (unsigned layer = 1; layer < _Network_size; layer++)
		for (unsigned neuron = 0; neuron < _Network_Layer_Size[layer]; neuron++) {
			decimal deltaBi = -eta * _error_signal[layer][neuron];
			_bias[layer][neuron] += deltaBi;
			for (unsigned prevNeuron = 0; prevNeuron < _Network_Layer_Size[layer - 1]; prevNeuron++)
				_weights[layer][neuron][prevNeuron] += deltaBi * _output[layer - 1][prevNeuron];
		}//end for #neuron#

}//end updateSynapse()


decimal FeedForward::MSE(m1d const& t_input, m1d const& target)
{
	if (t_input.size() != _Input_size || target.size() != _output_size)
		throw exception("" + t_input.size());
	think(t_input);

	decimal v = 0.0L;
	for (unsigned i = 0; i < target.size(); i++)
		v += pow((target[i] - _output[_Network_size - 1][i]), 2);

	return v / (2.0L * target.size());
}//end MSE()

ostream& operator<<(ostream& oss, FeedForward& _left)
{
	for (size_t i = 0; i < _left.get_output().size(); i++)
		for (size_t j = 0; j < _left.get_output()[i].size(); j++)
			oss << _left.get_output()[i][j] << endl;
	return oss;
}