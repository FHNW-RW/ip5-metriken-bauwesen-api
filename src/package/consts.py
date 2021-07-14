from typing import Final

# check data/README.me for more info about package

# general data info
FIELD_ID: Final = "id"
FIELD_SOURCE: Final = "source"
FIELD_TITLE: Final = "title"

# country
FIELD_NOM_COUNTRY: Final = "nom_country"
COUNTRY_CH: Final = "SWITZERLAND"
COUNTRY_DE: Final = "GERMANY"

# verification status
FIELD_VERIFICATION_STATUS: Final = "verification_status"
STATUS_VERIFIED: Final = "VERIFIED_OK"
STATUS_NOT_VERIFIED: Final = "NOT_VERIFIED"
STATUS_PARTIALLY_VERIFIED: Final = "PARTIALLY_VERIFIED"
STATUS_VERIFIED_OK_BUT_UNSUITABLE: Final = "VERIFIED_OK_BUT_UNSUITABLE"

# construction type
FIELD_NEUBAU_UMBAU: Final = "neubau_umbau"
CONSTRUCTION_TYPE_NEUBAU: Final = "NEUBAU"
CONSTRUCTION_TYPE_UMBAU: Final = "UMBAU"
CONSTRUCTION_TYPE_NEU_UND_UMBAU: Final = "NEU_UND_UMBAU"

# elevators
FIELD_ELEVATOR_PRESENT: Final = "bool_elevators"
FIELD_NUM_ELEVATOR: Final = "num_elevators"
FIELD_ELEVATOR_INCLINED_PRESENT: Final = "bool_elevators_inclined"
FIELD_NUM_ELEVATOR_INCLINED: Final = "num_elevators_inclined"

# garage type
GARAGE_TYPE_INDOOR: Final = "EINSTELLHALLEN"
GARAGE_TYPE_OUTDOOR: Final = "GARAGEN_FREISTEHEND"

# relevant features
FIELD_NOM_FACADE: Final = "nom_facade"
FIELD_AREA_TOTAL_FLOOR_416: Final = "area_total_floor_416"
FIELD_AREA_NET_FLOOR_416: Final = "area_net_floor_416"
FIELD_AREA_MAIN_USAGE: Final = "area_main_usage"
FIELD_VOLUME_TOTAL_416: Final = "volume_total_416"
FIELD_VOLUME_TOTAL_116: Final = "volume_total_116"
FIELD_NUM_BUILDINGS: Final = "num_buildings"
FIELD_NUM_FLOORS_OVERGROUND: Final = "num_floors_overground"
FIELD_NUM_FLOORS_UNDERGROUND: Final = "num_floors_underground"
FIELD_HNF_GF_RATIO: Final = "ratio_hnf_gf"

FIELD_DYN_EXPENSES_JSON: Final = "dyn_expenses_json"
FIELD_TOTAL_EXPENSES: Final = "total_expenses"
JSON_FIELD_TOTAL_EXPENSES_BKP: Final = "BKP_08"
JSON_FIELD_TOTAL_EXPENSES_EBKP: Final = "EBKP_12"

FIELD_DYN_COST_REF: Final = "dyn_cost_ref"
FIELD_COST_REF_GF: Final = "cost_ref_gf"
FIELD_COST_REF_GSF: Final = "cost_ref_gfs"
JSON_FIELD_GF: Final = "GF"
JSON_FIELD_GSF: Final = "GSF"

# usages
FIELD_USAGES: Final = "usages"
FIELD_USAGE_CLUSTER: Final = "usage_cluster"
FIELD_NOM_USAGE_MAIN: Final = "nom_usage_main"
FIELD_COMBINED_USAGE: Final = "combined_usage"

USAGE_TYPE: Final = "type"
USAGE_PERCENTAGE: Final = "percentage"

GARAGE_INDOOR_PRESENT: Final = "garage_indoor"
GARAGE_OUTDOOR_PRESENT: Final = "garage_outdoor"

GARAGE_INDOOR_PERCENTAGE: Final = "garage_indoor_percentage"
GARAGE_OUTDOOR_PERCENTAGE: Final = "garage_outdoor_percentage"

NOM_PRIMARY_USAGE: Final = "nom_primary_usage"
NOM_SECONDARY_USAGE: Final = "nom_secondary_usage"
NOM_TERTIARY_USAGE: Final = "nom_tertiary_usage"
NOM_QUATERNARY_USAGE: Final = "nom_quaternary_usage"

PRIMARY_USAGE_PERCENTAGE: Final = "primary_percentage"
SECONDARY_USAGE_PERCENTAGE: Final = "secondary_percentage"
TERTIARY_USAGE_PERCENTAGE: Final = "tertiary_percentage"
QUATERNARY_USAGE_PERCENTAGE: Final = "quaternary_percentage"
