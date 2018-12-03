#include <gtest/gtest.h>

#include "../Header/dsatur.hpp"

using GraphColoring::Dsatur;

TEST(DsaturTests, DsaturK5ColorTest) {

    vector<string> node_k1 = { "k14", "k26", "k52", "k56" };
    vector<string> node_k2 = { "k12", "k13", "k17", "k26", "k28", "k32", "k33", "k34", "k39" };
    vector<string> node_k3 = { "k4", "k6", "k9", "k11", "k23", "k35", "k37", "k38", "k39", "k44", "k46", "k51", "k52", "k54" };
    vector<string> node_k4 = { "k2", "k3", "k5", "k7", "k10", "k11", "k13", "k15", "k17", "k24", "k30", "k31", "k32", "k33", "k34", "k35", "k38", "k40", "k42", "k43", "k44", "k48", "k50", "k54", "k55", "k56", "k57", "k60" };
    vector<string> node_k5 = { "k3", "k4", "k19", "k30", "k31", "k37", "k39", "k41", "k56", "k58" };
    vector<string> node_k6 = { "k1", "k7", "k8", "k12", "k14", "k15", "k21", "k22", "k31", "k36", "k44", "k47", "k48", "k49", "k51", "k54", "k55" };
    vector<string> node_k7 = { "k2", "k3", "k14", "k21", "k32", "k37", "k53" };
    vector<string> node_k8 = { "k4", "k7", "k11", "k13", "k22", "k23", "k37", "k51" };
    vector<string> node_k9 = { "k1", "k19", "k28", "k37", "k41", "k47", "k49", "k51", "k59" };
    vector<string> node_k10 = { "k42", "k45" };
    vector<string> node_k11 = { "k1", "k16", "k24", "k25", "k32", "k35", "k41", "k49", "k51", "k53" };
    vector<string> node_k12 = { "k1", "k2", "k3", "k6", "k7", "k9", "k11", "k13", "k14", "k15", "k16", "k17", "k19", "k20", "k21", "k24", "k27", "k28", "k29", "k30", "k32", "k35", "k38", "k39", "k40", "k41", "k42", "k44", "k45", "k47", "k48", "k53", "k54", "k55", "k57", "k58", "k59", "k60" };
    vector<string> node_k13 = { "k1", "k2", "k4", "k5", "k8", "k17", "k19", "k20", "k22", "k23", "k24", "k27", "k28", "k30", "k31", "k32", "k33", "k35", "k36", "k38", "k40", "k42", "k44", "k45", "k47", "k50", "k51", "k58", "k60" };
    vector<string> node_k14 = { "k13", "k26" };
    vector<string> node_k15 = { "k4", "k17", "k24", "k26", "k54", "k58" };
    vector<string> node_k16 = { "k1", "k8", "k10", "k12", "k13", "k14", "k25", "k26", "k27", "k29", "k31", "k32", "k37", "k42", "k44", "k49", "k50", "k54", "k57", "k60" };
    vector<string> node_k17 = { "k7", "k8", "k12", "k19", "k27", "k33", "k34", "k41", "k46", "k47", "k49", "k54" };
    vector<string> node_k18 = { "k4", "k6", "k8", "k10", "k12", "k16", "k20", "k22", "k29", "k32", "k34", "k35", "k36", "k43", "k44", "k51", "k56", "k57", "k59" };
    vector<string> node_k19 = { "k2", "k3", "k5", "k7", "k9", "k11", "k12", "k13", "k16", "k17", "k21", "k22", "k24", "k26", "k27", "k28", "k29", "k30", "k33", "k39", "k40", "k42", "k45", "k47", "k48", "k49", "k50", "k51", "k52", "k53", "k54", "k56", "k57", "k59", "k60" };
    vector<string> node_k20 = { "k8", "k10", "k11", "k16", "k19", "k30", "k36", "k40", "k46", "k47", "k50", "k51", "k58" };
    vector<string> node_k21 = { "k1", "k2", "k4", "k7", "k9", "k11", "k13", "k18", "k19", "k23", "k25", "k41", "k44", "k45", "k47", "k51", "k52", "k54", "k55", "k56", "k57", "k60" };
    vector<string> node_k22 = { "k3", "k4", "k9", "k10", "k12", "k14", "k15", "k27", "k30", "k36", "k37", "k41", "k42", "k43", "k45", "k55", "k60" };
    vector<string> node_k23 = { "k1", "k4", "k7", "k11", "k13", "k15", "k16", "k19", "k20", "k21", "k26", "k32", "k33", "k34", "k35", "k40", "k41", "k44", "k46", "k50", "k51", "k52", "k53", "k55", "k57", "k58" };
    vector<string> node_k24 = { "k20", "k29", "k38", "k40", "k41", "k45", "k47", "k50", "k51", "k52", "k57" };
    vector<string> node_k25 = { "k6", "k7", "k9", "k10", "k14", "k17", "k19", "k20", "k32", "k33", "k36", "k38", "k44", "k48", "k51", "k54" };
    vector<string> node_k26 = { "k27", "k32" };
    vector<string> node_k27 = { "k5", "k10", "k12", "k20", "k22", "k26", "k28", "k29", "k32", "k33", "k36", "k39", "k40", "k43", "k45", "k46", "k47", "k50", "k51", "k52", "k54", "k59", "k60" };
    vector<string> node_k28 = { "k2", "k3", "k4", "k5", "k6", "k7", "k9", "k10", "k11", "k12", "k15", "k16", "k17", "k18", "k19", "k20", "k21", "k23", "k24", "k25", "k26", "k27", "k29", "k30", "k33", "k34", "k35", "k37", "k38", "k39", "k40", "k41", "k43", "k45", "k46", "k47", "k48", "k49", "k50", "k51", "k52", "k53", "k54", "k55", "k56", "k57", "k58", "k59", "k60" };
    vector<string> node_k29 = { "k1", "k27", "k60" };
    vector<string> node_k30 = { "k3", "k7", "k14", "k33", "k37", "k43", "k44", "k45", "k50", "k52" };
    vector<string> node_k31 = { "k13", "k20", "k39", "k55" };
    vector<string> node_k32 = { "k1", "k5", "k9", "k12", "k19", "k23", "k24", "k29", "k40", "k42", "k57" };
    vector<string> node_k33 = { "k1", "k5", "k6", "k7", "k25", "k28", "k29", "k31", "k32", "k35", "k40", "k47", "k53" };
    vector<string> node_k34 = { "k2", "k5", "k8", "k17", "k30", "k37", "k38", "k42" };
    vector<string> node_k35 = { "k3", "k12", "k13", "k19", "k20", "k21", "k23", "k28", "k29", "k30", "k31", "k38", "k44", "k52", "k57" };
    vector<string> node_k36 = { "k10", "k27" };
    vector<string> node_k37 = { "k12", "k39" };
    vector<string> node_k38 = { "k27", "k36", "k39", "k44", "k46", "k54", "k58" };
    vector<string> node_k39 = { "k1", "k3", "k4", "k5", "k6", "k8", "k9", "k10", "k12", "k14", "k15", "k16", "k17", "k22", "k24", "k25", "k28", "k29", "k30", "k31", "k33", "k34", "k36", "k37", "k38", "k41", "k42", "k43", "k45", "k47", "k48", "k49", "k50", "k53", "k54", "k55", "k57", "k58", "k59" };
    vector<string> node_k40 = { "k13", "k36", "k39", "k49" };
    vector<string> node_k41 = { "k1", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k13", "k17", "k18", "k19", "k24", "k26", "k28", "k30", "k31", "k34", "k35", "k36", "k39", "k42", "k43", "k44", "k45", "k48", "k49", "k51", "k52", "k56", "k57", "k58", "k60" };
    vector<string> node_k42 = { "k1", "k7", "k13", "k21", "k23", "k26", "k29", "k30", "k38", "k45", "k46", "k47", "k48", "k52", "k54", "k56", "k58" };
    vector<string> node_k43 = { "k1", "k2", "k5", "k6", "k8", "k9", "k10", "k12", "k13", "k15", "k16", "k17", "k19", "k20", "k21", "k22", "k26", "k27", "k30", "k32", "k35", "k37", "k41", "k44", "k46", "k47", "k48", "k49", "k51", "k53", "k54", "k55", "k58", "k59", "k60" };
    vector<string> node_k44 = { "k3", "k57" };
    vector<string> node_k45 = { "k6", "k9", "k10", "k19", "k33", "k38", "k48", "k51", "k54", "k56", "k60" };
    vector<string> node_k46 = { "k8", "k13", "k26" };
    vector<string> node_k47 = { "k8", "k9", "k12", "k14", "k19", "k22", "k24", "k30", "k37", "k43", "k46" };
    vector<string> node_k48 = { "k3", "k9" };
    vector<string> node_k49 = { "k3", "k5", "k6", "k8", "k10", "k12", "k16", "k20", "k21", "k22", "k23", "k25", "k26", "k28", "k29", "k31", "k32", "k36", "k38", "k42", "k43", "k46", "k48", "k54", "k55", "k56", "k57", "k58" };
    vector<string> node_k50 = { "k5", "k8", "k17", "k34", "k35", "k41", "k45", "k49", "k56", "k60" };
    vector<string> node_k51 = { "k18", "k29", "k44" };
    vector<string> node_k52 = { "k1", "k3", "k4", "k5", "k6", "k8", "k10", "k12", "k13", "k14", "k16", "k18", "k19", "k20", "k21", "k25", "k26", "k27", "k29", "k30", "k31", "k32", "k33", "k35", "k39", "k40", "k41", "k42", "k46", "k47", "k48", "k49", "k51", "k53", "k54", "k56", "k59" };
    vector<string> node_k53 = { "k5", "k7", "k19", "k27" };
    vector<string> node_k54 = { "k2", "k4", "k5", "k7", "k8", "k9", "k10", "k12", "k14", "k17", "k20", "k22", "k25", "k26", "k28", "k29", "k30", "k31", "k33", "k34", "k37", "k41", "k42", "k43", "k46", "k48", "k49", "k50", "k51", "k52", "k53", "k59", "k60" };
    vector<string> node_k55 = { "k3", "k5", "k9", "k12", "k14", "k17", "k19", "k22", "k24", "k25", "k29", "k32", "k33", "k34", "k36", "k37", "k40", "k43", "k45", "k46", "k49", "k50", "k52", "k53", "k54", "k60" };
    vector<string> node_k56 = { "k2", "k3", "k7", "k9", "k16", "k18", "k19", "k20", "k21", "k22", "k23", "k24", "k26", "k28", "k29", "k33", "k35", "k36", "k37", "k39", "k43", "k49", "k50", "k53", "k55", "k58" };
    vector<string> node_k57 = { "k2", "k6", "k11", "k12", "k14", "k17", "k18", "k20", "k25", "k37", "k39", "k45", "k47", "k55" };
    vector<string> node_k58 = { "k4", "k5", "k8", "k9", "k12", "k14", "k17", "k18", "k24", "k25", "k27", "k28", "k32", "k33", "k36", "k39", "k41", "k43", "k44", "k46", "k47", "k49", "k53", "k55", "k56" };
    vector<string> node_k59 = { "k2", "k7", "k11", "k13", "k22", "k23", "k24", "k31", "k32", "k33", "k40", "k41", "k49", "k51", "k52", "k54", "k55", "k57" };
    vector<string> node_k60 = { "k32", "k45" };
    map<string,vector<string>> k60 = { {"k1", node_k1}, {"k2", node_k2}, {"k3", node_k3}, {"k4", node_k4}, {"k5", node_k5}, {"k6", node_k6}, {"k7", node_k7}, {"k8", node_k8}, {"k9", node_k9}, {"k10", node_k10}, {"k11", node_k11}, {"k12", node_k12}, {"k13", node_k13}, {"k14", node_k14}, {"k15", node_k15}, {"k16", node_k16}, {"k17", node_k17}, {"k18", node_k18}, {"k19", node_k19}, {"k20", node_k20}, {"k21", node_k21}, {"k22", node_k22}, {"k23", node_k23}, {"k24", node_k24}, {"k25", node_k25}, {"k26", node_k26}, {"k27", node_k27}, {"k28", node_k28}, {"k29", node_k29}, {"k30", node_k30}, {"k31", node_k31}, {"k32", node_k32}, {"k33", node_k33}, {"k34", node_k34}, {"k35", node_k35}, {"k36", node_k36}, {"k37", node_k37}, {"k38", node_k38}, {"k39", node_k39}, {"k40", node_k40}, {"k41", node_k41}, {"k42", node_k42}, {"k43", node_k43}, {"k44", node_k44}, {"k45", node_k45}, {"k46", node_k46}, {"k47", node_k47}, {"k48", node_k48}, {"k49", node_k49}, {"k50", node_k50}, {"k51", node_k51}, {"k52", node_k52}, {"k53", node_k53}, {"k54", node_k54}, {"k55", node_k55}, {"k56", node_k56}, {"k57", node_k57}, {"k58", node_k58}, {"k59", node_k59}, {"k60", node_k60} };

    Dsatur* dsatur = new Dsatur(k60);

    map<string,int> resultant = dsatur->color();

    delete dsatur;

}