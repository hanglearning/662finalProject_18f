#include <gtest/gtest.h>

#include "../Header/hybrid_lmxrlf.hpp"

using GraphColoring::HybridLmxrlf;

TEST(HybridLmxrlfTests, HybridLmxrlfK5ColorTest) {

    vector<string> node_Alaska = {};
    vector<string> node_Alabama = { "Mississippi" , "Tennessee" , "Georgia" , "Florida" };
    vector<string> node_Arkansas = { "Missouri" , "Tennessee" , "Mississippi" , "Louisiana" , "Texas" , "Oklahoma" , "Oklahoma" };
    vector<string> node_Arizona = { "California" , "Nevada" , "Utah" , "Colorado" , "New_Mexico" };
    vector<string> node_California = { "Oregon" , "Nevada" , "Arizona" };
    vector<string> node_Colorado = { "Wyoming" , "Nebraska" , "Kansas" , "Oklahoma" , "New_Mexico" , "Arizona" , "Arizona" , "Utah" };
    vector<string> node_Connecticut = { "New_York" , "Massachusetts" , "Rhode_Island" };
    vector<string> node_Delaware = { "Maryland" , "Pennsylvania" , "New_Jersey" };
    vector<string> node_Florida = { "Alabama" , "Georgia" };
    vector<string> node_Georgia = { "Florida" , "Alabama" , "Tennessee" , "North_Carolina" , "South_Carolina" };
    vector<string> node_Hawaii = {};
    vector<string> node_Iowa = { "Minnesota" , "Wisconsin" , "Illinois" , "Missouri" , "Nebraska" , "South_Dakota" , "South_Dakota" };
    vector<string> node_Idaho = { "Montana" , "Wyoming" , "Utah" , "Nevada" , "Oregon" , "Washington" , "Washington" };
    vector<string> node_Illinois = { "Indiana" , "Kentucky" , "Missouri" , "Iowa" , "Wisconsin" };
    vector<string> node_Indiana = { "Michigan" , "Ohio" , "Kentucky" , "Illinois" };
    vector<string> node_Kansas = { "Nebraska" , "Missouri" , "Oklahoma" , "Colorado" };
    vector<string> node_Kentucky = { "Indiana" , "Ohio" , "West_Virginia" , "Virginia" , "Tennessee" , "Missouri" , "Missouri" , "Illinois" };
    vector<string> node_Louisiana = { "Texas" , "Arkansas" , "Mississippi" };
    vector<string> node_Massachusetts = { "Rhode_Island" , "Connecticut" , "New_York" , "New_Hampshire" , "Vermont" };
    vector<string> node_Maryland = { "Virginia" , "West_Virginia" , "Pennsylvania" , "Delaware" };
    vector<string> node_Maine = { "New_Hampshire" };
    vector<string> node_Michigan = { "Wisconsin" , "Indiana" , "Ohio" };
    vector<string> node_Minnesota = { "Wisconsin" , "Iowa" , "South_Dakota" , "North_Dakota" };
    vector<string> node_Missouri = { "Iowa" , "Illinois" , "Kentucky" , "Tennessee" , "Arkansas" , "Oklahoma" , "Oklahoma" , "Kansas" , "Nebraska" };
    vector<string> node_Mississippi = { "Louisiana" , "Arkansas" , "Tennessee" , "Alabama" };
    vector<string> node_Montana = { "North_Dakota" , "South_Dakota" , "Wyoming" , "Idaho" };
    vector<string> node_North_Carolina = { "Virginia" , "Tennessee" , "Georgia" , "South_Carolina" };
    vector<string> node_North_Dakota = { "Minnesota" , "South_Dakota" , "Montana" };
    vector<string> node_Nebraska = { "South_Dakota" , "Iowa" , "Missouri" , "Kansas" , "Colorado" , "Wyoming" , "Wyoming" };
    vector<string> node_New_Hampshire = { "Vermont" , "Maine" , "Massachusetts" };
    vector<string> node_New_Jersey = { "Delaware" , "Pennsylvania" , "New_York" };
    vector<string> node_New_Mexico = { "Arizona" , "Utah" , "Colorado" , "Oklahoma" , "Texas" };
    vector<string> node_Nevada = { "Idaho" , "Utah" , "Arizona" , "California" , "Oregon" };
    vector<string> node_New_York = { "New_Jersey" , "Pennsylvania" , "Vermont" , "Massachusetts" , "Connecticut" };
    vector<string> node_Ohio = { "Pennsylvania" , "West_Virginia" , "Kentucky" , "Indiana" , "Michigan" };
    vector<string> node_Oklahoma = { "Kansas" , "Missouri" , "Arkansas" , "Texas" , "New_Mexico" , "Colorado" , "Colorado" };
    vector<string> node_Oregon = { "California" , "Nevada" , "Idaho" , "Washington" };
    vector<string> node_Pennsylvania = { "New_York" , "New_Jersey" , "Delaware" , "Maryland" , "West_Virginia" , "Ohio" , "Ohio" };
    vector<string> node_Rhode_Island = { "Connecticut" , "Massachusetts" };
    vector<string> node_South_Carolina = { "Georgia" , "North_Carolina" };
    vector<string> node_South_Dakota = { "North_Dakota" , "Minnesota" , "Iowa" , "Nebraska" , "Wyoming" , "Montana" , "Montana" };
    vector<string> node_Tennessee = { "Kentucky" , "Virginia" , "North_Carolina" , "Georgia" , "Alabama" , "Mississippi" , "Mississippi" , "Arkansas" , "Missouri" };
    vector<string> node_Texas = { "New_Mexico" , "Oklahoma" , "Arkansas" , "Louisiana" };
    vector<string> node_Utah = { "Idaho" , "Wyoming" , "Colorado" , "New_Mexico" , "Arizona" , "Nevada" , "Nevada" };
    vector<string> node_Virginia = { "North_Carolina" , "Tennessee" , "Kentucky" , "West_Virginia" , "Maryland" };
    vector<string> node_Vermont = { "New_York" , "New_Hampshire" , "Massachusetts" };
    vector<string> node_Washington = { "Idaho" , "Oregon" };
    vector<string> node_Wisconsin = { "Michigan" , "Minnesota" , "Iowa" , "Illinois" };
    vector<string> node_West_Virginia = { "Ohio" , "Pennsylvania" , "Maryland" , "Virginia" , "Kentucky" };
    vector<string> node_Wyoming = { "Montana" , "South_Dakota" , "Nebraska" , "Colorado" , "Utah" , "Idaho" , "Idaho" };

    map<string, vector<string>> kusa = { {"Alabama", node_Alabama}, {"Alaska", node_Alaska}, {"Arizona", node_Arizona}, {"Arkansas", node_Arkansas}, {"California", node_California}, {"Colorado", node_Colorado}, {"Connecticut", node_Connecticut}, {"Delaware", node_Delaware}, {"Florida", node_Florida}, {"Georgia", node_Georgia}, {"Hawaii", node_Hawaii}, {"Idaho", node_Idaho}, {"Illinois", node_Illinois}, {"Indiana", node_Indiana}, {"Iowa", node_Iowa}, {"Kansas", node_Kansas}, {"Kentucky", node_Kentucky}, {"Louisiana", node_Louisiana}, {"Maine", node_Maine}, {"Maryland", node_Maryland}, {"Massachusetts", node_Massachusetts}, {"Michigan", node_Michigan}, {"Minnesota", node_Minnesota}, {"Mississippi", node_Mississippi}, {"Missouri", node_Missouri}, {"Montana", node_Montana}, {"Nebraska", node_Nebraska}, {"Nevada", node_Nevada}, {"New_Hampshire", node_New_Hampshire}, {"New_Jersey", node_New_Jersey}, {"New_Mexico", node_New_Mexico}, {"New_York", node_New_York}, {"North_Carolina", node_North_Carolina}, {"North_Dakota", node_North_Dakota}, {"Ohio", node_Ohio}, {"Oklahoma", node_Oklahoma}, {"Oregon", node_Oregon}, {"Pennsylvania", node_Pennsylvania}, {"Rhode_Island", node_Rhode_Island}, {"South_Carolina", node_South_Carolina}, {"South_Dakota", node_South_Dakota}, {"Tennessee", node_Tennessee}, {"Texas", node_Texas}, {"Utah", node_Utah}, {"Vermont", node_Vermont}, {"Virginia", node_Virginia}, {"Washington", node_Washington}, {"West_Virginia", node_West_Virginia}, {"Wisconsin", node_Wisconsin}, {"Wyoming", node_Wyoming} };

    HybridLmxrlf* hybrid_lmxrlf = new HybridLmxrlf(kusa);

    map<string,int> resultant = hybrid_lmxrlf->color();

    delete hybrid_lmxrlf;

}