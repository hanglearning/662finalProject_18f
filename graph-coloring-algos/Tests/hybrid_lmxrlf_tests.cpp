#include <gtest/gtest.h>

#include "../Header/hybrid_lmxrlf.hpp"

using GraphColoring::HybridLmxrlf;

TEST(HybridLmxrlfTests, HybridLmxrlfK5ColorTest) {

    vector<string> node_Tasmania = {};
    vector<string> node_Western_Australia = {"Northern_Territory", "South_Australia"};
    vector<string> node_Northern_Territory = {"Western_Australia", "South_Australia","Queensland"};
    vector<string> node_South_Australia = {"Western_Australia", "Northern_Territory", "Queensland", "New_South_Wales", "Victoria"};
    vector<string> node_Queensland = {"Northern_Territory", "South_Australia", "New_South_Wales"};
    vector<string> node_New_South_Wales = {"Queensland", "South_Australia", "Victoria"};
    vector<string> node_Victoria = {"South_Australia", "New_South_Wales"};
    map<string,vector<string>> kaus = {{"Tasmania", node_Tasmania}, {"Western_Australia", node_Western_Australia}, {"Northern_Territory", node_Northern_Territory}, {"South_Australia", node_South_Australia}, {"Queensland", node_Queensland },{"New_South_Wales",node_New_South_Wales},{"Victoria",node_Victoria}};

    HybridLmxrlf* hybrid_lmxrlf = new HybridLmxrlf(kaus);

    map<string,int> resultant = hybrid_lmxrlf->color();

    delete hybrid_lmxrlf;

}