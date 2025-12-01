# send-hello.ps1
# Creates a session then sends "hello amigo" to it
param(
    [string]$BaseUrl = 'http://127.0.0.1:61675',
    [string]$ApiKey  = ''
)

# Build headers
$headers = @{ 'Accept' = 'application/json' }
if ($ApiKey -ne '') { $headers['Authorization'] = "Bearer $ApiKey" }

try {
  Write-Host "Creating session at $BaseUrl/session..."
  # 1) Create a new session
  $createBody = @{ title = "ps-session" }
  $createJson = $createBody | ConvertTo-Json -Depth 10

  $createResp = Invoke-RestMethod -Method Post -Uri "$BaseUrl/session" -Headers $headers -Body $createJson -ContentType 'application/json' -ErrorAction Stop
  Write-Host "Create response:`n$($createResp | ConvertTo-Json -Depth 5)"

  # extract session id (schema: Session.id, pattern ^ses.*)
  $sessionId = $createResp.id
  if (-not $sessionId -and $createResp.info -and $createResp.info.id) { $sessionId = $createResp.info.id }
  if (-not $sessionId -and $createResp."") { $sessionId = $createResp."" }

  if (-not $sessionId) {
    Write-Error "Unable to determine session id from create response: $($createResp | ConvertTo-Json -Depth 5)"
    exit 1
  }
  Write-Host "Created session: $sessionId"

  # 2) Send the prompt "hello amigo"
  $parts = @(
    @{ type = 'text'; text = 'hello amigo' }
  )
  $msgBody = @{ parts = $parts }
  $msgJson = $msgBody | ConvertTo-Json -Depth 10

  $url = "$BaseUrl/session/$sessionId/message"
  Write-Host "Posting message to $url ..."
  $resp = Invoke-RestMethod -Method Post -Uri $url -Headers $headers -Body $msgJson -ContentType 'application/json' -ErrorAction Stop

  Write-Host "Message POST response:`n$($resp | ConvertTo-Json -Depth 10)"
  exit 0
}
catch {
  Write-Error "Request failed: $($_.Exception.Message)"
  if ($_.Exception.Response -ne $null) {
    try { $body = (New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())).ReadToEnd(); Write-Host "Response body:`n$body" }
    catch { Write-Host "Could not read response body." }
  }
  exit 2
}
