addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  if (request.method === 'POST') {
    const body = await request.text()
    const parsedBody = new URLSearchParams(body)

    // Extract code, grant_type, and refresh_token from request body
    const code = parsedBody.get('code')
    const grantType = parsedBody.get('grant_type')
    const refreshToken = parsedBody.get('refresh_token')

    // Create POST request options with extracted fields and constants
    const url = 'https://services.leadconnectorhq.com/oauth/token'
    const options = {
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: new URLSearchParams({
        client_id: 'YOURCLIENTIDHERE',
        client_secret: 'YOURCLIENTSECRETHERE',
        grant_type: grantType,
        code: code,
        refresh_token: refreshToken
      })
    }

    try {
      const response = await fetch(url, options)
      const data = await response.json()
      return new Response(JSON.stringify(data), {status: 200})
    } catch (error) {
      console.error(error)
      return new Response('Error', {status: 500})
    }
  } else {
    return new Response('Method not allowed', {status: 405})
  }
}
