const API_ENDPOINT = 'https://services.leadconnectorhq.com/oauth/token';
const CLIENT_ID = 'INSERT_CLIENT_ID_HERE';
const CLIENT_SECRET = 'INSERT_CLIENT_SECRET_HERE';

addEventListener('fetch', event => {
  event.respondWith(processRequest(event.request))
})

async function processRequest(request) {
  if (request.method !== 'POST') {
    return new Response('Only POST method is allowed', { status: 405 });
  }

  try {
    const { authorizationCode, grantType, refreshToken } = await extractRequestBody(request);
    const requestOptions = buildPostRequestOptions(grantType, authorizationCode, refreshToken);
    const apiResponse = await fetch(API_ENDPOINT, requestOptions);
    const responseData = await apiResponse.json();
    return new Response(JSON.stringify(responseData), { status: 200 });
  } catch (error) {
    console.error(error);
    return new Response(`Error processing request: ${error.message}`, { status: 500 });
  }
}

async function extractRequestBody(request) {
  const requestBody = await request.text();
  const params = new URLSearchParams(requestBody);
  return {
    authorizationCode: params.get('code'),
    grantType: params.get('grant_type'),
    refreshToken: params.get('refresh_token'),
  };
}

function buildPostRequestOptions(grantType, authorizationCode, refreshToken) {
  return {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      client_id: CLIENT_ID,
      client_secret: CLIENT_SECRET,
      grant_type: grantType,
      code: authorizationCode,
      refresh_token: refreshToken,
    })
  };
}
