SELECT 
    MD5(county) AS county_id,
    county
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
GROUP BY 
    county;
