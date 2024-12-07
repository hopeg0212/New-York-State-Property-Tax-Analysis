SELECT 
    fiscal_year_ending,
    SUM(county_tax_levy) AS total_county_tax_levy,
    SUM(municipality_tax_levy) AS total_municipal_tax_levy,
    SUM(school_district_tax_levy) AS total_school_district_tax_levy
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
GROUP BY 
    fiscal_year_ending
ORDER BY 
    fiscal_year_ending ASC;
