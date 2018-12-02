
#include <gtest/gtest.h>

#include "../Header/dsatur.hpp"

using GraphColoring::Dsatur;

TEST(DsaturTests, DsaturK5ColorTest) {
    vector<string> node_k1 = { "k2" };
    vector<string> node_k2 = { "k1", "k6" };
    vector<string> node_k3 = { "k1", "k2" };
    vector<string> node_k4 = { "k1", "k2", "k6" };
    vector<string> node_k5 = { "k1",  "k4", "k6" };
    vector<string> node_k6 = { "k1", "k2" };
    map<string,vector<string>> k6 = {{"k1", node_k1}, {"k2", node_k2}, {"k3", node_k3}, {"k4", node_k4}, {"k5", node_k5 }, {"k6", node_k6 }};
    
    Dsatur* dsatur = new Dsatur(k6);

    std::cout << (dsatur->is_colored()) << std::endl;
    map<string,int> resultant = dsatur->color();
    //
    std::cout << (dsatur->is_colored()) << std::endl;
    // dsatur->verify();
    dsatur->print_coloring();
    //std::cout << (dsatur->print_coloring()) << std::endl; //prints each node (by name) and it's color (int)
    EXPECT_EQ(resultant.size(), k6.size());
    //EXPECT_EQ(dsatur->get_num_colors(),6);
    delete dsatur;
}

// TEST(DsaturTests, DsaturK33ColorTest) {
//     vector<string> side_a = { "k4", "k5", "k6" };
//     vector<string> side_b = { "k1", "k2", "k3" };
//     map<string,vector<string>> k33 = { {"k1", side_a}, {"k2", side_a}, {"k3", side_a}, {"k4", side_b}, {"k5", side_b}, {"k6", side_b} };
    
//     Dsatur* dsatur = new Dsatur(k33);
//     map<string,int> resultant = dsatur->color();
//     EXPECT_EQ(resultant.size(), k33.size());
//     EXPECT_EQ(dsatur->get_num_colors(),2);
//     delete dsatur;
// }

// TEST(DsaturTests, DsaturEmptyGraphTest) {
//     map<string,vector<string>> empty = map<string,vector<string>>();

//     Dsatur* dsatur = new Dsatur(empty);
//     map<string,int> resultant = dsatur->color();
//     EXPECT_EQ(resultant.size(), empty.size());
//     delete dsatur;
// }

// TEST(DsaturTests, DsaturOneNodeGraphTest) {
//     map<string,vector<string>> one_node = {{ "n", vector<string>() }};

//     Dsatur* dsatur = new Dsatur(one_node);
//     map<string,int> resultant = dsatur->color();
//     EXPECT_EQ(resultant.size(), one_node.size());
//     EXPECT_EQ(dsatur->get_num_colors(),1);
//     delete dsatur;
// }
