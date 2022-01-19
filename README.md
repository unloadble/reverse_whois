# Register and get API code

register in whoisxmlapi.com and go to this page : https://user.whoisxmlapi.com/products and copy your API key.

# Replace your API key

Edit reverse_whois.py and replace your API key on line 
```
 api_key = 'YOUR API KEY'
```

# usage 
```
python3 reverse_whois.py -f [file.txt] -i [input URL or E-mail or etc ]

python3 reverse_whois.py  --file [file.txt] --input [input URL or E-mail or etc ]
```
