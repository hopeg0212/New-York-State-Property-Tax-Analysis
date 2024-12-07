SELECT 
    school_name,
    MAX(school_district_tax_rate_per_1000_value) AS max_school_tax_rate
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
GROUP BY 
    school_name
ORDER BY 
    max_school_tax_rate DESC
LIMIT 10;
