const API_URL = 'https://services.leadconnectorhq.com/oauth/token';
const CLIENT_ID = 'YOURCLIENTIDHERE';
const CLIENT_SECRET = 'YOURCLIENTSECRETHERE';

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  if (request.method !== 'POST') {
    return new Response('Method not allowed', {status: 405});
  }

  try {
    const {code, grantType, refreshToken} = await parseRequestBody(request);
    const options = createPostRequestOptions(grantType, code, refreshToken);
    const response = await fetch(API_URL, options);
    const data = await response.json();
    return new Response(JSON.stringify(data), {status: 200});
  } catch (error) {
    console.error(error);
    return new Response(`Error: ${error.message}`, {status: 500});
  }
}

async function parseRequestBody(request) {
  const body = await request.text();
  const parsedBody = new URLSearchParams(body);
  return {
    code: parsedBody.get('code'),
    grantType: parsedBody.get('grant_type'),
    refreshToken: parsedBody.get('refresh_token'),
  };
}

function createPostRequestOptions(grantType, code, refreshToken) {
  return {
    method: 'POST',
    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    body: new URLSearchParams({
      client_id: CLIENT_ID,
      client_secret: CLIENT_SECRET,
      grant_type: grantType,
      code: code,
      refresh_token: refreshToken,
    })
  };
}
