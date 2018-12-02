
#include <gtest/gtest.h>

#include "../Header/hybrid_lmxrlf.hpp"

using GraphColoring::HybridLmxrlf;

TEST(HybridLmxrlfTests, HybridLmxrlfK5ColorTest) {
    vector<string> node_k1 = { "k2", "k3", "k4", "k5" };
    vector<string> node_k2 = { "k1", "k3", "k4", "k5" };
    vector<string> node_k3 = { "k1", "k2", "k4", "k5" };
    vector<string> node_k4 = { "k1", "k2", "k3", "k5" };
    vector<string> node_k5 = { "k1", "k2", "k3", "k4" };
    map<string,vector<string>> k5 = {{"k1", node_k1}, {"k2", node_k2}, {"k3", node_k3}, {"k4", node_k4}, {"k5", node_k5 }};

    HybridLmxrlf* hybrid_lmxrlf = new HybridLmxrlf(k5);
    map<string,int> resultant = hybrid_lmxrlf->color();
    EXPECT_EQ(resultant.size(), k5.size());
    EXPECT_EQ(hybrid_lmxrlf->get_num_colors(),5);
    delete hybrid_lmxrlf;
}

// TEST(HybridLmxrlfTests, HybridLmxrlfK33ColorTest) {
//     vector<string> side_a = { "k4", "k5", "k6" };
//     vector<string> side_b = { "k1", "k2", "k3" };
//     map<string,vector<string>> k33 = { {"k1", side_a}, {"k2", side_a}, {"k3", side_a}, {"k4", side_b}, {"k5", side_b}, {"k6", side_b} };
    
//     HybridLmxrlf* hybrid_lmxrlf = new HybridLmxrlf(k33);
//     map<string,int> resultant = hybrid_lmxrlf->color();
//     EXPECT_EQ(resultant.size(), k33.size());
//     EXPECT_EQ(hybrid_lmxrlf->get_num_colors(),2);
//     delete hybrid_lmxrlf;
// }

// TEST(HybridLmxrlfTests, HybridLmxrlfEmptyGraphTest) {
//     map<string,vector<string>> empty = map<string,vector<string>>();

//     HybridLmxrlf* hybrid_lmxrlf = new HybridLmxrlf(empty);
//     map<string,int> resultant = hybrid_lmxrlf->color();
//     EXPECT_EQ(resultant.size(), empty.size());
//     delete hybrid_lmxrlf;
// }

// TEST(HybridLmxrlfTests, HybridLmxrlfOneNodeGraphTest) {
//     map<string,vector<string>> one_node = {{ "n", vector<string>() }};

//     HybridLmxrlf* hybrid_lmxrlf = new HybridLmxrlf(one_node);
//     map<string,int> resultant = hybrid_lmxrlf->color();
//     EXPECT_EQ(resultant.size(), one_node.size());
//     EXPECT_EQ(hybrid_lmxrlf->get_num_colors(), 1);
//     delete hybrid_lmxrlf;
// }
