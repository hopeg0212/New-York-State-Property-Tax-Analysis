WITH base AS (
    SELECT DISTINCT
        fiscal_year_ending,
        roll_year,
        swis_code,
        municipality,
        county,
        school_code,
        school_name,
        type_of_value_on_whichtax_rates_are_applied,
        county_tax_levy,
        county_tax_rate_outside_village_per_1000_assessed_value,
        county_tax_rate_inside_village_per_1000_assessed_value,
        municipality_tax_levy,
        municipal_tax_rate_outside_village_per_1000_assessed_value,
        municipal_tax_rate_inside_village_per_1000_assessed_value,
        school_district_tax_levy,
        school_district_tax_rate_per_1000_assessed_value
    FROM `cis4400-hw-443410.cleaned_data.property_tax_rates`
)
SELECT * FROM base;
