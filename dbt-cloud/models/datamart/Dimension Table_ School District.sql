SELECT 
    MD5(school_name) AS school_district_id,
    school_name,
    school_code
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
GROUP BY 
    school_name, school_code;
