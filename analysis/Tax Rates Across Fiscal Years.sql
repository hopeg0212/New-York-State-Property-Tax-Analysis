SELECT 
    fiscal_year_ending,
    AVG(county_tax_rate_outside_village_per_1000_assessed_value) AS avg_county_tax_rate,
    AVG(municipal_tax_rate_outside_village_per_1000_assessed_value) AS avg_municipal_tax_rate,
    AVG(school_district_tax_rate_per_1000_assessed_value) AS avg_school_district_tax_rate
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
WHERE 
    county = 'Albany'
GROUP BY 
    fiscal_year_ending
ORDER BY 
    fiscal_year_ending;
