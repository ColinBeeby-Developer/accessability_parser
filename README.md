# accessability_parser

To perform the parsing activities descripted here you will need to have nhsuk-cms running on your local environment. 
You will also have downloaded and restored a copy of the production database to your local environment.

## Acquiring site urls
Before you can parse any of the sites pages you will need to have collected the urls that you wish to examine into a file.
The file should be in the format of a single url on each line, EG

http://yousite.com/path/path1/

http://yoursite.com/path/page0/

http://yoursite.com/path/page2/

To build a urls file you can use the following command:

wget -m http://www.example.com 2>&1 | grep '^--' | awk '{ print $3 }' | grep -v '\.\(css\|js\|png\|gif\|jpg\|JPG\)$' > urls.txt

This may take a significant ammount of time to run, depending on how many pages you site contains.
Once you have created your urls.txt file, you can 'tidy' the file prior to processing with the parse_found_urls.py utility, which is provided as part of this repository.
