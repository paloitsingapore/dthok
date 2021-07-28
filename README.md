# Introduction
PSTD BulkData Generator is a open-source  standalone tool to generate mock Test data in form of csv,  and xml format which can be used for any Mock Service, Performance Testing etc. It required input parameter as  schema file where required structure is defined with data type, number of records and required format.

It's a cross-platform stand-alone executable tool can be used in Windows, Linux and Mac operating system.

# Index
<table>
<tr>
  <th>Setup</th>
  <td>
      <a href="#Installation">Installation</a>
    | <a href="#Execution">Execution</a>
  </td>
</tr>
<tr>
  <th>Input Data Type</th>
  <td>
      <a href="#alphabets"><code>alphabets</code></a>
    | <a href="#alphanumeric"><code>alpha-numeric</code></a>
    | <a href="#numeric"><code>numeric</code></a>
    | <a href="#code"><code>code</code></a>
    | <a href="#title"><code>title</code></a>
    | <a href="#firstName"><code>firstName</code></a>
    | <a href="#lastName"><code>lastName</code></a>
    | <a href="#date_of_birth"><code>date_of_birth</code></a>
    | <a href="#choices"><code>choices</code></a>
    | <a href="#PhoneNumber"><code>PhoneNumber</code></a>
    | <a href="#email"><code>email</code></a>
    | <a href="#streetName"><code>streetName</code></a>
    | <a href="#postcode"><code>postcode</code></a>
    | <a href="#country"><code>country</code></a>
    | <a href="#city"><code>city</code></a>
    | <a href="#date"><code>date</code></a>
    | <a href="#company"><code>company</code></a>
    | <a href="#boolean"><code>boolean</code></a>
    | <a href="#accountNumber"><code>accountNumber</code></a>
    | <a href="#constant"><code>constant</code></a>

  </td>
</tr>
<tr>
  <th>Output File Format</th>
  <td>
      <a href="#csv">csv</a> 
    | <a href="#json">json</a>
    | <a href="#xml">xml</a>
  </td>
</tr>
</table>

# Features

* Generate random records in required format like , xml and csv.
* Cross-platform application on Windows, Linux and macOS.
* Use as a stand-alone executable application in Windows and macOS without any installation.
* Configure required DataType for record values.
* Generate randomised Nested  payload

