# RPYC Demo

Setup:

```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
npm install -g foreman
```

Running:

```
source env/bin/activate # In every tab
nf start -j Procfile.dev # Runs three servers on one process. Can be run independently instead
```

## Testing

Try out:
http://localhost:5000/primes?n=100

Also:
http://localhost:5000/async?n=12929301020229321282823

Or, run the server (above) then run in another tab:
```
python test.py
```

## More

https://rpyc.readthedocs.io/en/latest/tutorial/tut3.html