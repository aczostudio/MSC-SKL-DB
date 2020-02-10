SELECT cpo.CustomerProductOrderID, cpo.CustomerProductOrderQuantity, 
cpo.CustomerProductOrderVat, cpo.ProductName, pro.ProductDescription, pro.ProductPrice 
FROM customerproductorder cpo 
JOIN product pro ON cpo.ProductName = pro.ProductName