## Input Datatype
Required input schema definition have to provided with all required Field name and required datatype in JSON format. Here is Sample input Schema definition [file](https://github.com/bpanda130/DataGenerator/tree/master/Helper/SampleInputFile),

![Schema Defination Image](https://github.com/paloitsingapore/bulk_data_generation/blob/main/resources/InputSchemaDefination.JPG)


Below are the sample data type syntax that can be used in input file.
### alphabets

To generate random alphabetic String

Syntax: 
```json
"<Node Name>" : "alphabet|<length>"
```
e.g.
```json
"ProductName" : "alphabet|30"
```

### alphanum
To generate random alphanumeric String

Syntax: 
```json
"<Node Name>" : "alphanum|<length>"
```
e.g.
```json
"ProductNumber" : "alphanum|30"
```

### numeric
To generate random numeric value

Syntax: 
```json
"<Node Name>" : "numeric|<length>"
```
e.g.
```json
"ProductID" : "numeric|30"
```

### code
If you want to generate a code with some Prefix String

Syntax: 
```json
"<Node Name>" : "code||<Prefix String><regex>"
```
* Number signs (‘#’) are replaced with a random digit (0 to 9)
* Number signs (‘#’) are replaced with a random digit (0 to 9)
* Percent signs (‘%’) are replaced with a random non-zero digit (1 to 9)
* Exclamation marks (‘!’) are replaced with a random digit or an empty string
* At symbols (‘@’) are replaced with a random non-zero digit or an empty string

e.g.
```json
"EmployeeID" : "code||PALO-%%-##LTD!@"

Output: 
"EmployeeID": "PALO-26-12LTD8"
```
### title
To generate random salutations like Dr. or Mr. or Mrs. or Mx.

Syntax: 
```json
"<Node Name>" : "alphabet||title"
```
e.g.
```json
"Salutation" : "alphabet||title"

Output: 
"Salutation": "Mr."
```

### firstName
Use to generate random firstName

Syntax: 
```json
"<Node Name>" : "alphabet|<Max length>|firstName"
```
e.g.
```json
"Firstname" : "alphabet|20|firstName",

Output: 
"Firstname": "Samantha"
```

### lastName
Use to generate random lastname

Syntax: 
```json
"<Node Name>" : "alphabet|<Max length>|lastName"
```
e.g.
```json
"LastName" : "alphabet|20|lastName"

Output: 
"LastName": "Daniel"
```

### date_of_birth
Use to generate random date_of_birth

Syntax: 
```json
"<Node Name>" : "date_of_birth|MinAge=<age>,MaxAge=<age>|<DateFormat>"
```
e.g.
```json
"DOB" : "date_of_birth|MinAge=30,MaxAge=40|%m-%d-%Y"

Output: 
"DOB": "04-14-1981"
```

### choices
If we want to select a value randomly from given choices

Syntax: 
```json
"<Node Name>" : "choices|(<'value1', 'value2'>)|"
```
e.g.
```json
"AddressType": "choices|('RES', 'OFF', 'WRK')|"

Output: 
"AddressType": "RES"
```

### PhoneNumber
Random Phone Number based on country

Syntax: 
```json
"<Node Name>" : "PhoneNumber||<Country Name>"
```
e.g.
```json
"Mobile" : "PhoneNumber||India"

Output: 
"Mobile": "+917880010426"
```
### email
Random Email Address

Syntax: 
```json
"<Node Name>" : "alphanum||email"
```
e.g.
```json
"emailId" : "alphanum||email"

Output: 
"emailId": "ncooper@hopkins.com"
```

### streetName
Random Street Address Name

Syntax: 
```json
"<Node Name>" : "alphabet|<length>|streetName"
```
e.g.
```json
"Street-1": "alphabet|20|streetName"

Output: 
"Street-1": "Douglas Crossing"
```

### postcode
Random postcode

Syntax: 
```json
"<Node Name>" : "numeric|<length>|postcode"
```
e.g.
```json
"Postalcode": "numeric|6|postcode"

Output: 
"Postalcode": "20494"
```
### country
Random country

Syntax: 
```json
"<Node Name>" : "alphabet||country"
```
e.g.
```json
"country": "alphabet||country"

Output: 
"country": "Singapore"
```
### city
Random city

Syntax: 
```json
"<Node Name>" : "alphabet||city"
```
e.g.
```json
"City": "alphabet||city"

Output: 
"city": "Bangalore"
```

### date
Generate Random Date between two date

Syntax: 
```json
"<Node Name>" : "date|StartDate=<date in yyyyMMdd>,EndDate=<date in yyyyMMdd>|<required Date Format>"
```
e.g.
```json
"DOJ": "date|StartDate=20100223,EndDate=20200330|%Y-%m-%d"

Output: 
"DOJ": "2011-07-04"
```

### company
Generate Random Company Name

Syntax: 
```json
"<Node Name>" : "alphabet||company"
```
e.g.
```json
"Client": "alphabet||company"

Output: 
"Client": "Williams-Harris"
```

### boolean
Randomly choose boolean value

Syntax: 
```json
"<Node Name>" : "boolean||"
```
e.g.
```json
"Active": "boolean||"

Output: 
"Active": "False"
```

### accountNumber
Generate random Basic or Internal account number 

Syntax: 
```json
"<Node Name>" : "alphanum|<Account Type>|accountNumber" 
```
* NONE - Generate a Basic Bank Account Number (BBAN)
* Internal - Generate an International Bank Account Number (IBAN)

e.g.
```json
"AccountNum": "alphanum|NONE|accountNumber"

Output: 
"AccountNum": "JRMR05894987945503"
```
### constant
If you want to use Constant values for all the records

Syntax: 
```json
"<Node Name>" : "constant|<Required Value>|"
```
* NONE - Generate a Basic Bank Account Number (BBAN)
* Internal - Generate an International Bank Account Number (IBAN)

e.g.
```json
"Salary": "constant|Monthly|"

Output: 
"Salary": "Monthly"
```

##Installation
- To Install required 3rd party libraries use the available file from [here](https://github.com/paloitsingapore/bulk_data_generation/blob/main/installation.sh)

##Execution
To execute on any OS use the below command to generate required bulk Data,
```commandline
python dataGene.py "<input Payload file path>" "<No. of Records>" "<Output file format (csv, json or xml)>"
```
For Example:
```commandline
python3 dataGene.py "/mnt/c/user/test.json" "1000" "xml"
```

- To generate required output file use this [reference](https://github.com/paloitsingapore/bulk_data_generation/tree/main/resources/Bulk_Data_Generator_Execution_Flow.mp4)