[comment]: # "Auto-generated SOAR connector documentation"
# Pipl

Publisher: Splunk Community  
Connector Version: 3\.0\.0  
Product Vendor: Pipl  
Product Name: Pipl  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.1\.0  

This app integrates with Pipl to perform an investigative action

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Pipl asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api\_key** |  required  | password | API Key

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate API Key with Pipl server  
[get user](#action-get-user) - Get information about a person  

## action: 'test connectivity'
Validate API Key with Pipl server

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get user'
Get information about a person

Type: **investigate**  
Read only: **True**

Please enter all the information you have about the person you're searching for\. At least one field is required\: Email, Phone, Username, Url, Name \(First \+ Last\), or Full Address \(House Number \+ Street \+ City \+ State\)\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**first\_name** |  optional  | First Name | string | 
**last\_name** |  optional  | Last Name | string | 
**email** |  optional  | Email | string |  `email` 
**phone** |  optional  | Phone Number | string |  `phone` 
**username** |  optional  | Username | string |  `user name` 
**url** |  optional  | URL | string |  `url` 
**street** |  optional  | Street Name | string | 
**house\_number** |  optional  | House Number | string | 
**city** |  optional  | City | string | 
**zip\_code** |  optional  | Zip Code | string | 
**state** |  optional  | State Abbreviation | string | 
**country** |  optional  | Country Abbreviation | string | 
**age** |  optional  | Age \(Exact Age or Range\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.age | string | 
action\_result\.parameter\.city | string | 
action\_result\.parameter\.country | string | 
action\_result\.parameter\.email | string |  `email` 
action\_result\.parameter\.first\_name | string | 
action\_result\.parameter\.house\_number | string | 
action\_result\.parameter\.last\_name | string | 
action\_result\.parameter\.phone | string |  `phone` 
action\_result\.parameter\.state | string | 
action\_result\.parameter\.street | string | 
action\_result\.parameter\.url | string |  `url` 
action\_result\.parameter\.username | string |  `user name` 
action\_result\.parameter\.zip\_code | string | 
action\_result\.data\.\*\.available\_data\.basic\.addresses | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.dobs | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.educations | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.emails | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.ethnicities | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.genders | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.images | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.jobs | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.landline\_phones | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.languages | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.mobile\_phones | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.names | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.origin\_countries | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.phones | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.relationships | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.social\_profiles | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.user\_ids | numeric | 
action\_result\.data\.\*\.available\_data\.basic\.usernames | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.addresses | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.dobs | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.educations | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.emails | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.ethnicities | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.genders | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.images | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.jobs | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.landline\_phones | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.languages | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.mobile\_phones | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.names | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.origin\_countries | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.phones | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.relationships | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.social\_profiles | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.user\_ids | numeric | 
action\_result\.data\.\*\.available\_data\.premium\.usernames | numeric | 
action\_result\.data\.\*\.available\_sources | numeric | 
action\_result\.data\.\*\.http\_status\_code | numeric | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.apartment | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.city | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.country | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.display | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.house | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.last\_seen | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.po\_box | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.state | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.street | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.type | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.valid\_since | string | 
action\_result\.data\.\*\.people\.\*\.addresses\.\*\.zip\_code | string | 
action\_result\.data\.\*\.people\.\*\.dob\.date\_range\.end | string | 
action\_result\.data\.\*\.people\.\*\.dob\.date\_range\.start | string | 
action\_result\.data\.\*\.people\.\*\.dob\.display | string | 
action\_result\.data\.\*\.people\.\*\.dob\.valid\_since | string | 
action\_result\.data\.\*\.people\.\*\.educations\.\*\.date\_range\.end | string | 
action\_result\.data\.\*\.people\.\*\.educations\.\*\.date\_range\.start | string | 
action\_result\.data\.\*\.people\.\*\.educations\.\*\.degree | string | 
action\_result\.data\.\*\.people\.\*\.educations\.\*\.display | string | 
action\_result\.data\.\*\.people\.\*\.educations\.\*\.school | string | 
action\_result\.data\.\*\.people\.\*\.emails\.\*\.address | string |  `email` 
action\_result\.data\.\*\.people\.\*\.emails\.\*\.address\_md5 | string |  `md5` 
action\_result\.data\.\*\.people\.\*\.emails\.\*\.disposable | boolean | 
action\_result\.data\.\*\.people\.\*\.emails\.\*\.email\_provider | boolean | 
action\_result\.data\.\*\.people\.\*\.emails\.\*\.type | string | 
action\_result\.data\.\*\.people\.\*\.ethnicities\.\*\.content | string | 
action\_result\.data\.\*\.people\.\*\.gender\.content | string | 
action\_result\.data\.\*\.people\.\*\.gender\.valid\_since | string | 
action\_result\.data\.\*\.people\.\*\.id | string | 
action\_result\.data\.\*\.people\.\*\.images\.\*\.url | string |  `url` 
action\_result\.data\.\*\.people\.\*\.images\.\*\.valid\_since | string | 
action\_result\.data\.\*\.people\.\*\.jobs\.\*\.date\_range\.end | string | 
action\_result\.data\.\*\.people\.\*\.jobs\.\*\.date\_range\.start | string | 
action\_result\.data\.\*\.people\.\*\.jobs\.\*\.display | string | 
action\_result\.data\.\*\.people\.\*\.jobs\.\*\.industry | string | 
action\_result\.data\.\*\.people\.\*\.jobs\.\*\.organization | string | 
action\_result\.data\.\*\.people\.\*\.jobs\.\*\.title | string | 
action\_result\.data\.\*\.people\.\*\.languages\.\*\.display | string | 
action\_result\.data\.\*\.people\.\*\.languages\.\*\.inferred | boolean | 
action\_result\.data\.\*\.people\.\*\.languages\.\*\.language | string | 
action\_result\.data\.\*\.people\.\*\.languages\.\*\.region | string | 
action\_result\.data\.\*\.people\.\*\.match | numeric | 
action\_result\.data\.\*\.people\.\*\.names\.\*\.display | string | 
action\_result\.data\.\*\.people\.\*\.names\.\*\.first | string | 
action\_result\.data\.\*\.people\.\*\.names\.\*\.last | string | 
action\_result\.data\.\*\.people\.\*\.names\.\*\.last\_seen | string | 
action\_result\.data\.\*\.people\.\*\.names\.\*\.middle | string | 
action\_result\.data\.\*\.people\.\*\.names\.\*\.prefix | string | 
action\_result\.data\.\*\.people\.\*\.names\.\*\.type | string | 
action\_result\.data\.\*\.people\.\*\.names\.\*\.valid\_since | string | 
action\_result\.data\.\*\.people\.\*\.origin\_countries\.\*\.country | string | 
action\_result\.data\.\*\.people\.\*\.origin\_countries\.\*\.inferred | boolean | 
action\_result\.data\.\*\.people\.\*\.phones\.\*\.country\_code | numeric | 
action\_result\.data\.\*\.people\.\*\.phones\.\*\.display | string |  `phone` 
action\_result\.data\.\*\.people\.\*\.phones\.\*\.display\_international | string |  `phone` 
action\_result\.data\.\*\.people\.\*\.phones\.\*\.do\_not\_call | boolean | 
action\_result\.data\.\*\.people\.\*\.phones\.\*\.last\_seen | string | 
action\_result\.data\.\*\.people\.\*\.phones\.\*\.number | numeric | 
action\_result\.data\.\*\.people\.\*\.phones\.\*\.type | string | 
action\_result\.data\.\*\.people\.\*\.phones\.\*\.valid\_since | string | 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.emails\.\*\.address | string |  `email` 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.emails\.\*\.address\_md5 | string |  `md5` 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.emails\.\*\.disposable | boolean | 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.emails\.\*\.email\_provider | boolean | 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.names\.\*\.display | string | 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.names\.\*\.first | string | 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.names\.\*\.last | string | 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.names\.\*\.middle | string | 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.names\.\*\.type | string | 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.subtype | string | 
action\_result\.data\.\*\.people\.\*\.relationships\.\*\.type | string | 
action\_result\.data\.\*\.people\.\*\.search\_pointer | string | 
action\_result\.data\.\*\.people\.\*\.urls\.\*\.category | string | 
action\_result\.data\.\*\.people\.\*\.urls\.\*\.domain | string |  `domain` 
action\_result\.data\.\*\.people\.\*\.urls\.\*\.name | string | 
action\_result\.data\.\*\.people\.\*\.urls\.\*\.source\_id | string |  `md5` 
action\_result\.data\.\*\.people\.\*\.urls\.\*\.url | string |  `url` 
action\_result\.data\.\*\.people\.\*\.user\_ids\.\*\.content | string | 
action\_result\.data\.\*\.people\.\*\.user\_ids\.\*\.last\_seen | string | 
action\_result\.data\.\*\.people\.\*\.user\_ids\.\*\.valid\_since | string | 
action\_result\.data\.\*\.people\.\*\.usernames\.\*\.content | string | 
action\_result\.data\.\*\.people\.\*\.usernames\.\*\.last\_seen | string | 
action\_result\.data\.\*\.persons\_count | numeric | 
action\_result\.data\.\*\.query\.addresses\.\*\.country | string | 
action\_result\.data\.\*\.query\.addresses\.\*\.display | string | 
action\_result\.data\.\*\.query\.addresses\.\*\.house | string | 
action\_result\.data\.\*\.query\.addresses\.\*\.state | string | 
action\_result\.data\.\*\.query\.addresses\.\*\.street | string | 
action\_result\.data\.\*\.query\.addresses\.\*\.zip\_code | string | 
action\_result\.data\.\*\.query\.dob\.date\_range\.end | string | 
action\_result\.data\.\*\.query\.dob\.date\_range\.start | string | 
action\_result\.data\.\*\.query\.dob\.display | string | 
action\_result\.data\.\*\.query\.emails\.\*\.address | string |  `email` 
action\_result\.data\.\*\.query\.emails\.\*\.address\_md5 | string |  `md5` 
action\_result\.data\.\*\.query\.emails\.\*\.type | string | 
action\_result\.data\.\*\.query\.names\.\*\.display | string | 
action\_result\.data\.\*\.query\.names\.\*\.first | string | 
action\_result\.data\.\*\.query\.names\.\*\.last | string | 
action\_result\.data\.\*\.query\.user\_ids\.\*\.content | string | 
action\_result\.data\.\*\.query\.usernames\.\*\.content | string | 
action\_result\.data\.\*\.search\_id | string | 
action\_result\.data\.\*\.visible\_sources | numeric | 
action\_result\.data\.\*\.warnings | string | 
action\_result\.summary\.exact\_match\_found | boolean | 
action\_result\.summary\.possible\_matches | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 