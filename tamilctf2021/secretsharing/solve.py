from sslib import shamir
data = {'required_shares': 2, 'prime_mod': 'AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEp', 'shares': [
    '1-MEwx7cz+C01rL8H0Hhz2EIgHjWYXVcL81uITmRha674=', '2-YJhj22+ntS1s80CT9b6Y7ayc52baTFGNRpPUyLxtaf8=', '3-kOSVyRJRXw1utr8zzWA7ytEyQWedQuAdtkWV+GB/6EA=', '4-wTDHtrT7CO1wej3TpQHep/XHm2hgOW6uJfdXKASSZoE=', '5-8Xz5pFekss1yPbxzfKOBhRpc9WkjL/0+lakYV6ik5MI=']}
print(shamir.recover_secret(shamir.from_base64(data)).decode())
