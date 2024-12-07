SELECT 
    MD5(CONCAT(fiscal_year_ending, roll_year, municipality, county, school_name)) AS fact_id,
    fiscal_year_ending,
    roll_year,
    MD5(municipality) AS municipality_id,
    MD5(county) AS county_id,
    MD5(school_name) AS school_district_id,
    county_tax_levy,
    county_tax_rate_outside_village_per_1000_assessed_value,
    county_tax_rate_inside_village_per_1000_assessed_value,
    municipality_tax_levy,
    municipal_tax_rate_outside_village_per_1000_assessed_value,
    municipal_tax_rate_inside_village_per_1000_assessed_value,
    school_district_tax_levy,
    school_district_tax_rate_per_1000_assessed_value
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`;
