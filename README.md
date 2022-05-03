# Sort the input contry names by continent and alphabetical order
This script is to sort country names by continent and alphabetical order

### Prerequites:
- pycountry
- pycountry_convert

`
pip3 install pycountry, pycountry_convert
`

### Input:
**Correct** country names sperate by ', ' 


For example:
'Nigeria, Canada'

Incorrect input:
~~'nigeria, canada'~~


### Output:

```
North America
===============
Canada


South America
===============


Asia
===============


Australia
===============


Africa
===============
Nigeria


Europe
===============

```

### References:
- [https://stackoverflow.com/questions/55910004/get-continent-name-from-country-using-pycountry](https://stackoverflow.com/questions/55910004/get-continent-name-from-country-using-pycountry)

### Updates
- added multiple delimeters support for split (05/03/5022)   
