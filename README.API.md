# speech API backend application

## Installation

```
pip install -r api/requirements.txt
```

## Local Execution

Set the environment variable:

Note: as written, the python request to elevenlabs does not appear to be using this. See
the elevenlabs python library docs for info about making use of the API key.

```
export ELEVENLABS_API_KEY=your-api-key
```


Run the API:

```
uvicorn api.speech:app --reload
```

The API is available at http://localhost:8000/

Note: This uses [Starlette](https://www.starlette.io/) rather than Flask because:

 - inherent async functionality
 - builtin concept of background jobs

This could easily be ported to any other Python web framework.


## Open the example client in a browser

An example client is provided at api/client.html and can simply be opened in a browser as
a file. Submitting text should result in a backend request to elevenlabs and a resulting
audio file written to `files/<userID>` which should subsequently be shown in the file
list in the browser. Click an item in the list to play it.

This is meant as a reference example for baseline functionality with the backend API
and does not provide, e.g. user authentication. The userID is currently hard-coded into
the client-side javascript.
