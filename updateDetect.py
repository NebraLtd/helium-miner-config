import urllib.request, json, os
supervisorAddress = str(os.environ['BALENA_SUPERVISOR_ADDRESS'])
supervisorKey = str(os.environ['BALENA_SUPERVISOR_API_KEY'])
supervisorAddress = "%s/v2/applications/state?apikey=%s" % (supervisorAddress, supervisorKey)
with urllib.request.urlopen(balenaState) as url:
    data = json.loads(url.read().decode())
    print(data)
