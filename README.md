# OSINT
Scripts to automate Open Source Intelligence (OSINT)

## [Twitter](https://github.com/0xmachos/OSINT/tree/master/Twitter)

### `dump.py`
- Dump a Twitter users follwers and following 

### `search.py`
- Search the files created by `dump.py` for a string 

### `device.py`
- Print a sorted list of the device used to sent a users last 100 tweets

## [Infrastructure](https://github.com/0xmachos/OSINT/tree/master/Infrastructure)

### `ct-abuse.py`
- For the given domain query [Certificate Transparency](https://www.certificate-transparency.org/what-is-ct) to get a list of subdomains which have SSL/TLS certificates issued for them 
- Usage: `./ct-abuse.py {target_domain}`

