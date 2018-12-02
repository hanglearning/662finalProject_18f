
#include <gtest/gtest.h>

#include "../Header/mcs.hpp"

using GraphColoring::Mcs;

TEST(McsTests, McsK5ColorTest) {
    vector<string> node_k1 = { "k2", "k3", "k4", "k5" };
    vector<string> node_k2 = { "k1", "k3", "k4", "k5" };
    vector<string> node_k3 = { "k1", "k2", "k4", "k5" };
    vector<string> node_k4 = { "k1", "k2", "k3", "k5" };
    vector<string> node_k5 = { "k1", "k2", "k3", "k4" };
    map<string,vector<string>> k5 = {{"k1", node_k1}, {"k2", node_k2}, {"k3", node_k3}, {"k4", node_k4}, {"k5", node_k5 }};
    
    Mcs* mcs = new Mcs(k5);
    map<string,int> resultant = mcs->color();
    EXPECT_EQ(resultant.size(), k5.size());
    EXPECT_EQ(mcs->get_num_colors(),5);
    delete mcs;
}

// TEST(McsTests, McsK33ColorTest) {
//     vector<string> side_a = { "k4", "k5", "k6" };
//     vector<string> side_b = { "k1", "k2", "k3" };
//     map<string,vector<string>> k33 = { {"k1", side_a}, {"k2", side_a}, {"k3", side_a}, {"k4", side_b}, {"k5", side_b}, {"k6", side_b} };
    
//     Mcs* mcs = new Mcs(k33);
//     map<string,int> resultant = mcs->color();
//     EXPECT_EQ(resultant.size(), k33.size());
//     EXPECT_EQ(mcs->get_num_colors(),2);
//     delete mcs;
// }

// TEST(McsTests, McsEmptyGraphTest) {
//     map<string,vector<string>> empty = map<string,vector<string>>();

//     Mcs* mcs = new Mcs(empty);
//     map<string,int> resultant = mcs->color();
//     EXPECT_EQ(resultant.size(), empty.size());
//     delete mcs;
// }

// TEST(McsTests, McsOneNodeGraphTest) {
//     map<string,vector<string>> one_node = {{ "n", vector<string>() }};

//     Mcs* mcs = new Mcs(one_node);
//     map<string,int> resultant = mcs->color();
//     EXPECT_EQ(resultant.size(), one_node.size());
//     EXPECT_EQ(mcs->get_num_colors(),1);
//     delete mcs;
// }
