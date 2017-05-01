================================================================================
ressources

https://github.com/movebank/movebank-api-doc/blob/master/movebank-api.md

sensor types
curl -u "$MOVEBANK_USER:$MOVEBANK_PASS" https://www.movebank.org/movebank/service/direct-read?entity_type=tag_type

================================================================================
studies

list studies
curl -u "$MOVEBANK_USER:$MOVEBANK_PASS" "https://www.movebank.org/movebank/service/direct-read?entity_type=study" > direct_read_study.csv

get info about study (no more than in list)
curl -u "$MOVEBANK_USER:$MOVEBANK_PASS" "https://www.movebank.org/movebank/service/direct-read?entity_type=study&study_id=5826799"

get animal reference (no taxon)
https://www.movebank.org/movebank/service/direct-read?entity_type=individual&study_id=2911040
curl -u "$MOVEBANK_USER:$MOVEBANK_PASS" "https://www.movebank.org/movebank/service/direct-read?entity_type=individual&study_id=3615655"

get events data
DOESNOTWORK curl -u "$MOVEBANK_USER:$MOVEBANK_PASS" "https://www.movebank.org/movebank/service/direct-read?entity_type=event&study_id=5826799"
curl -u "$MOVEBANK_USER:$MOVEBANK_PASS" "https://www.movebank.org/movebank/service/direct-read?entity_type=event&study_id=3615655"

================================================================================
170572260

curl -u "$MOVEBANK_USER:$MOVEBANK_PASS" "https://www.movebank.org/movebank/service/direct-read?entity_type=study&study_id=170572260"

================================================================================
get taxon

curl -u "$MOVEBANK_USER:$MOVEBANK_PASS" "https://www.movebank.org/movebank/service/public/json?study_id=2911040&individual_local_identifiers=4262-84830876&sensor_type=gps"

fa$ curl -u "$MOVEBANK_USER:$MOVEBANK_PASS" "https://www.movebank.org/movebank/service/direct-read?entity_type=individual&study_id=3615655"
comments,death_comments,earliest_date_born,exact_date_of_birth,id,latest_date_born,local_identifier,ring_id,sex,taxon_canonical_name
"Fixed-4",,,,3616439,,"Billy",,"m",
"Fixed-4",,,,3616440,,"Charlie",,"m",
"Fertile-?",,,,3616441,,"Dog",,"f",
"Fixed-14+",,,,3616442,,"Fred",,"m",
"Fixed-8",,,,3616443,,"Junior",,"m",
"Fixed-4",,,,3616444,,"Mookie",,"f",
"Fixed-1",,,,3616445,,"Orion",,"m",
"Fixed-6",,,,3616446,,"Quinton",,"m",
"Fixed-7",,,,3616447,,"Rusty",,"m",
"Fertile-?",,,,3616448,,"Smokey",,"f",
"Fertile-Adult",,,,3616449,,"Tiger",,"f",
"Fixed-4",,,,3616450,,"Willie",,"m",

curl -u "$MOVEBANK_USER:$MOVEBANK_PASS" "https://www.movebank.org/movebank/service/public/json?study_id=3615655&individual_local_identifiers=Willie&sensor_type=gps"

================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
