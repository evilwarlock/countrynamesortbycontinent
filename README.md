# Sort the input contry names by continent and alphabetical order
This project starts when I am trying to figure out which countries/institution have cited my paper, I could not find a converter to sort them by the country and plot them to show the significance of my research work.

future work may include the automation part via google scholar

### Prerequites:
- pycountry
- pycountry_convert

`
pip3 install pycountry, pycountry_convert
`

### Input:
**Correct** country names sperate by ',' (updated with pretty much any common delimeters) 


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
